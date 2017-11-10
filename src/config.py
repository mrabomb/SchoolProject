settings = dict(
        #this is for SeleniumScraper.py
        #time between calculations related to aggregation
	secondsToWait = 5,
	populationsBeforeUpdate = 6,
	updatesBeforeRefresh = 3, 

        #this is for ErrorCounter.py
        #Print every function or just the ones that arent expected?
        printAll = False            


        #Time between calculations (not time between data collection)
        #uncomment exactly one of these
        minutesToWait = (
                            1
                            #5
                            #15
                            #30
                            #60
                        )
)
