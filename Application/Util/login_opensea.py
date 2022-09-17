from time import sleep

from waiting_element import waiting_element_displayed


def login_opensea(driver, COLLECTION_CREATE_PATH):
    # open opensea
    driver.switch_to.window(driver.window_handles[1])
    driver.get(COLLECTION_CREATE_PATH)
    sleep(10)

    # login opensea
    waiting_element_displayed(driver, "//span [text()='MetaMask']")[0].click()
    print(driver.title)

    sleep(3)
    driver.switch_to.window(driver.window_handles[2])
    waiting_element_displayed(driver, "//button [text()='下一頁']")[0].click()
    waiting_element_displayed(driver, "//button [text()='連線']")[0].click()

    sleep(5)
    driver.switch_to.window(driver.window_handles[2])
    waiting_element_displayed(driver, "//button [text()='簽署']")[0].click()
    driver.switch_to.window(driver.window_handles[1])
