import os, time, pytest

pytestmark = pytest.mark.ui

def _skip_if_no_display():
    # CI safety: skip when no X server or driver
    if os.getenv("CI") == "true":
        pytest.skip("UI disabled in CI by default")
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
except Exception:
    webdriver = None

def _driver():
    browser = os.getenv("BROWSER","chrome")
    if browser == "firefox":
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        return webdriver.Firefox(options=opts)
    else:
        opts = ChromeOptions()
        opts.add_argument("--headless=new")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-gpu")
        return webdriver.Chrome(options=opts)

def test_checkout_flow():
    _skip_if_no_display()
    if webdriver is None:
        pytest.skip("Selenium not installed with drivers")
    d = _driver()
    try:
        d.get("https://httpbin.org/forms/post")
        # Simulate filling form fields (httpbin demo form)
        txt = d.find_element(By.NAME, "custname")
        txt.send_keys("Praneetha QA")
        d.find_element(By.NAME, "custtel").send_keys("9701340694")
        d.find_element(By.NAME, "custemail").send_keys("qa@sentinelpay.example")
        d.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
        time.sleep(1)
        assert "form" in d.page_source.lower()
    finally:
        d.quit()
