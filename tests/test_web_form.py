
import pytest
from playwright.sync_api import Page, expect
from tests.pages.web_form_page import WebFormPage


@pytest.mark.parametrize(
    "username",
    ["Ayush", "QA Tester", "QualityCheck"],
)
def test_form_submission_with_different_inputs(
    page: Page,
    username: str,
):
    form = WebFormPage(page)

    form.open()
    form.text_input.fill(username)
    form.submit()

    form.expect_success_message()





def test_text_input_accepts_and_retains_value(page: Page):
    form = WebFormPage(page)
    form.open()

    form.text_input.fill("QualityCheck")
    expect(form.text_input).to_have_value("QualityCheck")

    form.submit()
    form.expect_success_message()
