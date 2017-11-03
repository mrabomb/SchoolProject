import csv
import time
from pyvirtualdisplay import Display
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

path_to_chromedriver = '\Alex\Documents\Repos\BitcoinBot\src\driver\chromedriver' # change path as needed
driver = webdriver.Chrome(executable_path = path_to_chromedriver, chrome_options=chrome_options)

def openDriver():
    url = 'http://bitcointicker.co/bitstamp/'
    driver.get(url)

def closeDriver():
    driver.quit()

def refreshDriver():
    driver.refresh()
    
def writeToFile(ttimes, tpriceg, tvol):
    title = '../CSVs/' + str(int(time.time()))+ '.csv'          
    with open(title, "w") as f:
        rows = zip(ttimes, tpriceg, tvol)
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

def parse():
    count = 0
    while(True):
        ttime_element = driver.find_elements_by_xpath("//div[@class='ttime']")
        ttimes = [x.text for x in ttime_element]


        tpriceg_element = driver.find_elements_by_xpath("//div[@class='tpriceg']")
        tpriceg = [x.text for x in tpriceg_element]

        tvol_element = driver.find_elements_by_xpath("//div[@class='tvol']")
        tvol = [x.text for x in tvol_element]

        if((count%10 == 0) and (count > 0)):
            writeToFile(ttimes, tpriceg, tvol)
            if(count%60 == 0):
                refreshDriver()

        time.sleep(5)
        count = count + 1
    


if __name__ == "__main__":
    openDriver()
    

