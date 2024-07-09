from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pytest

def test_google_search_for_ptw():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.google.com")
        page.wait_for_selector('textarea.gLFyf')
        page.fill('textarea.gLFyf', 'PTW')
        page.press('textarea.gLFyf', 'Enter')
        page.wait_for_load_state("networkidle")
        html = page.content()
        soup = BeautifulSoup(html, 'html.parser')
        search_results = soup.find_all('div', {'class': 'yuRUbf'})
        browser.close()
        assert any('ポールトゥウィン' in result.text for result in search_results)

# Run the test
pytest.main(["-v", "-s", __file__])
