import os
import argparse
from multiprocessing import Pool, Process
import multiprocessing
# import subprocess
import logging

import bbc
import apnews
import reuters


SOURCES = [bbc, apnews, reuters]


def run(source):
    p = source().get_articles()
    print(f'Start "{p}" task!')


if __name__ == '__main__':
    procs = []
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sources', type=str, nargs='+', help='add source "bbc", "appnews" or "reuters"')
    args = parser.parse_args()
    pool = Pool(processes=len(args.sources))
    try:
        for source in SOURCES:
            if source.__name__ in args.sources:
                print(source.__name__)
                result = pool.apply_async(run, args=(source.Agent,))
                print(result.get(timeout=180))
                pool.close()
                pool.join()
    except Exception as exception:
        print(f'Critical Error: {exception}')
        raise SystemExit(1)
