import schedule
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
try:
    import autoit
except ModuleNotFoundError:
    pass
import time
import datetime
import os


def func(input, message):

	browser = None
	Link = "https://web.whatsapp.com/"
	wait = None
	
	input = '"' + input + '"'

	
	chrome_options = Options()
	chrome_options.add_argument('--user-data-dir=./User_Data')
	browser = webdriver.Chrome('C:/Users/RayyanMerchant/Desktop/TSEC/TSEC/userlogin/chromedriver.exe')
	wait = WebDriverWait(browser, 600)
	browser.get(Link)
	browser.maximize_window()
	print("QR scanned")

	target = input
	try:
		x_arg = '//span[contains(@title,' + target + ')]'
		ct = 0
		while ct != 10:
			try:
				group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
				group_title.click()
				break
			except:
				ct += 1
				time.sleep(3)
		input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
		for ch in message:
			if ch == "\n":
				ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
			else:
				input_box.send_keys(ch)
		input_box.send_keys(Keys.ENTER)
		print("Message sent successfuly")
		time.sleep(1)
	except NoSuchElementException:
		pass
	browser.quit()












































