#!/usr/bin/env python3
import os
import shutil
from webbrowser import get
from data import get_con, DATA_DIRECTORY
from provider.base_provider import BaseProvider
from helper.file_helper import get_file_md5

INPUT_DIR = os.path.join(DATA_DIRECTORY, 'input')

def setup_worker():
    print('creating ' + INPUT_DIR)
    if os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)

def execute_worker(providers: list[BaseProvider], destination_directory: str):
    print("Executing duplication worker")

    for provider in providers:
        print(f"Processing provider: {provider.__class__.__name__}")
        all_files = provider.list_all_files()

        for f in all_files:            
            result = provider.download_file(f, DATA_DIRECTORY)
            if result:
                print(f"Downloaded file {f.fileName} in {result}")
                md5 = get_file_md5(result)

                new_file_name = os.path.join(destination_directory, md5 + f.fileExtension.lower())
                
                if not os.path.exists(new_file_name):
                    shutil.move(result, new_file_name)
                else:
                    print(f"File {new_file_name} already exists, removing {result}")
                    os.remove(result)
                    