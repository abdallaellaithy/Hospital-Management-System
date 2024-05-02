import tkinter as tk
import psycopg2  

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="Hospital_Mangement_System",
    user="postgres",
    password="#####"
)
cursor = conn.cursor()

# GUI Functions
def insert_patient():
    patient_id = patient_id_entry.get()
    patient_name = patient_name_entry.get()
    date_of_birth = date_of_birth_entry.get()
    gender = gender_entry.get()
    address = address_entry.get()
    contact_number = contact_number_entry.get()

    # Execute the SQL query to insert patient data
    cursor.execute("""
        INSERT INTO patients (patient_id, patient_name, date_of_birth, gender, address, contact_number)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (patient_id, patient_name, date_of_birth, gender, address, contact_number))
    conn.commit()


def update_patient():
    patient_id = patient_id_entry.get()
    current_patient_name = current_patient_name_entry.get()
    new_patient_name = new_patient_name_entry.get()

    # Execute the SQL query to update patient data
    cursor.execute("""
        UPDATE patients
        SET patient_name = %s
        WHERE patient_name = %s
    """, (new_patient_name, current_patient_name))
    conn.commit()


def delete_patient():
    patient_name = patient_name_entry.get()

    # Execute the SQL query to delete patient data
    cursor.execute("""
        DELETE FROM patients
        WHERE patient_name = %s
    """, (patient_name,))
    conn.commit()


def create_new_table():
    table_name = table_name_entry.get()
    primary_key = primary_key_entry.get()
    foreign_key = foreign_key_entry.get()
    rest_columns = rest_columns_entry.get().split(",")

    # Construct the SQL query to create a new table
    query = f"CREATE TABLE {table_name} ({primary_key} INTEGER PRIMARY KEY, {foreign_key} INTEGER,"
    for column in rest_columns:
        query += f" {column} TEXT,"
    query = query.rstrip(",") + ")"

    # Execute the SQL query to create the new table
    cursor.execute(query)
    conn.commit()


def insert_doctor():
    doctor_id = doctor_id_entry.get()
    doctor_name = doctor_name_entry.get()
    department_id = department_id_entry.get()
    specialization = specialization_entry.get()
    contact_number = doctor_contact_number_entry.get()
    address = doctor_address_entry.get()

    # Execute the SQL query to insert doctor data
    cursor.execute("""
        INSERT INTO doctors (doctor_id, doctor_name, department_id, specialization, contact_number, address)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (doctor_id, doctor_name, department_id, specialization, contact_number, address))
    conn.commit()


def update_doctor():
    doctor_id = doctor_id_entry.get()
    current_doctor_name = current_doctor_name_entry.get()
    new_doctor_name = new_doctor_name_entry.get()

    # Execute the SQL query to update doctor data
    cursor.execute("""
        UPDATE doctors
        SET doctor_name = %s
        WHERE doctor_id = %s AND doctor_name = %s
    """, (new_doctor_name, doctor_id, current_doctor_name))
    conn.commit()


def delete_doctor():
    doctor_id = doctor_id_entry.get()
    doctor_name = doctor_name_entry.get()

    # Execute the SQL query to delete doctor data
    cursor.execute("""
        DELETE FROM Doctors
        WHERE doctor_id = %s AND doctor_name = %s
    """, (doctor_id, doctor_name))
    conn.commit()


def get_available_beds():
    # Execute the SQL query to get the available beds count
    cursor.execute("SELECT COUNT(*) FROM Beds WHERE availability = 'false'")
    result = cursor.fetchone()[0]
    result_label.config(text="Available Beds: " + str(result))


# Create the main window
window = tk.Tk()
window.title("Hospital Management System")

# Create and place the input fields and buttons for patient operations
patient_id_label = tk.Label(window, text="Patient ID:")
patient_id_label.grid(row=0, column=0)
patient_id_entry = tk.Entry(window)
patient_id_entry.grid(row=0, column=1)

patient_name_label = tk.Label(window, text="Patient Name:")
patient_name_label.grid(row=1, column=0)
patient_name_entry = tk.Entry(window)
patient_name_entry.grid(row=1, column=1)

date_of_birth_label = tk.Label(window, text="Date of Birth:")
date_of_birth_label.grid(row=2, column=0)
date_of_birth_entry = tk.Entry(window)
date_of_birth_entry.grid(row=2, column=1)

gender_label = tk.Label(window, text="Gender:")
gender_label.grid(row=3, column=0)
gender_entry = tk.Entry(window)
gender_entry.grid(row=3, column=1)

address_label = tk.Label(window, text="Address:")
address_label.grid(row=4, column=0)
address_entry = tk.Entry(window)
address_entry.grid(row=4, column=1)

