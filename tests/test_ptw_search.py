from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def test_google_search_for_ptw():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.google.com")
        
        # クッキー同意ポップアップを処理
        try:
            page.click("button:has-text('同意する')")
        except:
            pass  # ボタンが見つからなければ無視
        
        # 検索ボックスが表示されるまで待機
        page.wait_for_selector('textarea.gLFyf')
        page.fill('textarea.gLFyf', 'PTW')
        page.press('textarea.gLFyf', 'Enter')
        page.wait_for_load_state("networkidle")
        
        # ログインプロンプトが出る可能性に対応
        try:
            page.click('button[aria-label="ログインしない"]')
        except:
            pass  # ボタンが見つからなければ無視

        # 検索結果が表示されるまで待機
        page.wait_for_selector('div.yuRUbf', timeout=10000)
        
        html = page.content()
        soup = BeautifulSoup(html, 'html.parser')
        search_results = soup.find_all('div', {'class': 'yuRUbf'})
        
        # デバッグ情報として検索結果を出力
        print("Search results:")
        for result in search_results:
            print(result.text)
        
        browser.close()
        assert any('ポールトゥウィン' in result.text for result in search_results)
