from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def test_google_search_for_ptw():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.google.com")
        page.wait_for_selector('textarea.gLFyf')
        page.fill('textarea.gLFyf', 'PTW')
        page.press('textarea.gLFyf', 'Enter')
        page.wait_for_load_state("networkidle")
        
        # 追加: 検索結果が読み込まれるまでの待機時間を追加
        page.wait_for_timeout(5000)
        
        html = page.content()
        soup = BeautifulSoup(html, 'html.parser')
        search_results = soup.find_all('div', {'class': 'yuRUbf'})
        
        # 追加: デバッグ情報として検索結果を出力
        print("Search results:")
        for result in search_results:
            print(result.text)
        
        browser.close()
        assert any('ポールトゥウィン' in result.text for result in search_results)
