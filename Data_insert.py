import sched, time
s = sched.scheduler(time.time, time.sleep)

def upload_data(sc): 
    seconds = time.time()
    local_time = time.ctime(seconds)
    print("Uploaded data at...", local_time)
    # do your stuff
    s.enter(60, 1, upload_data, (sc,))

s.enter(1, 1, upload_data, (s,))
s.run()