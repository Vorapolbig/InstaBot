from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from time import sleep
from secrets import password

class InstaBot:
    def __init__(self,username,pw):
        self.username = username
        self.browser = webdriver.Chrome(r"C:\Users\vorapolbig\Downloads\chromedriver.exe")
        self.browser.get('https://www.instagram.com')
        sleep(2)
        self.browser.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(2)
        self.browser.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.browser.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.browser.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
# InstaBot('botpacker','password')

class InstaBotMobile:

    def __init__(self,username,pw):
        self.mobile_emulation = { "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("mobileEmulation", self.mobile_emulation)
        self.browser = webdriver.Chrome(r"C:\Users\vorapolbig\Downloads\chromedriver.exe",chrome_options = self.chrome_options)
        self.browser.get('https://www.instagram.com')
        sleep(2)
        self.browser.find_element_by_xpath("//button[contains(text(), 'Log In')]").click()
        sleep(2)
        self.browser.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.browser.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.browser.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        self.browser.find_element_by_xpath("//button[contains(text(), 'Cancel')]").click()
        sleep(2)
    
    def upload_photo(self):
        self.browser.find_element_by_xpath('/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]/svg/path[1]').click()
        # self.browser.find_elements_by_css_selector("#react-root > section > nav.NXc7H.f11OC > div > div > div.KGiwt > div > div > div.q02Nz._0TPg > svg").click()


myBot = InstaBotMobile('botpacker','password')
# myBot.upload_photo()