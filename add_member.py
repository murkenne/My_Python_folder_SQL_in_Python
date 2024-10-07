from connect_mysql import connect_database


# Define a basic function to add a member
def add_member(id, name, age):
    """Adds a new member to the 'Members' table."""
    conn = connect_database()  # Connect to the database
    
    if conn:  # If connection is successful
        cursor = conn.cursor()
        
        # SQL query to add a new member
        query = "INSERT INTO members (id, name, age) VALUES (%s, %s, %s)"
        new_member = (id, name, age)  # New member details
        
        try:
            cursor.execute(query, new_member)  # Execute the query
            conn.commit()  # Commit the changes
            print("New member added!")  # Print success message
        except:
            print("Something went wrong...") 
        finally:
            cursor.close()  # Close the cursor
            conn.close()  # Close the connection
    else:
        print("Connection failed!") 

# Call the function to test it
add_member(1, 'Jane Doe', 30)
