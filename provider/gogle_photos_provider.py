#!/usr/bin/env python3

import os
import shutil
import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


from base_provider import BaseProvider, FileInfo


class GooglePhotosProvider(BaseProvider):
    __CLIENT_ID : str
    __CLIENT_SECRET: str
    __SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly']
    __GOOGLE_CREDENTIALS = None
    __TOKEN_FILE = os.path.join("_data_", "token.json")
    __SERVICE = None

    def __init__(self, client_id: str, client_secret: str) -> None:
        super().__init__()
        self.__CLIENT_ID = client_id
        self.__CLIENT_SECRET = client_secret

        self.__setup()
        
    def __setup(self):
        if os.path.exists('token.json'):
            self.__GOOGLE_CREDENTIALS = Credentials.from_authorized_user_file(self.__TOKEN_FILE, self.__SCOPES)
        
        if not self.__GOOGLE_CREDENTIALS or not self.__GOOGLE_CREDENTIALS.valid:
            if self.__GOOGLE_CREDENTIALS and self.__GOOGLE_CREDENTIALS.expired and self.__GOOGLE_CREDENTIALS.refresh_token:
                self.__GOOGLE_CREDENTIALS.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.__SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Salva as credenciais para a próxima execução.
            with open(self.__TOKEN_FILE, 'w') as token:
                token.write(creds.to_json())
        
        service = build('photoslibrary', 'v1', credentials=creds, static_discovery=False)
        

    def list_all_files(self, base_dir: str) -> list[FileInfo]:
        results = []
        
        if self.__SERVICE:
            results = self.__SERVICE.mediaItems().list(pageSize=10).execute()
            items = results.get('mediaItems', [])

            if items:
                print('Could not find any media.')
            else:
                print('Fotos encontradas:')
                for item in items: # type: ignore
                    f = FileInfo(item['id'], item['filename'])
                    results.append(f)
        
        return results
	
    def download_file(self, file: FileInfo, destination_path: str):
        if self.__SERVICE is None:
            return False
        
        media_item = self.__SERVICE.mediaItems().get(mediaItemId=file.fileId).execute()
        download_url = media_item['baseUrl'] + '=d'
        filename = media_item['filename']

        print(f"Downloading photo '{filename}'...")
        response = requests.get(download_url, stream=True)
        if response.status_code == 200:
            file_path = os.path.join(destination_path, filename)                        
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

                f.flush()
                f.close()

            return True
        else:
            print(f"Error download photo: {response.status_code}")
            return False