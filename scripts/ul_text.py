import time
import os
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from bs4 import BeautifulSoup

# The start of the api folder you want to iterated
START_FOLDER_NUM = 3
# The number of categorized folders in the left panel
END_FOLDER_NUM = 83
#TODO: can be later changed into pass in using flags
# Login email
# TODO: change the username
USERNAME = 'admin@admin.com'
# Login password
# TODO: change the password
PASSWORD = 'ymfe.org'
# PREFIX = './texts/'

def copy_text_from_txt_file(file_path):
    with open(file_path, 'r') as file:
        text_content = file.read()
        pyperclip.copy(text_content)

# Custom expected condition to wait for the element to become active
class ElementActive:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        return "ant-tabs-tabpane-active" in element.get_attribute("class")

# Set up the WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate WebDriver for your browser
website = "http://192.168.5.200:8700/"

# Navigate to the website
driver.get(website)  # Replace with the actual website URL

# Wait for the new section after every action
wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds

# Click the initial button to open the login page
initial_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yapi"]/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/a/button')))
initial_button.click()

# Wait for the login page to load and locate the email and password fields
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
# Input the email and password
email_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)

# Submit the login form
login_button = driver.find_element(By.XPATH, '//*[@id="yapi"]/div/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[1]/form/div[3]/div/div/span/button')
login_button.click()

# Wait for the workspace to load and navigate to it
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="yapi"]/div/div[1]/div[2]/div/div/div/div[1]/div/div[2]/div/ul/li[2]')))
wkspace_btn = driver.find_element(By.XPATH, '//*[@id="yapi"]/div/div[1]/div[2]/div/div/div/div[1]/div/div[2]/div/ul/li[2]')
wkspace_btn.click()

# Open the project folder
# Project folder is gymera
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="yapi"]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/i')))
project_btn = driver.find_element(By.XPATH, '//*[@id="yapi"]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/i')
project_btn.click()
time.sleep(1)

'''
Iterate through local folders
'''
# Open all the categorized folders in the left
# for i in range(START_FOLDER_NUM + 1, END_FOLDER_NUM + 1):
for i in range(76,82):

    # Get the currently iterated directory
    input_directory = "./updated_texts/" + str(i)
    if not os.path.exists(input_directory):
        continue

    webidx = i + 1
    # Find API folders using the relative XPath of them
    api_folder_path = '//*[@id="yapi"]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/ul/li[' + str(webidx) + ']'
    wait.until(EC.presence_of_element_located((By.XPATH, api_folder_path)))
    api_folder_btn = driver.find_element(By.XPATH, api_folder_path)
    api_folder_btn.click()

    '''
    Iterate through files in the current directory
    '''
    for alt_file in os.listdir(input_directory):
        alt_file = alt_file[:-4]
        #DEBUG
        print("file want to upload: " + alt_file)
        time.sleep(1)
        '''
        Iterate through API files within the online folder
        '''
        # Open all the API files after expanding each category folder
        api_files = driver.find_elements(By.XPATH, api_folder_path + '/ul/li/span[2]/span/div/a[contains(@class, "interface-item")]')
        # Iterate through the API files
        for api_file in api_files:
            time.sleep(1)
            api_file.click()
            time.sleep(2) 

            '''
            Get API name out of its title
            '''
            api_name = 'unknown'
            # This is the "api名字" span
            title_path = '//*[@id="yapi"]/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/div[2]/span'
            wait.until(EC.presence_of_element_located((By.XPATH, title_path)))
            title_sec = driver.find_element(By.XPATH, title_path)
            # Process the api name to make sure there's no /
            api_name = title_sec.text
            index = api_name.rfind("/") + 1
            api_name = api_name[index:]

            #DEBUG 
            print("api: " + api_name)
            # #DEBUG
            if api_name != alt_file:
                continue
            # time.sleep(1)

            '''
            Switch to the edit page
            '''
            # This is the "编辑" button
            edit_path = '//*[@id="yapi"]/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div[3]'
            wait.until(EC.presence_of_element_located((By.XPATH, edit_path)))
            edit_btn = driver.find_element(By.XPATH, edit_path)
            edit_btn.click()
            time.sleep(1)  # Add a delay of 1 second before clicking the element
            
            try:
                '''
                Click on the setting button
                '''
                # This is the "高级设置" button for "root"
                root_path = '//*[@id="yapi"]/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[5]/div[1]/div/div[2]/div[1]/div/div/div/div[1]/div[5]/span[1]/i'
                wait.until(EC.presence_of_element_located((By.XPATH, root_path)))
                root_btn = driver.find_element(By.XPATH, root_path)
                driver.execute_script("arguments[0].scrollIntoView(true);", root_btn)
                time.sleep(1)  # Add a delay of 1 second before clicking the element
                root_btn.click()

            except(TimeoutException, ElementNotInteractableException):
                # Handle the case when the edit button is not found within the waiting time
                print("Edit button not found for API:", api_name)
                continue

            '''
            Start coping text into the pop up window
            '''
            # Coly the text to clipboard to a variable
            copy_text_from_txt_file(input_directory + "/" + alt_file + ".txt")

            # # Click the editor field to set focus
            # pyautogui.click(x=574, y=694)

            # Wait for me to click onto the eidtor
            time.sleep(3)

            # Use keyDown and keyUp to simulate pressing and releasing the Command key
            pyautogui.keyDown('command')

            # Press and release the 'a' and 'c' keys while the Command key is held down
            pyautogui.press('a')
            pyautogui.press('v')

            # Release the Command key
            pyautogui.keyUp('command')

            time.sleep(1)

            #Confirm button
            confirm_path = '/html/body/div[4]/div/div[2]/div/div[1]/div[3]/div/button[2]'
            confirm_btn = driver.find_element(By.XPATH, confirm_path)
            confirm_btn.click()

            # #Close the pop_up window
            
            # close = '/html/body/div[4]/div/div[2]/div/div[1]/button/span'
            # close_btn = driver.find_element(By.XPATH, close)
            # close_btn.click()

            #Don't forget to save the change
            save = '//*[@id="yapi"]/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[8]/div/div/span/div/div/button'
            save_btn = driver.find_element(By.XPATH, save)
            save_btn.click()

            time.sleep(1)

            # Break out of the api-file loop, go back to the local-file loop
            break

# Close the browser
driver.quit()
