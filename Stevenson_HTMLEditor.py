from fileinput import filename
from bs4 import BeautifulSoup
from selenium import webdriver
import requests as req
import time

driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe')
driver.get("https://linkedin.com/uas/login")
time.sleep(5)

username = driver.find_element_by_id("username")
username.send_keys("bryceas17@gmail.com")
pword = driver.find_element_by_id("password")
pword.send_keys("#Ghost2734")
driver.find_element_by_xpath("//button[@type='submit']").click()

profile_url = "https://www.linkedin.com/in/bryce-stevenson/"
driver.get(profile_url)
start = time.time()
initialScroll = 0
finalScroll = 1000

while True:
	driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
	# this command scrolls the window starting from
	# the pixel value stored in the initialScroll
	# variable to the pixel value stored at the
	# finalScroll variable
	initialScroll = finalScroll
	finalScroll += 1000

	# stop the script for 3 seconds so that the data can load
	time.sleep(3)
	end = time.time()
	if round(end - start) > 20:
		break
src = driver.page_source
S = BeautifulSoup(src,'lxml')
intro = S.find('div', {'class': 'pv-text-details__left-panel'})\

name_loc = intro.find("h1")
name = name_loc.get_text().strip()

works_at_loc = intro.find("div", {'class': 'text-body-medium'})
# this gives us the HTML of the tag in which the Company Name is present
works_at = works_at_loc.get_text().strip()

experience = S.find("section", {"id": "experience-section"}).find('ul')
li_tags = experience.find('div')
a_tags = li_tags.find("a")
job_title = a_tags.find("h3").get_text().strip()

company_name = a_tags.find_all("p")[1].get_text().strip()

joining_date = a_tags.find_all("h4")[0].find_all("span")[1].get_text().strip()

employment_duration = a_tags.find_all("h4")[1].find_all(
	"span")[1].get_text().strip()

lengthOfEmployment = (joining_date + ", " + employment_duration)

with open('parsedwebsiteinfo.html','w') as f:
    f.write(str(S.title))
    f.write(str(name))
    f.write(str(works_at))
    f.write(str(job_title))
    f.write(str(company_name))
    f.write(str(lengthOfEmployment))
    f.close()
filename ='file:///Users/18325/Documents/AdvancedBusinessProgramming/' + 'parsedwebsiteinfo.html'