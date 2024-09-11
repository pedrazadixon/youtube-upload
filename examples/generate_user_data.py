from playwright.sync_api import sync_playwright
import random
import time

user_dir = "user_data\\path"

def run(playwright):
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir=user_dir,
        channel="chrome",
        headless=False,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        args=[
            '--window-size=1920,1080',
            '--disable-blink-features=AutomationControlled',
            "--no-sandbox",
            "--allow-profiles-outside-user-dir",
            f"--profile-directory=Default",
        ],

    )

    page = browser.new_page()
    page.goto('https://studio.youtube.com/')

    time.sleep(random.uniform(1, 3))

    input("Press one key to exit...")

    browser.close()


with sync_playwright() as playwright:
    run(playwright)
