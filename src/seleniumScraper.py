import os
import csv
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#custom module
import config
from CsvConcatonator import *

def openDriver(driver):
    url = 'http://bitcointicker.co/bitstamp/'
    driver.set_script_timeout(20)
    try:
        driver.get(url)
    except socket.timout:
        openDriver()

def closeDriver(driver):
    driver.quit()

def refreshDriver(driver):
    driver.refresh()
    
def writeToFile(ttimes, tpriceg, tvol, writeCount):
    #we are going to need the date inserted before the timestamp in the first row
    date = time.strftime("%Y:%m:%d")
    
    title = '../CSVs/' + str(int(time.time()))+ '.csv'
    dateList = []
    writeCountList = []
    for x in ttimes:
        dateList.append(date)
        writeCountList.append(writeCount)
    with open(title, 'w') as f:
        rows = zip(dateList, ttimes, tpriceg, tvol, writeCountList)
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)
    writeCount = writeCount + 1
    return writeCount

def recordError(e, debug):
    outTime = str(int(time.time()))
    outFile = open(('../ErrorLog/Errors.txt'), 'a+')
    outFile.write("\n\n" + outTime)
    try:
        for f in e:
            outFile.write(str(f))
    except Exception as f:
        outFile.write(str(e))
    outFile.write("\n" + debug)

def parse(driver, writeCount):
    try:
        debug = "file start"
        count = 0
        while(True):
            #set the lists we will use as empty
            ttime_element = []
            tpriceg_element = []
            tvol_element = []
            ttimes = []
            tpriceg = []
            tvol = []

            #read from config file
            secondsToWait = int(config.settings['secondsToWait'])
            populationsBeforeUpdate = int(config.settings['populationsBeforeUpdate'])
            updatesBeforeRefresh = int(config.settings['updatesBeforeRefresh'])

            #wait for the page to load secondsToWait seconds of data
            debug = "timeout at sleep"
            i = 0
            while i < secondsToWait:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Time remaining until next cycle: " + str(int(secondsToWait - i)))
                time.sleep(1)
                i = i + 1

            #copy the relevant classes to lists
            debug = "timeout at ttime_element"
            ttime_element = driver.find_elements_by_xpath("//div[@class='ttime']")
            debug = "timeout at tpriceg_element"
            tpriceg_element = driver.find_elements_by_xpath("//div[@class='tpriceg']") 
            debug = "timeout at tvol_element"
            tvol_element = driver.find_elements_by_xpath("//div[@class='tvol']")
            debug = "timeout at ttimes"

            #convert them to lists of text
            ttimes = [x.text for x in ttime_element]
            debg = "timeout at priceg"
            tpriceg = [x.text for x in tpriceg_element]
            debug = "timeout at tvol"
            tvol = [x.text for x in tvol_element]

            #if we've done this desired number of times, write out
            if((count%populationsBeforeUpdate == 0) and (count > 0)):
                debug = "about to write"
                writeCount = writeToFile(ttimes, tpriceg, tvol, writeCount)
                debug = "about to concatonate"
                Concatonate()
                #if we have written out desired number of times, refresh the page
                if(count%(updatesBeforeRefresh*populationsBeforeUpdate) == 0):
                    debug = "about to refresh"
                    refreshDriver(driver)
                    count = 0
            #increment the conter
            count = count + 1

            #clear the shell so we can tell what breaks if theres a crash
            os.system('cls' if os.name == 'nt' else 'clear')

    except Exception as e: #yes I did just do this. Shoot me
        recordError(e, debug)
        try:
            refreshDriver(driver)
            parse(driver, writeCount)
        except Exception as f:
            debug = "failed to refresh after exception"
            recordError(f, debug)
            openDriver(driver)
            parse(driver, writeCount)
        

#upon startup do this
if __name__ == "__main__":
    path_to_chromedriver = ''
    if os.name == 'nt':
        path_to_chromedriver = os.getcwd()+'\driver\windows\chromedriver' # change path as needed
    else:
        path_to_chromedriver = os.getcwd()+'\driver\linux\chromedriver' # change path as needed
    driver = webdriver.Chrome(executable_path = path_to_chromedriver)

    #int value representing how many times we've written. Helps keep data together
    writeCount = 0
    openDriver(driver)
    parse(driver, writeCount)
    closeDriver(driver)
    

