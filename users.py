''' Interactionam cu tabelul users '''

import sqlite3
from sesiunea_12.marketplace20.tables import PATH_DB, connection, cursor


#CRUD - ne ajuta sa actualizam, modificam, adaugam, stergem date din DB


#CREATE

#1
# cursor.execute(
#     '''
#     INSERT INTO users (username, email, password, first_name, last_name)
#     VALUES ('ion12', 'i@email.com', '123i', 'Ion', 'Pop')
#     '''
# )
#
# connection.commit()

#2
user_query = '''
    INSERT INTO users (username, email, password, first_name, last_name, address, city, postal_code, country)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
# # tuplu
#
# cursor.execute(user_query, ('ioana12', 'ioana@email.com', '123Ioana', 'Ioana', 'Popa', 'str Constanta nr 2', 'Brasov', '123002', 'Romania'))
# connection.commit()

#3
# users_to_create_list = [
#     ('maria02', 'mr@email.com', '123Mr', 'Maria', 'Popescu', 'str 9 Mai nr 56', 'Bacau', '123003', 'Romania'),
#     ('matei03', 'mt@email.com', '123Mt', 'Matei', 'Popovici', 'str Lalelelor nr 8', 'Cluj', '964378', 'Romania'),
#     ('flori00', 'fl@email.com', '123Fl', 'Flori', 'Plop', 'str Condor nr 1', 'Iasi', '122000', 'Romania')
# ]
# cursor.executemany(user_query, users_to_create_list)
# connection.commit()


#READ / GET ALL USERS
cursor.execute('''SELECT * FROM users''')
users = cursor.fetchall()
# print(users)
# print(type(users))

for user in users:
    print(user)

print("---" * 45)


#READ / GET USER BY ID
cursor.execute('''SELECT * FROM users WHERE id = 3''')
user_id = cursor.fetchone()
print(user_id)

print("---" * 45)


#READ / GET USER BY USERNAME
get_by_username_query = '''SELECT * FROM users WHERE username = ?'''
cursor.execute(get_by_username_query, ("matei03",))
user_username = cursor.fetchone()
print(user_username)
print("---" * 45)


#UPDATE USER BY ID
# cursor.execute('''
#     UPDATE users SET username = 'flori02'
#     WHERE id = '5';
# ''')
# connection.commit()


#DELETE USER BY ID
cursor.execute('''
    DELETE FROM users 
    WHERE id = '4';
''')
# connection.commit()
