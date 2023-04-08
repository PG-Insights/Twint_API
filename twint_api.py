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
        query: str,
        instance: str):
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
    ]  # If Instance needs to be modified use a value from https://github.com/zedeus/nitter/wiki/Instances

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
        nargs='+', 
        help='Twitter query string: https://github.com/igorbrigadir/twitter-advanced-search'
    )
    args = parser.parse_args()
    query_str = create_query(
        args.query
    )
    json_str = return_query_results(
        query_str, 
        args.instance, 
        args.save_format
    )
    response_json = parse_json_returned(
        json_str
    )
    df = pd.read_json(
        response_json, 
        lines=True
    )
    save_name = f'{datetime.now()}_{args.instance.replace(".", "_")}.csv'
    df.to_csv(
        Path(
            TWINT_API_DIR, 
            save_name
        )
    )
    for col in df.columns:
        print(df[col])
        print()
   