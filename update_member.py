from connect_mysql import connect_database


def update_member_age(member_id, new_age):

    # Connect to the database
    conn = connect_database()
    
    if conn: # Check if the connection was successful
        try:
            cursor = conn.cursor()
            
            # Check if the member exists
            cursor.execute("SELECT * FROM members WHERE id = %s", (member_id))
            result = cursor.fetchone()
            
            if result: # If member found
                # Update the member's age 
                cursor.execute("UPDATE members SET age = %s WHERE id = %s", (new_age, member_id))
                conn.commit()
                print("Updated member's age.")
            else:
                print("Member not found.")
        except:
            print("Error occurred.") 
        finally:
            cursor.close()
            conn.close()
    else:
        print("Database connection failed")
        
        
# Call the function to test it
update_member_age(1,35)