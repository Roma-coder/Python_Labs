from person import Person


class Patient(Person):
    def __init__(self, last_name, first_name, surname, birthday, sex, height, weight, diagnosis):
        Person.__init__(self, last_name, first_name, surname, birthday)

        self.sex = sex
        self.height = height
        self.weight = weight
        self.diagnosis = diagnosis
    