#!/usr/bin/env python3

from data import start_db
from provider.file_system_provider import FileSystemProvider
from worker.remove_duplicates_worker import execute_worker
from provider.gogle_photos_provider import GooglePhotosProvider

def main():
    print("Starting script. Check if DB exists...")
    start_db()

    print("setup duplicates worker...")
    
    providers = [
            FileSystemProvider(base_directory="C:\\tools\\photo-helper\\origin"),
            # GooglePhotosProvider()
        ]

    print("Starting worker...")
    execute_worker(providers, "C:\\tools\\photo-helper\\destination")   
    



if __name__ == '__main__':
    main()