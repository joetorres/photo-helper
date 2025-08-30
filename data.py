#!/usr/bin/env python3

import sqlite3
import os

DATA_DIRECTORY = '.\\_data_';

def get_con():
    path_db = os.path.join('.', DATA_DIRECTORY, 'photos.db')    
    conn = sqlite3.connect(path_db)
    return conn

def start_db():
    if not os.path.exists(DATA_DIRECTORY):
        os.makedirs(DATA_DIRECTORY)

    conn = get_con()
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS media (fileHash TEXT PRIMARY KEY, originalFilePath TEXT, provider INTEGER );")
    conn.commit()
