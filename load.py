import psycopg2


def load_data(cleaned_data, table_name, conn):
    print("load connection success")
    cur = conn.cursor()

    for row in cleaned_data:
        columns = list(row.keys())              # ['hospital_name', 'contact', ...]
        values = list(row.values())             # ['Sirirat', '+6680', ...]

        placeholders = ", ".join(["%s"] * len(values))     # '%s, %s, %s, ...'
        column_names = ", ".join(columns)

        insert_sql = f"""
            INSERT INTO {table_name} ({column_names})
            VALUES ({placeholders});
        """

        cur.execute(insert_sql, values)

    conn.commit()
    
    cur.close()
    
    conn.close()
    
