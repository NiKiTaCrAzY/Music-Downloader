####################### Libraries #######################
								    					#
import re, time										    #
from selenium.webdriver import *						#
from selenium.webdriver.firefox.options import Options	#
from termcolor import colored       					#
from bs4 import BeautifulSoup as BS						#
import urllib, argparse, platform						#
									   					#
#########################################################

################ Main Class #################

class Download_Music:
	def __init__(self, name):
		pattern = re.search(r'\(.+\)', name)
		if pattern:			
			self.name = name.replace(
				pattern.group(0),
				''
			)
		else:
			self.name = name
		self.opt = Options()
		self.opt.headless = True
		if platform.system() == "Linux":
			if platform.uname()[4] == "x86_64":
				self.driver = Firefox(executable_path = "./geckodriver64", firefox_options = self.opt)
			else:
				self.driver = Firefox(executable_path = "./geckodriver32", firefox_options = self.opt)
		else:
			if platform.uname()[4] == "x86_64":
				self.driver = Firefox(executable_path = "./geckodriver64.exe", firefox_options = self.opt)
			else:
				self.driver = Firefox(executable_path = "./geckodriver32.exe", firefox_options = self.opt)
	def get_music_webpage(self):
		self.driver.get("https://goobum.ru/index.php?do=search")
		time.sleep(10)
		self.driver.find_element_by_id("searchinput").send_keys(self.name)
		self.driver.find_element_by_id("dosearch").click()
		time.sleep(3)
		html_code = self.driver.page_source
		soup = BS(
			html_code,
			"html.parser"
		)
		mp3_file = soup.find("div", {"class": "track-item anim fx-row fx-middle js-item js-item-current js-item-stopped"})['data-track']
		urllib.request.urlretrieve(mp3_file, self.name.replace(' ', '') + ".mp3")

#############################################

AUTHOR = "NiKiTaCrAzY ( or Pythonforever )"
GITHUB = "https://github.com/NiKiTaCrAzY"

############## Main Code ##############

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--name")
	music_name = parser.parse_args().name
	download_object = Download_Music(music_name)
	download_object.get_music_webpage()

#######################################
