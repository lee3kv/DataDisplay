# test file
import time

def data_format():
    # grab latest time every callback
    seconds = time.time()
    local_time = time.ctime(seconds)
    hour = time.strftime("%I_%M_%S", time.localtime())
    data_format.day = time.strftime("%m_%d", time.localtime())

data_format()

def something():
    print(data_format.day)

something()
something()
def hi():
    # other code...
    hi.bye = 42  # Create function attribute.
    sigh = 10

hi()
print(hi.bye)  # -> 42