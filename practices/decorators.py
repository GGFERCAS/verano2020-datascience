
import requests
import timeit

def timer(function):
    def wrapper():
        start_timing = timeit.default_timer()  
        function()
        end_time = timeit.default_timer()
        print("It took {} seconds to run".format(end_time - start_timing))
    return wrapper


def do_something():
    url = "https://www.google.co.uk"
    requests.get(url)

x = timer(do_something)
x()