from abc import ABC, abstractmethod

class FileInfo:
    def __init__(self, fileId: str, fileName: str, fullPath: str, fileExtension: str = None):
        self.fileName = fileName
        self.fileId = fileId
        self.fullPath = fullPath
        self.fileExtension = fileExtension if fileExtension else ""

    fileName: str
    fullPath: str
    fileId: str
    fileExtension: str

class BaseProvider(ABC):
    @abstractmethod
    def list_all_files(self) -> list[FileInfo]:
        pass

    @abstractmethod
    def download_file(self, file: FileInfo, destination_dir: str) -> str:
        pass
    