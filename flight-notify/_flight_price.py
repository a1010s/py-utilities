from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import Select
#import pandas as pd
from selenium.webdriver.chrome.options import Options
#import datetime



options = Options()
#options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-notifications')




# Url to use
url = 'https://www.kayak.de/'

# Driver to use (webdriver.Chrome or Firefox..or etc.) with the driver path as string param

service = ChromeService(executable_path='/home/astegaru/Downloads/chromedriver_linux64/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url, options=options)

sleep(2)

# Open up Chrome
driver.get(url)
driver.maximize_window()
sleep(1)

# Very useful snippet to accept cookies! button[contains](string()
accept = driver.find_elements(By.XPATH, "//button[contains(string(), 'Akzeptieren')]")[0].click()

delete_default_1 = driver.find_element(By.XPATH, '//input[@type="text"]').send_keys(Keys.BACKSPACE)
delete_default_2 = driver.find_element(By.XPATH, '//input[@type="text"]').send_keys(Keys.BACKSPACE)

town1 = input('Enter start location (ex.: Berlin, Deutschland): ')
town2 = input('Enter destination (ex.: Bucharest, Rumänien): ')


# for debug
#town1 = "BER"
#town2 = "OTP"


source = driver.find_element(By.XPATH, '//input[@type="text"]').send_keys(f'{town1}')
sleep(1)
select = driver.find_element(By.XPATH, '//*[@id="flight-origin-smarty-input-list"]/li/div').click()

#sleep(1)
# Problems here: the zEiP ID CHANGE! Need another locator!!!
#destination = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section[2]/div/div/div/div/div/div[1]/div[2]/div/div[3]/div/div/input').send_keys('OTP')
destination = driver.find_element(By.XPATH, '//*[@aria-label="Eingabe Flugziel"]').send_keys(f'{town2}')



sleep(1)    # Aufpassen mit sleep. 1 kann manchmal zu wenig sein!
select = driver.find_element(By.XPATH, '//*[@id="flight-destination-smarty-input-list"]/li/div').click()

original_window = driver.current_window_handle

sleep(1)
# Choose Date

start_date = input('Enter the start date (ex.: Mittwoch 1. März 2023): ')
return_date = input('Enter the return date (ex.: Sonntag 5. März 2023): ')



# for debug
#start_date = "Mittwoch 1. März 2023"
#return_date = "Sonntag 5. März 2023"

click_start_date = driver.find_element(By.XPATH, '//*[@aria-label="Eingabe Startdatum im Kalender"]').click()
sleep(3)
send_start_date = driver.find_element(By.XPATH, f'//*[@class="onx_-days"]/div[@aria-label="{start_date}"]').click()

#send_start_date = driver.find_element(By.XPATH, '//*[@class="onx_-days"]/div[@aria-label="Mittwoch 1. März 2023"]').click()


click_return_date = driver.find_element(By.XPATH, '//*[@aria-label="Eingabe Enddatum im Kalender"]').click()
sleep(2)
send_return_date = driver.find_element(By.XPATH, f'//*[@class="onx_-days"]/div[@aria-label="{return_date}"]').click()

#sleep(2)

submit = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
sleep(25)

# =============================================
# NOT NEEDED, AS I MAXIMIZED THE 
# WINDOW AND A NEW TAB DOESN'T OPEN ANYMORE
# =============================================

#Close the tab or window
#sleep(2)
#new_window = driver.current_window_handle

#Switch back to the old tab or window
#driver.switch_to.window(new_window)
#driver.close()


#price = driver.find_element(By.XPATH, '//*[@class="listBody"]/div[@class="listInner"]').text
#price = driver.find_element(By.XPATH, '//div/[@class="listBody"]/div[@class="resultsContainer"]').text

price = driver.find_element(By.XPATH, '//*[@aria-label="Flug-Suchergebnisse"]').text

print(price)    # string
price_list = price.split() # list
price_list2 = ' '.join(price_list) # string

print(price_list)
print(price_list2)



print('====>> ONLY PRICES <<====')
print()

only_price = price.split()
only_price = ''.join(only_price)

for i, char in enumerate(only_price):
    if char == '€':
        for j in range(i-1, i-5, -1):
            if not only_price[j].isdigit():
                break
        print(only_price[j+1:i] + ' ' + char)


sleep(20)
