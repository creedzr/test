# Import library yang dibutuhkan
import pyodbc

# Koneksikan ke database
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=localhost,1433;"
    "Database=karyawan;"
    "UID=sa;"
    "PWD=secret"
)

# Buat formulir
def create_employee_form():
    # Dapatkan input dari user
    first_name = input("Masukkan nama depan: ")
    last_name = input("Masukkan nama belakang: ")
    department = input("Masukkan departemen: ")
    salary = float(input("Masukkan gaji: "))
    start_date = input("Masukkan tanggal mulai bekerja (YYYY-MM-DD): ")
    project_name = input("Masukkan nama proyek: ")
    project_start_date = input("Masukkan tanggal mulai proyek (YYYY-MM-DD): ")
    project_end_date = input("Masukkan tanggal selesai proyek (YYYY-MM-DD): ")

    # Tambahkan departemen ke database jika belum ada
    cursor = conn.cursor()
    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM departments WHERE name = ?)
        BEGIN
            INSERT INTO departments (name)
            VALUES (?)
        END
    """, (department, department))
    conn.commit()

    # Dapatkan ID departemen
    cursor.execute("""
        SELECT id FROM departments WHERE name = ?
    """, (department,))
    department_id = cursor.fetchone()[0]

    # Tambahkan karyawan ke database
    cursor.execute("""
        INSERT INTO employees (first_name, last_name, department_id, salary, start_date)
        VALUES (?, ?, ?, ?, ?)
    """, (first_name, last_name, department_id, salary, start_date))
    employee_id = cursor.lastrowid
    conn.commit()

    # Tambahkan proyek karyawan ke database
    cursor.execute("""
        INSERT INTO employer_projects (employee_id, name, start_date, end_date)
        VALUES (?, ?, ?, ?)
    """, (employee_id, project_name, project_start_date, project_end_date))
    conn.commit()

    print("Data karyawan berhasil ditambahkan!")

# Jalankan formulir
if __name__ == '__main__':
    create_employee_form()

# Tutup koneksi ke database
conn.close()