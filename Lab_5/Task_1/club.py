from datetime import datetime

class Club: 
    def __init__(self, club_name, country, built_year, president_name, budget, award):
        self.club_name = club_name
        self.country = country
        self.built_year = built_year
        self.president_name = president_name
        self.budget = budget
        self.award = award

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}'\
            .format(self.club_name, self.country, self.built_year, self.president_name,
                self.budget, self.award)