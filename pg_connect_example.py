import psycopg2, pprint

def main():
    connection_string = "host='localhost' dbname='feeddata_prod' user='postgres'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    return cursor

if __name__ == "__main__":
    cursor = main()
    cursor.execute("SELECT * FROM customers;")
    customers = cursor.fetchall()
    pprint.pprint(customers)