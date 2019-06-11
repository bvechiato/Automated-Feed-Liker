from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

f = open("receipts.txt","a+")

driver = webdriver.Chrome(executable_path='')


id = ''
passd = ''

driver.get('https://www.instagram.com/accounts/login')

def login():
	driver.implicitly_wait(5)
	username = driver.find_element_by_xpath("//input[@name='username']")
	username.send_keys(id)
	password = driver.find_element_by_xpath("//input[@name='password']")
	password.send_keys(passd)
	webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
	time.sleep(5)
	driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()

def record_time():
	localtime = time.asctime(time.localtime(time.time()))
	f.write(str(localtime))
	f.write("\n")

def liking():
	y = 0
	like = 0
	unliked = 0
	while unliked <> 30:
		y += 400
		driver.execute_script("window.scrollTo(0, %d)" % (y))
		try:
			#like
			driver.implicitly_wait(2)
			driver.find_element_by_class_name("glyphsSpriteHeart__outline__24__grey_9").click()
			like += 1
			unliked = 0
			#user
			driver.implicitly_wait(2)
			find_user = driver.find_element_by_class_name("FPmhX")
			user = find_user.text
			if like == 1:
				f.write("1 post has been liked so far by {}.\n".format(user))
			else:
				f.write("{} posts have been liked so far. Last by {}.\n".format(like, user))
		except:
			#liked
			driver.implicitly_wait(2)
			driver.find_element_by_class_name("glyphsSpriteHeart__filled__24__red_5")
			unliked += 1
			#user
			driver.implicitly_wait(2)
			find_user = driver.find_element_by_class_name("FPmhX")
			user = find_user.text
			if unliked == 1:
				f.write("1 post was found liked by {}.\n".format(user))
			else:
				f.write("{} posts were found liked. Last by {}.\n".format(unliked, user))
		else:
			try:
				y = y + 200
				driver.execute_script("window.scrollTo(0, %d)" % (y))
			except:
				break

login()
record_time()
liking()
f.write("\n ------------------ \n")
driver.quit()
