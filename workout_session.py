# workout_sessions.py

from connect_mysql import connect_database

# Task 2: Add a Workout Session
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    """Add a new workout session to the 'WorkoutSessions' table for a specific member."""
    conn = connect_database()  # Connect to the database
    
    if conn:
        try:
            cursor = conn.cursor()

            # Check if the member ID is valid
            cursor.execute("SELECT * FROM members WHERE id = %s", (member_id,))
            member_exists = cursor.fetchone()

            if member_exists:
                # SQL query to add a new workout session
                query = """
                INSERT INTO WorkoutSessions (member_id, session_date, duration_minutes, calories_burned)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (member_id, date, duration_minutes, calories_burned))
                conn.commit()
                print("Workout session added successfully.")
            else:
                print("Invalid member ID. Cannot add workout session.")

        except:
            print("Failed to add workout session.")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database.")

# Task 4: Delete a Workout Session
def delete_workout_session(session_id):
    """Delete a workout session based on its session ID."""
    conn = connect_database()  # Connect to the database

    if conn:
        try:
            cursor = conn.cursor()
            
            # Check if the session ID exists
            cursor.execute("SELECT * FROM WorkoutSessions WHERE session_id = %s", (session_id,))
            session_exists = cursor.fetchone()

            if session_exists:
                # SQL query to delete the session
                delete_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
                cursor.execute(delete_query, (session_id,))
                conn.commit()
                print(f"Workout session with ID {session_id} deleted.")
            else:
                print(f"No workout session found with ID {session_id}.")

        except:
            print("Failed to delete workout session.")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database.")
