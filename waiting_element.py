from time import sleep
from selenium.webdriver.common.by import By


def waiting_element_displayed(driver, xpath_language):
    while True:
        try:
            elements = driver.find_elements(By.XPATH, xpath_language)
            if elements[0].is_displayed():
                return elements
        except:
            pass
        sleep(1)
