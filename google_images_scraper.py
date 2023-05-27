from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import re
import requests


#This solution works for 20 images, also it downloads the thumbnails, not the original image

query = "street fashion bag"  # Replace with your desired search query
num_images = 500  # Replace with the number of images you want to download. choose a number between 50 and 500

# Set up Safari driver
driver = webdriver.Firefox()



def scrape_google_images(query, num_images):
    # Open Google Images
    driver.get("https://www.google.com/imghp")

    driver.maximize_window()

    # Find the search bar element and enter the search query
    search_bar = driver.find_element("name", "q")
    search_bar.send_keys(query)
    search_bar.send_keys(Keys.RETURN)

    num_scrolls = num_images // 50
    for i in range(num_scrolls):
        if i == 6:
                load_more = driver.find_element(By.XPATH, '/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/input')
                load_more.click()
                time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    driver.execute_script("window.scrollTo(0, 0);")

    thumbnails = []
    k=1
    j=1
    for i in range(num_images):
            
            if i < 50:
                n = i+1
                try:
                    thumbnails.append(driver.find_element(By.XPATH, f'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{n}]/a[1]/div[1]/img'))
                except Exception as e:
                    pass
                 
            if i >= 50:
                n = 50 + k
                try:
                    thumbnails.append(driver.find_element(By.XPATH, f'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{n}]/div[{j}]/a[1]/div[1]/img'))
                    j = j+1
                except Exception as e:
                    try:
                        j = j+1
                        driver.find_element(By.XPATH, f'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{n}]/div[{j}]/a[1]/div[1]/img')
                    except Exception as d:
                        j = 1
                        k = k + 1





    urls = []

    for thumbnail in thumbnails:
        #print(thumbnail.get_attribute('alt'))
        thumbnail.click()
        time.sleep(1)
        try:
            image_url = driver.find_element(By.XPATH, '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]').get_attribute('src')
            urls.append(image_url)
        except Exception as e:
             pass
    driver.quit()

    print(len(urls))
    # Create a directory to save the images
    os.makedirs(query, exist_ok=True)

    for url in urls:
        print(url)
        try:
            file_name = url[-16:]
            file_name = re.sub(r'\W+', '', file_name)
            file_path = os.path.join(query, file_name)
            response = requests.get(url, timeout=5)
            with open(file_path, "wb") as file:
                file.write(response.content)
                print('good')
        except Exception as e:
            print('bad')

scrape_google_images(query, num_images)