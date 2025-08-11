#!/usr/bin/env python3
import os
import shutil
from webbrowser import get
from data import get_con, DATA_DIRECTORY
from provider.base_provider import BaseProvider
from helper.file_helper import get_file_md5

INPUT_DIR = os.path.join(DATA_DIRECTORY, 'input')
RESULT_DIR = os.path.join(DATA_DIRECTORY, 'result')

def setup_worker():
    print('creating ' + INPUT_DIR)
    if os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)

    print('creating ' + RESULT_DIR)
    if os.path.exists(RESULT_DIR):
        os.makedirs(RESULT_DIR)

def execute(providers: list[BaseProvider]):
    print("Executing duplication worker")

    for provider in providers:
        print(f"Processing provider: {provider.__class__.__name__}")
        all_files = provider.list_all_files()

        for f in all_files:
            destination_file_name = os.path.join(INPUT_DIR, f.id)
            result = provider.download_file(f, INPUT_DIR)
            if result:
                print(f"Downloaded file {f.fileName} in {result}")
                md5 = get_file_md5(result)

                new_file_name = os.path.join(RESULT_DIR, md5 + f.extensao.lower())
                
                if not os.path.exists(new_file_name):
                    shutil.move(result, new_file_name)
                else:
                    print(f"File {new_file_name} already exists, removing {result}")
                    os.remove(result)
                    