#!/usr/bin/env python3
import os
import shutil

from provider.base_provider import BaseProvider, FileInfo

class FileSystemProvider(BaseProvider):
    __BASE_DIRECTORY = ""

    def __init__(self, base_directory: str):
        super().__init__()
        self.__BASE_DIRECTORY = base_directory


    def list_all_files(self) -> list[FileInfo]:
        files = []

        for root, _, filenames in os.walk(self.__BASE_DIRECTORY):
            for filename in filenames:
                full_file_path = os.path.join(root, filename)
                if os.path.isfile(full_file_path):
                    file = os.path.basename(full_file_path)
                    extensao = os.path.splitext(file)[-1]
                    files.append(FileInfo(file, file, full_file_path, extensao))

        return files

    def download_file(self, file: FileInfo, destination_dir: str) -> str:
        destination_path = os.path.join(destination_dir, file.fileName)

        if os.path.exists(file.fullPath):
            shutil.copy(file.fullPath, destination_path)
            return destination_path
        else:
            return None