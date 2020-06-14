import os
import argparse
from multiprocessing import Pool
import subprocess

import bbc
import apnews
import reuters


bbc = bbc.Agent()
apnews = apnews.Agent()
reuters = reuters.Agent()
SOURCES = [bbc, apnews, reuters]

# def run(func):
#     dirname = os.path.dirname(os.path.abspath(__file__))
#     subprocess.call(os.path.join(dirname, func+'.py'))


def run(sources):
    for source in sources:
        if source in SOURCES:
            print(sources)

# print(reuters.get_articles())
# run(script)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sources', type=str, nargs='+', help='Pass source name/s')
    args = parser.parse_args()
    run(args.sources)