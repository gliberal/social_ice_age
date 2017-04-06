#!/usr/bin/env python3

from mastodon import Mastodon

from diaspora.DiasporaParser import DiasporaParser
from twitter.TwitterParser import TwitterParser

if __name__ == "__main__":
    print("--- Social Ice Age ---")
    parser = DiasporaParser("./diaspora/sauvegarde_diaspora.json")
    for post in parser.get_statuses():
        print(post)
    for post in parser.get_shares():
        print(post)

    parser = TwitterParser("./twitter/tweets.csv")
    for post in parser.get_statuses():
        print(post)
    for post in parser.get_shares():
        print(post)
