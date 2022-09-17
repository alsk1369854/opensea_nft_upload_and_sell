# OpenSea NFT upload and sell

## 基本配置
### 配置 /applicationContext.py
```buildoutcfg
# MateMask 秘密恢復短語
SECRET_RECOVERY_PHRASE = 'YOUR SECRET_RECOVERY_PHRASE'
# MateMask 密碼
NEW_PASSWORD = YOUR NEW_PASSWORD'

# OpenSec Create New Item URL
# COLLECTION_CREATE_PATH = 'https://opensea.io/collection/<Your-Collection-Name>/assets/create'
COLLECTION_CREATE_PATH = 'https://opensea.io/collection/school-little-dinosaur/assets/create'

# Create Item Title
IMAGES_NAME = 'School Little Dinosaur #'
# Create Item Description
IMAGES_DESCRIPTION = ''
```
<br/>

### 檢查 Chromedriver 版本與本機 Chrome版本 是否匹配
#### 查看本機的 Chrome 版本
```buildoutcfg
# Chrome > 設定 > 關於 Chrome
版本 105.0.5195.127 (正式版本) (64 位元)
```
<br/>

#### 下載 [ChromeDriver](https://chromedriver.chromium.org/downloads)
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
```buildoutcfg
# 包內預設帶有105版本若你的 Chrome 是其他版本就需要另外安裝
下載自己 Chrome 對應的版本，取代根目錄底下的 '/chromedriver.exe'
```
<br/>

## 使用
### 上傳 /Application/Upload_Item
```buildoutcfg
# 斷線了會自動記錄，下次開啟直接執行 Main.py 即可繼續執行上傳
# 上傳完成的圖片會轉至 /Upload_image/Uploaded 文件夾
Step1: 將要上傳的.png圖片放入 /Upload_image/Wait 文件夾中
Step2: 執行 Main.py 
```
<br/>

### 販售 /Application/Sell_Item
#### !!!要販售的圖片必須已完成上傳!!!
```buildoutcfg
# 斷線了會自動記錄，下次開啟直接執行 Main.py 即可繼續執行販售
# 販售完成的圖片會轉至 /Sell_images/Sell_Finish 文件夾
Step1: 將要販售的.png圖片放入 /Sell_images/Waiting_Sell 文件夾中，
Step2: 執行 Main.py 
```