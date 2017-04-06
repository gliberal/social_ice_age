#!/usr/bin/env python3

import json


class DiasporaPost:
    """
    This class is an abstraction of a Diaspora post (share or status)
    """

    def __init__(self, text, date):
        self.text = text
        self.date = date

    def __str__(self):
        return "%s - %s" % (self.date, self.text)


class DiasporaParser:
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
        self.load_diaspora_information_from_file()

    def load_diaspora_information_from_file(self):
        """
        Load the content of the provided file into Diaspora fields
        """
        # Open the file
        with open(self.file_path, 'r') as diaspora_backup_file:
            # Load the content into json structure
            diaspora_json_data = json.loads(diaspora_backup_file.read())

            # Retrieve the user informations
            self.user_pseudo = diaspora_json_data['user']['username']
            self.user_name = diaspora_json_data['user']['name']
            self.user_mail = diaspora_json_data['user']['email']

            # Iterate over statuses
            for post_entry in diaspora_json_data['user']['posts']:
                # If the text is not empty
                if post_entry['text'].strip():
                    if 'Reshare' in post_entry['type']:
                        self.shares.append(DiasporaPost(post_entry['text'], post_entry['created_at']))
                    elif 'StatusMessage' in post_entry['type']:
                        self.statuses.append(DiasporaPost(post_entry['text'], post_entry['created_at']))

    def get_statuses(self, min=0, max=0):
        return self.statuses


if __name__ == "__main__":
    print("Calling DiasporaParser manually")
    parser = DiasporaParser("./sauvegarde_diaspora.json")
    for post in parser.get_statuses():
        print(post)