#!/usr/bin/env python3
import os
from data import get_con, DATA_DIRECTORY
from provider.base_provider import BaseProvider

INPUT_DIR = os.path.join(DATA_DIRECTORY, 'input')
RESULT_DIR = os.path.join(DATA_DIRECTORY, 'result')

def setup_worker():
    print('creating ' + INPUT_DIR)
    if os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)

    print('creating ' + RESULT_DIR)
    print('creating ' + RESULT_DIR)
    if os.path.exists(RESULT_DIR):
        os.makedirs(RESULT_DIR)

def execute(providers: list[BaseProvider]):
    print("Executing duplication worker")

    for provider in providers:
        all_files = provider.list_all_files()

        
