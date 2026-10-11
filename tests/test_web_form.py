
from playwright.sync_api import Page

from tests.pages.web_form_page import WebFormPage


def test_form_submission_success(page: Page):
    form = WebFormPage(page)

    form.open()
    form.fill_form(
        username="Ayush",
        password="TestPassword123",
        message="QualityCheck test",
    )
    form.submit()

    form.expect_success_message()


def test_empty_text_input_submission(page: Page):
    form = WebFormPage(page)

    form.open()
    form.submit()

    form.expect_success_message()
