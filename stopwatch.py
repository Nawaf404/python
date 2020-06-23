import time
print("press enter to start time")
while True:
    try:
        input()
        starttime = time.time() # count time from now
        print("started")
        while True:
            print("Time elaspsed : ", round(time.time() - starttime, 0), 'secs' ,end='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nstopped")
        endtime = time.time()
        print("Total time : ", round(endtime - starttime, 2), 'secs')
        break
