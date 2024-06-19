# countdown program.... 
# import the time module
import time 
p= int(input("enter time in seconds"))
def countdown(p):
    while p:
        mins,secs=divmod(p,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        p -= 1
    print("Happy Happy Happy !!!")

countdown(p) 


