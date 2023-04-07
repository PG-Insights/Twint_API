#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 09:45:15 2023

@author: dale
"""

import json
import subprocess
import pandas as pd
from os import chdir
from pathlib import Path


def create_query(*args):
    return ' '.join(*args)


def return_query_results(
        query: str,
        instance: str,
        save_format='csv'):
    working_dir = Path(__file__).parent
    chdir(working_dir)
    cmd = [
        'go',
        'run',
        'main.go',
        '-Query',
        query,
        '-Instance',
        instance,
        "-Format",
        save_format
    ]

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
    save_path = ''  # will save in cwd if not updated
    save_name = 'twitter_df_test.csv'  # change this name for testing
    query = [
        'from:LetMOPLay', 
        'within_time:10h',
        # add more query parameters here, order doesn't matter
    ]
    instance = 'birdsite.xanny.family'  #  Don't change, this one works lol
    json_str = return_query_results(
        create_query(query), 
        instance, 
        save_format='json'
    )
    response_json = parse_json_returned(json_str)
    
    df= pd.read_json(response_json, lines=True)
    df.to_csv(save_name)
    print(df)
    