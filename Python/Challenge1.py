import mysql.connector

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Aj@y_054',
        database='challenge1'
    )
    cursor = connection.cursor()

    # Display sales table data
    cursor.execute("SELECT * FROM sales")
    sales_data = cursor.fetchall()
    for row in sales_data:
        print(row)

    # Collect user input for a new sales record
    customer_id = input("Enter customer ID: ")
    order_date = input("Enter order date (YYYY-MM-DD): ")
    product_id = input("Enter product ID: ")

    # Insert the new row into the sales table
    insert_query = "INSERT INTO sales (customer_id, order_date, product_id) VALUES (%s, %s, %s)"
    values = (customer_id, order_date, product_id)
    cursor.execute(insert_query, values)
    connection.commit()

    print("New row inserted successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
