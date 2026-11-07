import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE Car (
#     id INTEGER PRIMARY KEY AUTOINCREMENT
#              NOT NULL
#              UNIQUE
# );''')

# cursor.execute('''INSERT INTO Car (name, model, year, activ)
#  VALUES (?,?,?,?)
# ''', ('LADA', 2106, 1979, 1))
# cursor.execute('''DELETE FROM Car WHERE id = 2''')

conn.commit()
# result = cursor.execute('''SELECT name, model, year FROM Car WHERE year <> 1979;''')
# result = cursor.execute('''SELECT name, model, year FROM Car
# WHERE year BETWEEN 1970 and  2020;''')
# result = cursor.execute('''SELECT name, model, year FROM Car
# WHERE year in (1970, 1979, 2019);''')
# result = cursor.execute('''SELECT name, model, year FROM Car
# WHERE name LIKE "M_______";''')
# result = cursor.execute('''SELECT name, model, year FROM Car
# WHERE name LIKE "M%" OR model LIKE "2%";''')
# result = cursor.execute('''SELECT DISTINCT year FROM Car;''')
# result = cursor.execute('''SELECT name, model, year FROM Car
# WHERE year BETWEEN 1970 and  2020 ORDER BY name DESC;''')  # ASC, DESC
# result = cursor.execute('''SELECT name, model, year FROM Car
# WHERE year BETWEEN 1970 and 2020 ORDER BY name DESC LIMIT 3 OFFSET 1;''')
# result = cursor.execute('''SELECT name, model, year FROM Car
# WHERE year BETWEEN 1970 and 2020 ORDER BY name DESC LIMIT 2, 4 ;''')
# result = cursor.execute('''SELECT COUNT(activ) FROM Car;''')
# result = cursor.execute('''SELECT name, AVG(amount) FROM Car GROUP BY name;''')
result = cursor.execute('''SELECT name, SUM(amount) FROM Car GROUP BY name;''')

print(result)
for row in result.fetchall():
    print(row)
