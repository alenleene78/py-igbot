from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()

class igbot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get ("https://www.instagram.com/")
        time.sleep(5)
        login_button = driver.find_element_by_xpath ("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(5)
        #  Логинимся в аккаунт ( Важно чтобы он был без двухфакторной этой хуйни)
        username_elem = driver.find_element_by_xpath("//input[@name='username']")
        username_elem.clear()
        username_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

        def like_photo(self, hashtag):
            driver = self.driver
            driver.get ("https://www.instagram.com/explore/tags/" + hashtag + "/")
            time.sleep(5)

            # Сбор фотографий
            pic_hrefs = []
            for i in range (1, 7):
                try:
                    driver.execute_script ("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(5)
                    # Берем тэги
                    hrefs_in_view = driver.find_elements_by_tag_name('a')

                    hrefs_in_view = [elem.get_attribute ('href') for elem in hrefs_in_view if
                                     hashtag in elem.get_attribute ('href')]
                    # Делаем лист не повторящиихся фотографий
                    [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                except Exception:
                    continue

            # Лайк фотографий
            unique_photos = len(pic_hrefs)
            for pic_href in pic_hrefs:
                driver.get (pic_href)
                time.sleep(5)
                driver.execute_script ("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep (random.randint(3, 5))
                like_button = lambda: driver.find_element_by_xpath ('/html/body/span/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line ("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                     + " | Sleeping" + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1


username = "USERNAME"
password = "PASSWORD"

ig = igbot(username, password)
ig.login()

hashtags = [] # Хэштеги писать по типу ['hello', 'world']

while true:
    try:
        tag = random.choice(hashtags) #Выбирает рандомный тег среди всех
        ig.like_photo(tag)
    except Exception:
        ig.closeBrowser()
        time.sleep(60)
        ig = igbot (username, password)
        ig.login()