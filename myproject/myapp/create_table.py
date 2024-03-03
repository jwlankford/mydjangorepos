import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('module4.db')

# Create a cursor object
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE Module4 (grade int)''')

# Insert grades into the table
grades = [(grade,) for grade in range(50, 101)]
c.executemany('INSERT INTO Module4 VALUES (?)', grades)

# Save (commit) the changes and close the connection
conn.commit()
conn.close()