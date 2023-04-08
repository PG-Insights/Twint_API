#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 09:45:15 2023

@author: dale
"""

import json
import argparse
import subprocess
import pandas as pd
from os import chdir
from pathlib import Path

TWINT_API_DIR = Path(__file__).parent

def create_query(*args):
    return ' '.join(*args)


def return_query_results(
        query: str
    ) -> subprocess:
    global TWINT_API_DIR
    chdir(TWINT_API_DIR)
    cmd = [
        'go',
        'run',
        'main.go',
        '-Query',
        query,
        '-Instance',
        'birdsite.xanny.family',  
        '-Format',
        'json',
        '-lang',
        'en'
    ]
    # If Instance needs to be modified use a value from https://github.com/zedeus/nitter/wiki/Instances

    process = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True
    )
    return process.stdout


def parse_json_returned(json_str: str) -> json:
    return json.loads(
        json.JSONEncoder().encode(
            json_str
        )
    )


if __name__ == '__main__':
    from datetime import datetime
    parser = argparse.ArgumentParser(
        description='Run "Twint Zero" API Twitter Query'
    )
    parser.add_argument(
        'query', 
        nargs='?', 
        default='from:LetMOPLay within_time:48h filter:has_engagement',
        help='Twitter query string: https://github.com/igorbrigadir/twitter-advanced-search'
    )
    args = parser.parse_args()
    query_str = create_query(
        args.query
    )
    json_str = return_query_results(
        query_str, 
    )
    response_json = parse_json_returned(
        json_str
    )
    df = pd.read_json(
        response_json, 
        lines=True
    )
    response_dir = Path(
        TWINT_API_DIR,
        'twint-responses'
    )
    response_dir.mkdir(exist_ok=True)
    save_name = f'{datetime.now()}_{args.query}'
    df.to_csv(
        Path(
            response_dir, 
            f'{save_name}.csv'
        )
    )
    print(f'\nExport name: {save_name}\n')
       