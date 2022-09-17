import os
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path
import random

import applicationContext
from Application.Util.login_opensea import login_opensea
from Application.Util import chrome_browser, metamask_connector
from waiting_element import waiting_element_displayed

SECRET_RECOVERY_PHRASE = applicationContext.SECRET_RECOVERY_PHRASE
NEW_PASSWORD = applicationContext.NEW_PASSWORD
COLLECTION_CREATE_PATH = applicationContext.COLLECTION_CREATE_PATH
IMAGES_NAME = applicationContext.IMAGES_NAME
IMAGES_DESCRIPTION = applicationContext.IMAGES_DESCRIPTION

IMAGES_DIR_PATH = r"Upload_images"

# chrome driver
driver = chrome_browser.get_driver()
def opensea_upload():
    # 創建 紀錄dir
    if not os.path.exists(IMAGES_DIR_PATH + '/Uploaded'):
        os.mkdir(IMAGES_DIR_PATH + '/Uploaded')

    # sort image list
    sorted_image_list = []
    for image in os.listdir(IMAGES_DIR_PATH + '/Wait'):
        count = 0
        if (image.endswith(".png")):
            sorted_image_list.append(int(image.replace(".png", "")))
            count += 1
    sorted_image_list.sort()
    sorted_image_list = [str(item) + '.png' for item in sorted_image_list]

    # 開始上傳
    for image in sorted_image_list:

        # start
        upload_item(image)
        # sleep(5)

        # # check_create_end
        # for i in range(10):
        #     try:
        #         element = driver.find_element(By.XPATH, '//h1[text()="Oops, something went wrong"]')
        #         if element.is_displayed():
        #             upload_item(image)
        #             sleep(5)
        #             break
        #     except:
        #         pass
        #     sleep(1)

        # [500] err
        while True:
            try:
                element_seare = driver.find_element(By.XPATH, '//p [text()="SHARE"]')
                if (element_seare.is_displayed()):
                    break
            except:
                # print(driver.title)
                try:
                    if (driver.title == 'Create NFTs | OpenSea'):
                        element_create = driver.find_element(By.XPATH, '//button [text()="Create"]').click()
                        # try:
                        #     title = driver.find_element(By.XPATH, '//h4[text()="Almost done"]')
                        #     element = driver.find_element(By.XPATH, '//div[@class="recaptcha-checkbox-borderAnimation"]')
                        #     print(title.text, element)
                        #     if (title.is_displayed()):
                        #         element.click()
                        # except:
                        #     element_create = driver.find_element(By.XPATH, '//button [text()="Create"]').click()
                    # Oops err
                    elif (driver.title == 'Something Went Wrong | OpenSea'):
                        upload_item(image)
                    else:
                        print(driver.title)
                except:
                    pass
                pass
            sleep(5)

        # 紀錄
        print(image)
        Path(IMAGES_DIR_PATH + '/Wait/' + image).rename(IMAGES_DIR_PATH + '/Uploaded/' + image)

# //h1[text()="Oops, something went wrong"]
# Something Went Wrong | OpenSea
def upload_item(image):
    # 打開 create item 頁面
    # err 'opensea.io | 504: Gateway time-out'
    while (driver.title != 'Create NFTs | OpenSea'):
        # print(driver.title)
        driver.get(COLLECTION_CREATE_PATH)
        sleep(10)

    # import image
    inputs = waiting_element_displayed(driver, '//input')
    # print(driver.title)
    # MetaMask out
    # sleep(3)
    if driver.title == 'Login | OpenSea':
        print(driver.title + "2")
        waiting_element_displayed(driver, "//span [text()='MetaMask']")[0].click()
        sleep(3)
        upload_item(image)
        return
    # image
    # sleep(5)
    inputs[1].send_keys(IMAGES_DIR_PATH + '/Wait/' + image)
    # image name
    # sleep(5)
    inputs[2].send_keys(IMAGES_NAME + image.replace(".png", ""))

    # image descript
    # create item
    sleep(random.randint(5,5))

# recaptcha-checkbox-border
if __name__ == '__main__':
    width = 546*2
    height = 735
    driver.set_window_size(width=width, height=height)

    metamask_connector.meta_mask_navigate(driver, SECRET_RECOVERY_PHRASE, NEW_PASSWORD)

    login_opensea(driver, COLLECTION_CREATE_PATH)

    sleep(5)
    opensea_upload()

    driver.get(COLLECTION_CREATE_PATH.replace('/assets/create', ''))
    driver.quit()

