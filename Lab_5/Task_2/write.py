import sqlite3

conn = sqlite3.connect('clubs.db')
cursor = conn.cursor()


club_name = input('club name: ')
country  = input('country: ')
built_date = input('built_date: ')
president_name = input('president name: ')
budget = input('budget: ')
award = input('award: ')

cursor.execute('INSERT INTO stadiums VALUES (?, ?, ?, ?, ?)', 
    (club_name, country, built_date, president_name, budget, award))

conn.commit()