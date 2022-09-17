# 475 * 625

# //button[@id="duration"] # 存活日期
# //input[@name="price"] # 價錢
# //div[@class="Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX"] # 6 months
# //button[@type="submit"] # 提交


# //div[@class='signature-request-message--root']

# //button[text()='簽署']

# //span[text()='Share your listing']


# 搜索網址
# https://opensea.io/collection/school-little-dinosaur?search[query]=
# School%20Littel%20Dinosaur%20%233 # 範例 School Littel Dinosaur #3
# &search[sortAscending]=true&search[sortBy]=CREATED_DATE

# 項目
# //a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq Asset--anchor']

# Sell button
# //a[text()='Sell']


from time import sleep
from selenium.webdriver.common.by import By
import os
from pathlib import Path

import applicationContext
from Application.Util import chrome_browser, metamask_connector
from Application.Util import login_opensea
import waiting_element

SECRET_RECOVERY_PHRASE = applicationContext.SECRET_RECOVERY_PHRASE
NEW_PASSWORD = applicationContext.NEW_PASSWORD
COLLECTION_CREATE_PATH = applicationContext.COLLECTION_CREATE_PATH
IMAGES_NAME = applicationContext.IMAGES_NAME
IMAGES_DESCRIPTION = applicationContext.IMAGES_DESCRIPTION

IMAGES_DIR_PATH = r"Sell_images"

# 賣價 ETH
SELL_PRICE = '0.1'

# 搜索網址
first_url = 'https://opensea.io/collection/school-little-dinosaur?search[query]='
last_url = '&search[sortAscending]=true&search[sortBy]=CREATED_DATE'

driver = chrome_browser.get_driver()

def find_item(item_number):
    image_name = item_number + '.png'
    item_name = IMAGES_NAME + item_number

    driver.get(first_url + item_number + last_url)
    driver.execute_script('document.documentElement.scrollTop=810')
    sleep(1.5)

    # https: // opensea.io / collection / school - little - dinosaur?search[query] = School % 20L
    # ittle % 20
    # Dinosaur % 20  # 132&search[sortAscending]=true&search[sortBy]=CREATED_DATE

    if (driver.title == 'opensea.io | 504: Gateway time-out'):
        print(driver.title)
        find_item(item_number)
        return
    try:
        item_list = driver.find_elements(By.XPATH, '//div[text()="' + item_name + '"]')
        item_len = len(item_list)
        if (item_len == 0):
            print(item_name + ", 數量: " + str(item_len))
            sleep(5000);
            return
        else:
            # item = driver.find_element(By.XPATH, "//a[@class='styles__StyledLink-sc-l6elh8-0 ekTmzq Asset--anchor']")
            # item.click()
            item_list[0].click()
            sell_button = waiting_element(driver, "//a[text()='Sell']")[0]
            sell_button.click()
            item_sell(image_name)
    except:
        print('out ' + image_name + ': ' + str(item_len) + '............')
        print(driver.title + '\n')

    return

def item_sell(image_name):
    try:
        sleep(2)
        input_price = driver.find_element(By.XPATH, '//input[@name="price"]')
        input_price.send_keys(SELL_PRICE);

        # driver.execute_script('document.documentElement.scrollTop=1000')
        button_submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        button_submit.click();

        sleep(20)

        driver.switch_to.window(driver.window_handles[2])

        driver.find_element(By.XPATH, "//div[@class='signature-request-message--root']").click();
        driver.execute_script('document.documentElement.scrollTop=3000')
        driver.find_element(By.XPATH, "//button[text()='簽署']").click()

        # sleep(8)

        driver.switch_to.window(driver.window_handles[1])
        waiting_element(driver, "//span[text()='Share your listing']")
        Path(IMAGES_DIR_PATH + '/Waiting_Sell/' + image_name).rename(IMAGES_DIR_PATH + '/Sell_Finish/' + image_name)
    except:
        print('item_sell_except ' + image_name)

    return


if __name__ == '__main__':
    width = 546 * 2
    height = 735
    driver.set_window_size(width=width, height=height)
    metamask_connector.meta_mask_navigate(driver, SECRET_RECOVERY_PHRASE, NEW_PASSWORD)
    login_opensea(driver, COLLECTION_CREATE_PATH)

    width = 475
    height = 625
    driver.set_window_size(width=width, height=height)

    # sort image list
    sorted_image_list = []
    for image in os.listdir(IMAGES_DIR_PATH + '/Waiting_Sell'):
        count = 0
        if (image.endswith(".png")):
            sorted_image_list.append(int(image.replace(".png", "")))
            count += 1
    sorted_image_list.sort()
    print(sorted_image_list);
    # result_array = [0]*len(sorted_image_list)
    for i in range (len(sorted_image_list)):
            item_number = str(sorted_image_list[i])
            find_item(item_number)

    driver.get(COLLECTION_CREATE_PATH.replace('/assets/create', ''))
    driver.quit()

