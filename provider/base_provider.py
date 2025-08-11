from abc import ABC, abstractmethod

class FileInfo:
    def __init__(self, fileName: str, fileId: str):
        self.fileName = fileName
        self.fileId = fileId

    fileName: str
    fileId: str

class BaseProvider(ABC):
    @abstractmethod
    def list_all_files(self, base_dir: str) -> list[FileInfo]:
        pass

    @abstractmethod
    def download_file(self, file: FileInfo, destination_path: str) -> bool:
        pass
    