from dotenv import load_dotenv
import os

class ConfigManager:
    def __init__(self):
        load_dotenv()

        self.ollama_model: str = self._get_env_str("OLLAMA_MODEL")
        self.ollama_url: str = self._get_env_str("OLLAMA_URL")
        self.ocr_language: str = self._get_env_str("OCR_LANGUAGE")
        self.watch_folder: str = self._get_env_str("WATCH_FOLDER")
        self.output_folder: str = self._get_env_str("OUTPUT_FOLDER")
        self.output_filename: str = self._get_env_str("OUTPUT_FILENAME")
        self.review_mode: bool = self._get_env_bool("REVIEW_MODE")

    def _get_env_str(self, name: str) -> str:
        value = os.getenv(name)
        if value is None:
            raise ValueError(f"{name} is required but not set in the .env file")
        return value
 
    def _get_env_bool(self, name: str) -> bool:
        value = os.getenv(name)
        if value is None:
            raise ValueError(f"{name} is required but not set in the .env file")
        return value.lower() == "true"

    # ========================
    # GETTERS
    # ========================

    def get_ollama_model(self) -> str:
        return self.ollama_model
 
    def get_ollama_url(self) -> str:
        return self.ollama_url
 
    def get_ocr_language(self) -> str:
        return self.ocr_language
 
    def get_watch_folder(self) -> str:
        return self.watch_folder
 
    def get_output_folder(self) -> str:
        return self.output_folder
 
    def get_output_filename(self) -> str:
        return self.output_filename
 
    def get_review_mode(self) -> bool:
        return self.review_mode