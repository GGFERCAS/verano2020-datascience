
import requests
import timeit

def do_something():
    url = "https://www.google.co.uk"
    requests.get(url)


start_timing = timeit.default_timer()
do_something()
end_time = timeit.default_timer()

print("It took {} seconds to run".format(end_time - start_timing))