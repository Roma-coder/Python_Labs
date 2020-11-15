import shelve
from club import Club

FILENAME = "clubs"
with shelve.open(FILENAME) as clubs:
    clubs["Barca"] = Club("Barca", "Barcelona", 1900, "Hosep Bartomeu", 2000000, 25)
    clubs["Milan"] = Club("Milan", "Italy", 1899, "Paolo Skaroni", 1050000, 20)
    clubs["Napoly"] = Club("Napoly", "Italy", 1926, "Aurelio de Laurentis", 1200000, 22)
    clubs["Roma"] = Club("Roma", "Italy", 1927, "James Palotta", 1500000, 23)
    clubs["Dynamo"] = Club("Dynamo", "Ukraine", 1955, "Ihor Surkis", 1000000, 15)
