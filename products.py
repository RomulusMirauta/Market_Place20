''' Interactionam cu tabelul products '''

import sqlite3
from sesiunea_12.marketplace20.tables import PATH_DB, connection, cursor


#CREATE

products_to_create_list = [
    ('cana', 'vesela', 15.3, 7, 'verde'),
    ('cana de ceai', 'vesela', 16.99, 2, 'albastra'),
    ('cana de cafea', 'vesela', 25.5, 5, 'alba'),
    ('pahar', 'vesela', 10, 23, 'gri'),
    ('pahar de vin', 'vesela', 50.99, 17, 'transparent'),
    ('pahar de bere', 'vesela', 5, 12.98, 'transparent')
]

product_query = '''
    INSERT INTO products (name, category, price, stock_count, description)
    VALUES (?, ?, ?, ?, ?)
'''
# cursor.executemany(product_query, products_to_create_list)
# connection.commit()

#READ / GET ALL PRODUCTS
cursor.execute('''SELECT * FROM products''')
products = cursor.fetchall()
for product in products:
    print(product)

print("---" * 45)


#UPDATE BY ID
cursor.execute('''
    UPDATE products SET price = '99.99'
    WHERE id = '6';
''')
# connection.commit()

print("---" * 45)


#DELETE BY ID
cursor.execute('''
    DELETE from products
    WHERE id = '3';
''')
# connection.commit()
