-- Create the 'Departments' table
CREATE TABLE Departments (
  department_id INT PRIMARY KEY,
  department_name VARCHAR(255) NOT NULL,
  department_head VARCHAR(255) NOT NULL
);

-- Create the 'Doctors' table
CREATE TABLE Doctors (
  doctor_id INT PRIMARY KEY,
  doctor_name VARCHAR(255) NOT NULL,
  department_id INT,
  specialization VARCHAR(255) NOT NULL,
  contact_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

-- Create the 'Patients' table
CREATE TABLE Patients (
  patient_id INT PRIMARY KEY,
  patient_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  gender VARCHAR(10) NOT NULL,
  address VARCHAR(255) NOT NULL,
  contact_number VARCHAR(20) NOT NULL
);


-- Create the 'Appointments' table
CREATE TABLE Appointments (
  appointment_id INT PRIMARY KEY,
  doctor_id INT,
  patient_id INT,
  appointment_date TIMESTAMP NOT NULL,
  FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
  FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Create the 'Medications' table
CREATE TABLE Medications (
  medication_id INT PRIMARY KEY,
  medication_name VARCHAR(255) NOT NULL,
  dosage VARCHAR(50) NOT NULL,
  patient_id INT NOT NULL
);


-- Create the 'Prescriptions' table
CREATE TABLE Prescriptions (
  prescription_id INT PRIMARY KEY,
  doctor_id INT,
  patient_id INT,
  appointment_id INT,
  medication_id INT,
  dosage VARCHAR(50),
  prescription_date DATE,
  FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
  FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
  FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id),
  FOREIGN KEY (medication_id) REFERENCES Medications(medication_id)
);

-- Create the 'Nurses' table
CREATE TABLE Nurses (
  nurse_id INT PRIMARY KEY,
  nurse_name VARCHAR(255) NOT NULL,
  department_id INT,
  contact_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

-- Create the 'Beds' table
CREATE TABLE Beds (
  bed_id INT PRIMARY KEY,
  bed_number INT NOT NULL,
  department_id INT,
  availability Bool,
  FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

-- Create the 'Admissions' table
CREATE TABLE Admissions (
  admission_id SERIAL PRIMARY KEY,
  patient_id INT NOT NULL,
  admission_date DATE NOT NULL,
  department_id INT NOT NULL,
  bed_id INT,
  FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
  FOREIGN KEY (department_id) REFERENCES Departments(department_id),
  FOREIGN KEY (bed_id) REFERENCES Beds(bed_id)
);

-- Create the 'LabTests' table
CREATE TABLE LabTests (
  test_id INT PRIMARY KEY,
  test_name VARCHAR(255) NOT NULL
);

-- Create the 'LabResults' table
CREATE TABLE LabResults (
  result_id INT PRIMARY KEY,
  test_id INT,
  patient_id INT,
  result_date TIMESTAMP NOT NULL,
  result_details TEXT,
  FOREIGN KEY (test_id) REFERENCES LabTests(test_id),
  FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Create the 'Invoices' table
CREATE TABLE Invoices (
  invoice_id INT PRIMARY KEY,
  patient_id INT,
  doctor_id INT,
  amount DECIMAL(10, 2) NOT NULL,
  invoice_date TIMESTAMP NOT NULL,
  FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
  FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);


-- Create the 'Payments' table
CREATE TABLE Payments (
  payment_id INT PRIMARY KEY,
  invoice_id INT,
  payment_date TIMESTAMP NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (invoice_id) REFERENCES Invoices(invoice_id),
  FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);


-- Create the 'MedicalRecords' table
CREATE TABLE MedicalRecords (
  record_id INT PRIMARY KEY,
  patient_id INT,
  doctor_id INT,
  record_date TIMESTAMP NOT NULL,
  record_details TEXT,
  FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
  FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- Add cardinality constraint to Appointments (1 doctor can have multiple appointments)
ALTER TABLE Appointments ADD CONSTRAINT FK_Doctor_Appointments FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id);

-- Add disjointness constraint between Nurses and Doctors (each nurse can only belong to one department)
ALTER TABLE Nurses ADD CONSTRAINT FK_Nurse_Department FOREIGN KEY (department_id) REFERENCES Departments(department_id);

-- Add disjointness constraint between Beds and Doctors (each bed can only belong to one department)
ALTER TABLE Beds ADD CONSTRAINT FK_Bed_Department FOREIGN KEY (department_id) REFERENCES Departments(department_id);

-- Add disjointness constraint between Admissions and Patients (each admission can only be associated with one patient)
ALTER TABLE Admissions ADD CONSTRAINT FK_Admission_Patient FOREIGN KEY (patient_id) REFERENCES Patients(patient_id);

-- Add disjointness constraint between Admissions and Beds (each admission can only be associated with one bed)
ALTER TABLE Admissions ADD CONSTRAINT FK_Admission_Bed FOREIGN KEY (bed_id) REFERENCES Beds(bed_id);

-- Add disjointness constraint between LabResults and Patients (each lab result can only be associated with one patient)
ALTER TABLE LabResults ADD CONSTRAINT FK_LabResult_Patient FOREIGN KEY (patient_id) REFERENCES Patients(patient_id);

-- Add disjointness constraint between Invoices and Patients (each invoice can only be associated with one patient)
ALTER TABLE Invoices ADD CONSTRAINT FK_Invoice_Patient FOREIGN KEY (patient_id) REFERENCES Patients(patient_id);

-- Add disjointness constraint between Invoices and Doctors (each invoice can only be associated with one doctor)
ALTER TABLE Invoices ADD CONSTRAINT FK_Invoice_Doctor FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id);

-- Add disjointness constraint between Payments and Invoices (each payment can only be associated with one invoice)
ALTER TABLE Payments ADD CONSTRAINT FK_Payment_Invoice FOREIGN KEY (invoice_id) REFERENCES Invoices(invoice_id);

-- Add disjointness constraint between MedicalRecords and Patients (each medical record can only be associated with one patient)
ALTER TABLE MedicalRecords ADD CONSTRAINT FK_MedicalRecord_Patient FOREIGN KEY (patient_id) REFERENCES Patients(patient_id);

-- Add disjointness constraint between MedicalRecords and Doctors (each medical record can only be associated with one doctor)
ALTER TABLE MedicalRecords ADD CONSTRAINT FK_MedicalRecord_Doctor FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id);
