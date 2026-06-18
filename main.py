from src.textual_ui import TextualApp


if __name__ == "__main__":
    app: TextualApp = TextualApp()
    replay: str | None = app.run()
    print(replay)