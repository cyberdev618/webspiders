

from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
 '''
IMPORTANT: FACEBOOK doesnt allow this type of crawling and would prefer you use their official API. use at your own risk. 
BE GENTLE ON SERVERS AND DONT REQUEST IN HIGH VELOCITY!
 '''
 
LOGIN_URL = 'https://www.facebook.com/login.php'
 
class FacebookLogin():
    def __init__(self, email, password, browser='Chrome'):
        # Store credentials for login
        self.email = email
        self.password = password
        self.browser = browser
        self.driver_install(browser)
        
       
    def driver_install(self,browser):
        if browser == 'Chrome':
            # Use chrome
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        elif browser == 'Firefox':
            # Set it to Firefox
            self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

#   request URL
        self.driver.get(LOGIN_URL)
        time.sleep(1) # Wait for some time to load

 #login function
    def login(self):
        email_element = self.driver.find_element_by_id('email')
        email_element.send_keys(self.email) # Give keyboard input
 
        password_element = self.driver.find_element_by_id('pass')
        password_element.send_keys(self.password) # Give password as input too
 
        #buttonClick(self)
        login_button = self.driver.find_element_by_id("loginbutton")
        login_button.click()
        time.sleep(2)

class pageInfo(webdriver.Firefox):
    def __init__(self, elementObj, name, payload ):
        self.e = elementObj
        self.n = name
        self.p = payload


    def SeCommand(self):
        element = driver.find_element_by_id(idname)
        element.send.keys(self.payload)
        ans = input("should we hit the button?\t:(Y or N)")
        
        
        if elementObj == 'ID':
            driver.find_element_by_id(name)

        elif elementObj == 'CLASS':
            driver.find_element_by_class_name(name).click()
        elif elementObj == 'TEXT':
            driver.find_element_by_xpath("// a[contains(text(),\
'What's on your mind, Neito?')]").click() #

        if ans == Y:
            login_button = self.driver.find_element_by_id(idname)
            login_button.click()
            time.sleep(2)
        elif ans == N:
            print("Continuing")

        else:
            print("Defaulting & continuing")

        
 
if __name__ == '__main__':

    # Enter your login credentials here
#[SECURITY CONCERN] # edit the email and passwd variables
    email = "user.email"
    passwd = "user.pass"

#change this to check against encrypted list or DB
    fb_login = FacebookLogin(email=email, password=passwd, browser='Firefox')

fb_login.login()

while True:
    elementObj = input("how should we access th element Object? \n\t:\tID\n\t:\tClass\n\t:\ttext")
    payload = input("Enter Payload for delivery \n\t:")
    name = input("Enter the name of the Object alias")
    cmd =  pageInfo(elementObj, name, payload) # initialize vars!
    cmd.SeCommand()

