
CREATE DATABASE karyawan;



-- Buat tabel departments
CREATE TABLE departments (
    id INT PRIMARY KEY IDENTITY,
    name VARCHAR(255) NOT NULL
);

-- Buat tabel employees
CREATE TABLE employees (
    id INT PRIMARY KEY IDENTITY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    department_id INT NOT NULL,
    salary FLOAT NOT NULL,
    start_date DATE NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments (id)
);

-- Buat tabel employer_projects
CREATE TABLE employer_projects (
    id INT PRIMARY KEY IDENTITY,
    employee_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees (id)
);