from unittest.mock import patch
import pytest

from src.config_manager.config_manager import ConfigManager

VALID_ENV: dict[str, str] = {
    "OLLAMA_MODEL": "llama3.2",
    "OLLAMA_URL": "http://localhost:11434",
    "OCR_LANGUAGE": "swe+eng",
    "WATCH_FOLDER": "receipts/",
    "OUTPUT_FOLDER": "output/",
    "OUTPUT_FILENAME": "receipts",
    "REVIEW_MODE": "true",
}

PATCH_TARGET = "src.config_manager.config_manager.os.getenv"


def make_getenv(env: dict[str, str]):
    def getenv(key: str, *_: str) -> str | None:
        return env.get(key)
    return getenv


def make_config(overrides: dict[str, str] = {}) -> ConfigManager:
    env: dict[str, str] = {**VALID_ENV, **overrides}
    with patch(PATCH_TARGET, side_effect=make_getenv(env)):
        return ConfigManager()


class TestConfigManager:
    # ── String values ────────────────────────────────────
    def test_ollama_model(self) -> None:
        assert make_config().get_ollama_model() == "llama3.2"

    def test_ollama_url(self) -> None:
        assert make_config().get_ollama_url() == "http://localhost:11434"

    def test_ocr_language(self) -> None:
        assert make_config().get_ocr_language() == "swe+eng"

    def test_watch_folder(self) -> None:
        assert make_config().get_watch_folder() == "receipts/"

    def test_output_folder(self) -> None:
        assert make_config().get_output_folder() == "output/"

    def test_output_filename(self) -> None:
        assert make_config().get_output_filename() == "receipts"

    # ── Review mode (bool) ───────────────────────────────
    def test_review_mode_true(self) -> None:
        assert make_config({"REVIEW_MODE": "true"}).get_review_mode() is True

    def test_review_mode_false(self) -> None:
        assert make_config({"REVIEW_MODE": "false"}).get_review_mode() is False

    def test_review_mode_case_insensitive(self) -> None:
        assert make_config({"REVIEW_MODE": "True"}).get_review_mode() is True
        assert make_config({"REVIEW_MODE": "TRUE"}).get_review_mode() is True
        assert make_config({"REVIEW_MODE": "False"}).get_review_mode() is False

    # ── Missing variables ────────────────────────────────
    @pytest.mark.parametrize("missing_key", VALID_ENV.keys())
    def test_raises_when_missing(self, missing_key: str) -> None:
        env: dict[str, str] = {k: v for k, v in VALID_ENV.items() if k != missing_key}
        with patch(PATCH_TARGET, side_effect=make_getenv(env)):
            with pytest.raises(ValueError, match=f"{missing_key} is required"):
                ConfigManager()