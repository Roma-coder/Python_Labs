import sqlite3

conn = sqlite3.connect('clubs.db')
cursor = conn.cursor()

country = input('country')

cursor.execute("""SELECT * FROM clubs
                  WHERE country LIKE ?
                  ORDER BY award
              """, (country, ))

print("The best club:", cursor.fetchone())

cursor.execute("""SELECT sum(budget) as sum FROM clubs
                  WHERE country LIKE ?
                  ORDER BY award
              """, (country, ))

print("Summary country budget: ", cursor.fetchone()[0])