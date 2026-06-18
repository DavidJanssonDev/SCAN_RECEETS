from textual.app import App, ComposeResult
from textual.widgets import Label, Button, Header

class TextualApp(App[str]):
    CSS_PATH="tcss/textual_app.tcss"
    TITLE="Expense Application"
    SUB_TITLE="A app where you track ur expenses"
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Do you love Textual?", id="question")
        yield Button("Yes",id="yes", variant="primary")
        yield Button("No",id="no", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)