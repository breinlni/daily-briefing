
# * --- Browser Manager ---


from selenium import webdriver


def open_chrome(headless, chrome_driver_path, target_url):
    chrome_options = webdriver.chrome.options.Options()
    if headless:
        chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)
    return driver.get(target_url)