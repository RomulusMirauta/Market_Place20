''' Interactionam cu tabelul orders '''

import sqlite3
from sesiunea_12.marketplace20.tables import PATH_DB, connection, cursor


#pasul 1 cream o comanda
order_query = '''INSERT INTO orders (customer_id, order_date) VALUES (3, '05.09.2024')'''
order_query2 = '''INSERT INTO orders (customer_id, order_date) VALUES (2, '06.09.2024')'''
# cursor.execute((order_query))
# cursor.execute((order_query2))
# connection.commit()


#pasul2 sa adaugam produse in cos
order_items_query = '''
    INSERT INTO order_items (order_id, product_id, quantity, total_price)
    VALUES (?, ?, ?, ?)
'''

order_items_list = [(1, 4, 5, 50), (1, 5, 10, 509.9)]
order_items_list2 = [(2, 1, 10, 153), (2, 3, 10, 255), (2, 4, 5, 50)]
# cursor.executemany(order_items_query, order_items_list)
# cursor.executemany(order_items_query, order_items_list2)
# connection.commit()


#READ / GET ORDER BY ID

get_order_by_id_and_items_query = '''
    SELECT orders.id, orders.customer_id, orders.order_date,
    order_items.product_id, order_items.quantity, order_items.total_price
    FROM orders
    LEFT JOIN order_items ON orders.id = order_items.order_id
    WHERE orders.id = ?;
'''
cursor.execute(get_order_by_id_and_items_query, (1,))   # de ce punem virgula? nu merge fara...
order_and_items = cursor.fetchall()
# print(order_and_items)


#UPDATE ORDER
update_order_query = '''
    UPDATE order_items SET quantity = ?
    WHERE order_id = ? AND product_id = ?;
'''
new_quantity = 100
order_id = 1
product_id = 5

# cursor.execute(update_order_query, (new_quantity, order_id, product_id,))
# connection.commit()


#DELETE ORDER
delete_order_query = '''DELETE FROM orders WHERE id = ?'''
# cursor.execute(delete_order_query, (1,))
# connection.commit()



# TEMA: pe proiectul facut pentru POO - de folosit ce am invatat astazi
# de incercat implementarea concepte baze de date


# VACANTA: CURSURI - vezi calendar
