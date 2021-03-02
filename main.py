from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

PROMISED_DOWN = 5
PROMISED_UP = 2
USER_NO = "9619733345"
PASS = "uday1998"
CHROME_PATH = "C:\\Users\\dell\\Desktop\\Study\\Development\\chromedriver.exe"


class TwitterComplaint_Bot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)
        self.up = 0
        self.down = 0

    def get_Internet_Speed(self):
        self.driver.get("https://www.speedtest.net/")
        test_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        test_button.click()
        sleep(120)
        self.down = round(int(float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)))
        self.up = round(int(float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)))

    def twitter_complaint(self):
        self.driver.get("https://twitter.com/login")
        sleep(10)

        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        sleep(5)

        login.send_keys(USER_NO)
        password.send_keys(PASS)

        enter = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        enter.click()

        tweet = f"Hey Internet Provider, why is my internet speed {self.down} down/{self.up} up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up ??"
        sleep(10)
        tweet_to_send = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        sleep(10)
        tweet_to_send.send_keys(tweet)
        sleep(3)
        send_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span')
        send_tweet.click()
        self.driver.close()


x = TwitterComplaint_Bot()
x.get_Internet_Speed()
if x.up < PROMISED_UP or x.down < PROMISED_DOWN:
    x.twitter_complaint()
