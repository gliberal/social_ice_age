#!/usr/bin/env python3

from mastodon import Mastodon

from diaspora.DiasporaParser import DiasporaParser

if __name__ == "__main__":
    print("hello")
    parser = DiasporaParser("./diaspora/sauvegarde_diaspora.json")
    for post in parser.get_statuses():
        print(post)
