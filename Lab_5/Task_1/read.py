import shelve
from club import Club

#загальний бютжет клубів в заданій країні
#клуб який має найбільше трофеїв


country = input('country')

FILENAME = "clubs"

with shelve.open(FILENAME) as states:
    clubs_by_country = list(filter(lambda s: s.country.lower() == country.lower(), states))

    if len(clubs_by_country) == 0 :
        print("No clubs with such country")
        exit()

    the_best_club = max(clubs_by_country, key=lambda s: int(s.award))
    clubs_budget = sum(int(club.budget) for club in clubs_by_country)

    print("The best club: ", the_best_club)
    print("Summary budget: ", clubs_budget)



