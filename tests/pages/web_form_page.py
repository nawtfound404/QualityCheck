
from playwright.sync_api import Page, expect


class WebFormPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.selenium.dev/selenium/web/web-form.html"

        self.text_input = page.get_by_label("Text input")
        self.password_input = page.get_by_label("Password")
        self.textarea = page.get_by_label("Textarea")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.message = page.locator("#message")

    def open(self):
        self.page.goto(self.url, wait_until="domcontentloaded")

    def fill_form(self, username: str, password: str, message: str):
        self.text_input.fill(username)
        self.password_input.fill(password)
        self.textarea.fill(message)

    def submit(self):
        self.submit_button.click()

    def expect_success_message(self):
        expect(self.message).to_have_text("Received!")