contact_number_label = tk.Label(window, text="Contact Number:")
contact_number_label.grid(row=5, column=0)
contact_number_entry = tk.Entry(window)
contact_number_entry.grid(row=5, column=1)

insert_patient_button = tk.Button(
    window, text="Insert Patient", command=insert_patient)
insert_patient_button.grid(row=6, column=0)

current_patient_name_label = tk.Label(window, text="Current Patient Name:")
current_patient_name_label.grid(row=7, column=0)
current_patient_name_entry = tk.Entry(window)
current_patient_name_entry.grid(row=7, column=1)

new_patient_name_label = tk.Label(window, text="New Patient Name:")
new_patient_name_label.grid(row=8, column=0)
new_patient_name_entry = tk.Entry(window)
new_patient_name_entry.grid(row=8, column=1)

update_patient_button = tk.Button(
    window, text="Update Patient", command=update_patient)
update_patient_button.grid(row=9, column=0)

delete_patient_button = tk.Button(
    window, text="Delete Patient", command=delete_patient)
delete_patient_button.grid(row=10, column=0)

# Create and place the input fields and buttons for doctor operations
doctor_id_label = tk.Label(window, text="Doctor ID:")
doctor_id_label.grid(row=14, column=0)
doctor_id_entry = tk.Entry(window)
doctor_id_entry.grid(row=14, column=1)

doctor_name_label = tk.Label(window, text="Doctor Name:")
doctor_name_label.grid(row=15, column=0)
doctor_name_entry = tk.Entry(window)
doctor_name_entry.grid(row=15, column=1)

department_id_label = tk.Label(window, text="Department ID:")
department_id_label.grid(row=16, column=0)
department_id_entry = tk.Entry(window)
department_id_entry.grid(row=16, column=1)

specialization_label = tk.Label(window, text="Specialization:")
specialization_label.grid(row=17, column=0)
specialization_entry = tk.Entry(window)
specialization_entry.grid(row=17, column=1)

doctor_contact_number_label = tk.Label(window, text="Contact Number:")
doctor_contact_number_label.grid(row=18, column=0)
doctor_contact_number_entry = tk.Entry(window)
doctor_contact_number_entry.grid(row=18, column=1)

doctor_address_label = tk.Label(window, text="Address:")
doctor_address_label.grid(row=19, column=0)
doctor_address_entry = tk.Entry(window)
doctor_address_entry.grid(row=19, column=1)

insert_doctor_button = tk.Button(
    window, text="Insert Doctor", command=insert_doctor)
insert_doctor_button.grid(row=20, column=0)

current_doctor_name_label = tk.Label(window, text="Current Doctor Name:")
current_doctor_name_label.grid(row=21, column=0)
current_doctor_name_entry = tk.Entry(window)
current_doctor_name_entry.grid(row=21, column=1)

new_doctor_name_label = tk.Label(window, text="New Doctor Name:")
new_doctor_name_label.grid(row=22, column=0)
new_doctor_name_entry = tk.Entry(window)
new_doctor_name_entry.grid(row=22, column=1)

update_doctor_button = tk.Button(
    window, text="Update Doctor", command=update_doctor)
update_doctor_button.grid(row=23, column=0)

delete_doctor_button = tk.Button(
    window, text="Delete Doctor", command=delete_doctor)
delete_doctor_button.grid(row=24, column=0)

# Create the GUI window
window = tk.Tk()
window.title("Create New Table")

# Create labels and entry fields for table details
table_name_label = tk.Label(window, text="Table Name:")
table_name_label.grid(row=0, column=0)
table_name_entry = tk.Entry(window)
table_name_entry.grid(row=0, column=1)

primary_key_label = tk.Label(window, text="Primary Key Column:")
primary_key_label.grid(row=1, column=0)
primary_key_entry = tk.Entry(window)
primary_key_entry.grid(row=1, column=1)

foreign_key_label = tk.Label(window, text="Foreign Key Column:")
foreign_key_label.grid(row=2, column=0)
foreign_key_entry = tk.Entry(window)
foreign_key_entry.grid(row=2, column=1)

rest_columns_label = tk.Label(window, text="Rest of Columns (comma-separated):")
rest_columns_label.grid(row=3, column=0)
rest_columns_entry = tk.Entry(window)
rest_columns_entry.grid(row=3, column=1)

# Create a button to create the new table
create_button = tk.Button(window, text="Create Table", command=create_new_table)
create_button.grid(row=4, column=0, columnspan=2)


# Create and place the button for getting available beds count
get_available_beds_button = tk.Button(
    window, text="Get Available Beds", command=get_available_beds)
get_available_beds_button.grid(row=30, column=0)

result_label = tk.Label(window, text="Available Beds:")
result_label.grid(row=31, column=0)

# Start the main loop
window.mainloop()

# Close the database connection
cursor.close()
conn.close()