import os
import csv
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

def openDriver(driver):
    url = 'http://bitcointicker.co/bitstamp/'
    driver.set_script_timeout(10)
    try:
        driver.get(url)
    except socket.timout:
        openDriver()

def closeDriver(driver):
    driver.quit()

def refreshDriver(driver):
    driver.refresh()
    
def writeToFile(ttimes, tpriceg, tvol):
    title = '/CSVs/' + str(int(time.time()))+ '.csv'          
    with open(title, "w") as f:
        rows = zip(ttimes, tpriceg, tvol)
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

def recordError(e):
    outFile = open('/ErrorLog/' + str(int(time.time()))+ '.txt', 'w')          
    for f in e:
        outFile.write(f)
    outFile.close()
        

def parse(driver):
    try:
        count = 0
        while(True):
            #set the lists we will use as empty
            ttime_element = []
            tpriceg_element = []
            tvol_element = []
            ttimes = []
            tpriceg = []
            tvol = []

            #wait for the page to load 5 seconds of data
            print("timeout at sleep")
            time.sleep(5)

            #copy the relevant classes to lists
            print("timeout at ttime_element")
            ttime_element = driver.find_elements_by_xpath("//div[@class='ttime']")
            print("timeout at tpriceg_element")
            tpriceg_element = driver.find_elements_by_xpath("//div[@class='tpriceg']") 
            print("timeout at tvol_element")
            tvol_element = driver.find_elements_by_xpath("//div[@class='tvol']")
            print("timeout at ttimes")

            #convert them to lists of text
            ttimes = [x.text for x in ttime_element]
            print("timeout at priceg")
            tpriceg = [x.text for x in tpriceg_element]
            print("timeout at tvol")
            tvol = [x.text for x in tvol_element]

            #if we've done this 12 times, write out
            if((count%12 == 0) and (count > 0)):
                print("about to write")
                writeToFile(ttimes, tpriceg, tvol)

                #if we have written out 3 times, refresh the page
                if(count%(3*12) == 0):
                    print("about to refresh")
                    refreshDriver(driver)
            #increment the conter
            count = count + 1

            #clear the shell so we can tell what breaks if theres a crash
            os.system('cls' if os.name == 'nt' else 'clear')

    except Exception as e: #yes I did just do this. Shoot me
        recordError(e)
        parse(driver)

#upon startup do this
if __name__ == "__main__":

    path_to_chromedriver = ''
    if os.name == 'nt':
        path_to_chromedriver = os.getcwd()+'\driver\windows\chromedriver' # change path as needed
    else:
        path_to_chromedriver = os.getcwd()+'\driver\linux\chromedriver' # change path as needed
    driver = webdriver.Chrome(executable_path = path_to_chromedriver)
    openDriver(driver)
    parse(driver)
    closeDriver(driver)
    

