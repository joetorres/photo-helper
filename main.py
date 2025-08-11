#!/usr/bin/env python3

from data import start_db
from worker.remove_duplicates_worker import setup_worker

def main():
    print("Starting script. Check if DB exists...")
    start_db()

    print("setup duplicates worker...")
    setup_worker()

if __name__ == '__main__':
    main()