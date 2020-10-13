from datetime import datetime
from patient import Patient

patients = []

with open('data.txt', 'r', encoding='utf-8') as dataFile:
    for line in dataFile:
        words = line.split(';')
        p = Patient(
            words[0],
            words[1],
            words[2],
            datetime(year=int(words[3]), month=int(words[4]), day=int(words[5])),
            words[6],
            int(words[7]),
            int(words[8]),
            words[9],
        )

        patients.append(p)

smallest_patient = 999
all_male_height = 0
male_count = 0

for patient in patients:
    if patient.weight <= smallest_patient:
        smallest_patient = patient.weight
        
    if patient.sex == 'Чоловік':
        all_male_height += patient.height
        male_count += 1

middle_height = all_male_height / male_count



print('Smallest patient: ', smallest_patient)
print('Middle height: ', middle_height)