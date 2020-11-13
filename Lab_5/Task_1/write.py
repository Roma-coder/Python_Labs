import shelve
from club import Club


#загальний бютжет клубів в заданій країні
#клуб який має найбільше трофеїв

FILENAME = "clubs"
with shelve.open(FILENAME) as clubs:
    clubs["Barca"] = club("Barcelona", 1950, "Enqriue Iglesia")