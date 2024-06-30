import time

def tictac(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f'{func.__name__} ran in '\
               f'{t2} seconds')
    return wrapper

@tictac
def do_this():
    time.sleep(1.4)    

@tictac
def do_that():
    time.sleep(.4)    

do_this()
do_that()
print("Done")