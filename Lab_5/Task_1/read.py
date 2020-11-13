import shelve
from club import Club



FILENAME = "clubs"

with shelve.open(FILENAME) as states:
    print(states["London"])
    print(states["Madrid"])

