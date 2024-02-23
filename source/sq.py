import sqlite3
# Create a connection to the database (or create it if it doesn't exist)
conn = sqlite3.connect('feed3.db')
c = conn.cursor()
# Create a table for faculty login information
c.execute('''CREATE TABLE IF NOT EXISTS faculty (
             faculty_id VARCHAR(10) PRIMARY KEY,
             password TEXT)''')
    # Create a table for student login information
c.execute('''CREATE TABLE IF NOT EXISTS students (
             student_id VARCHAR(10) PRIMARY KEY,
             password TEXT)''')
    # Insert some sample data for faculty
c.execute("INSERT INTO faculty (faculty_id, password) VALUES (?, ?)", ('SVECW101', 'Vishnu'))
    # Insert some sample data for students
c.execute("INSERT INTO students (student_id, password) VALUES (?, ?)", ('22B01A4229', 'Madhu'))
    # Commit changes and close connectio
conn.commit()
conn.close()