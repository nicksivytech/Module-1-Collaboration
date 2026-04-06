# 11.1
with open('zoo.py', 'w') as f;
  f.write("def hours():\n print('Open 9-5 daily')\n")
import zoo
zoo.hours()

# 11.2
import zoo as menagerie
menagerie.hours()

# 16.8
import sqlalchemy as sa
engine = sa.create_engine('sqlite:///books.db', echo=False)
with engine.connect() as conn:
  conn.execute(sa.text('''
    CREATE TABLE IF NOT EXISTS book (
      id INTEGER PRIMARY KEY,
      title VARCHAR(100),
      author VARCHAR(100)
      )
    '''))
  conn.execute(sa.text("DELETE FROM book"))
  conn.execute(sa.text("INSERT INTO book (title, author) VALUES ('The Hobbit', 'Tolkien')"))
  conn.execute(sa.text("INSERT INTO book (title, author) VALUES ('Moby Dick', 'Melville')"))
  conn.execute(sa.text("INSERT INTO book (title, author) VALUES ('Alice in Wonderland', 'Carroll')"))
  conn.commit()

with engine.connect() as conn:
  result = conn.execute(sa.text("SELECT title FROM book ORDER BY title ASC"))
    for row in result:
      print(row[0])
