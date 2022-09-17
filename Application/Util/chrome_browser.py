from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

# chrome_driver_download_path: https://chromedriver.chromium.org/downloads
chrome_driver_path = r'../../chromedriver.exe'
extension_path = r'../../extension_10_8_1_0.crx'
def get_driver():
    service = Service(chrome_driver_path)

    chrome_options = Options()
    chrome_options.add_argument('http://50.206.25.106:80')
    chrome_options.add_extension(extension_path)

    driver = webdriver.Chrome(service=service, chrome_options=chrome_options)

    return driver