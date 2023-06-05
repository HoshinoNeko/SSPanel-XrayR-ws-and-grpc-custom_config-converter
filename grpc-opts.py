import mysql.connector
import json

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="dbpassword",
    database="sspanel_dev"
)

# Create a MySQL cursor
cursor = cnx.cursor()

# Query the data to be updated
select_query = "SELECT custom_config FROM node WHERE sort = 11 AND custom_config LIKE '%grpc%'"
cursor.execute(select_query)
rows = cursor.fetchall()

# Iterate over the query results and update the data
for row in rows:
    custom_config = json.loads(row[0])

    # Check if grpc-opts field exists
    if 'grpc-opts' not in custom_config:
        grpc_service_name = custom_config.pop('grpc-service-name', '')
        servicename = custom_config.get('servicename', '')
        grpc_opts = {
            'grpc-service-name': servicename
        }

        custom_config['grpc-opts'] = grpc_opts

        updated_config = json.dumps(custom_config, indent=4)

        # Execute the update operation
        update_query = "UPDATE node SET custom_config = %s WHERE custom_config = %s"
        cursor.execute(update_query, (updated_config, row[0]))

# Commit the changes
cnx.commit()

# Close the cursor and database connection
cursor.close()
cnx.close()