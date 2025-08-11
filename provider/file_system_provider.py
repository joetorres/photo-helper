#!/usr/bin/env python3
import os
import shutil

from base_provider import BaseProvider, FileInfo


class FileSystemProvide(BaseProvider):
    def list_all_files(self, base_dir: str) -> list[FileInfo]:
        files = []

        for root, _, filenames in os.walk(base_dir):
            for filename in filenames:
                full_file_name = os.path.join(root, filename)
                if os.path.isfile(full_file_name):
                    files.append(FileInfo(full_file_name, full_file_name))

        return files

    def download_file(self, file: FileInfo, destination_path: str) -> bool:
        if os.path.exists(file.fileName):
            shutil.copy(file.fileName, destination_path)
            return True
