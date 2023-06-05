import mysql.connector
import json

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="db_password",
    database="sspanel_dev"
)

# Create a MySQL cursor
cursor = cnx.cursor()

# Query the data to be updated
select_query = "SELECT custom_config FROM node WHERE sort = 11 AND custom_config LIKE '%path%'"
cursor.execute(select_query)
rows = cursor.fetchall()

# Iterate over the query results and update the data
for row in rows:
    custom_config = json.loads(row[0])

    # Check if ws-opts field exists
    if 'ws-opts' not in custom_config:
        path = custom_config.get('path', '')
        host = custom_config.get('host', '')

        custom_config['ws-opts'] = {
            'path': path,
            'headers': {
                'Host': host
            }
        }

        updated_config = json.dumps(custom_config, indent=4)

        # Execute the update operation
        update_query = "UPDATE node SET custom_config = %s WHERE custom_config = %s"
        cursor.execute(update_query, (updated_config, row[0]))

# Commit the changes
cnx.commit()

# Close the cursor and database connection
cursor.close()
cnx.close()