import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Aj@y_054",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# # Full load: Copy all data from customer to customer_backup
# cursor.execute('TRUNCATE TABLE customer_backup')
# cursor.execute('INSERT INTO customer_backup SELECT * FROM customer')

# # Commit the transaction
# conn.commit()

# # Close the connection
# cursor.close()
# conn.close()
# Add unique constraint to customer_backup if not already added
cursor.execute("""
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conname = 'customer_backup_pkey'
    ) THEN
        ALTER TABLE customer_backup ADD CONSTRAINT customer_backup_pkey PRIMARY KEY (cid);
    END IF;
END $$;
""")

# Incremental load: Synchronize customer_backup with customer
merge_query = """
INSERT INTO customer_backup (cid, name, email, lastChange)
SELECT cid, name, email, lastChange FROM customer
ON CONFLICT (cid) DO UPDATE SET
    name = EXCLUDED.name,
    email = EXCLUDED.email,
    lastChange = EXCLUDED.lastChange;
"""

cursor.execute(merge_query)

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()