#!/usr/bin/env python3

import csv


class Tweet:
    """
    This class is an abstraction of a Twitter post (RT or status)
    """

    def __init__(self, text, date):
        self.text = text
        self.date = date

    def __str__(self):
        return "%s - %s" % (self.date, self.text)


class TwitterParser:
    """
    This class loads directly the content of the file provided in the constructor in human readable data.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.user_name = ""
        self.user_pseudo = ""
        self.user_mail = ""
        self.shares = []
        self.statuses = []
        self.load_tweets_from_file()

    def load_tweets_from_file(self):
        """
        Load the content of the provided file into Twitter fields
        """
        # Open the file
        with open(self.file_path, 'r') as twitter_backup_file:
            # Load the content into csv structure and iterate over it
            tweets = csv.reader(twitter_backup_file, delimiter=',')
            for tweet in tweets:
                if tweet[5].startswith('RT'):
                    self.shares.append(Tweet(tweet[5][3:], tweet[3]))
                else:
                    self.statuses.append(Tweet(tweet[5], tweet[3]))

    def get_statuses(self, min=0, max=0):
        return self.statuses

    def get_shares(self, min=0, max=0):
        return self.shares

if __name__ == "__main__":
    print("Calling TwitterParser manually")
    parser = TwitterParser("./tweets.csv")
    for tweet in parser.get_statuses():
        print(tweet)
