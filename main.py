import tkinter as tk
from tkinter import ttk
import csv
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Load data from CSV file
def load_data(filename='students.csv'):
    students = []
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            students.append(row)
    return students

# Save data to CSV file
def save_data(students, filename='students.csv'):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['id', 'nama', 'nim', 'beasiswa']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

# Update beasiswa status
def update_beasiswa():
    selected_item = tree.focus()
    if selected_item:
        values = tree.item(selected_item, 'values')
        student_id = values[0]
        for student in students:
            if student['id'] == student_id:
                student['beasiswa'] = 'Ya' if student['beasiswa'] == 'Tidak' else 'Tidak'
                tree.item(selected_item, values=(student['id'], student['nama'], student['nim'], student['beasiswa']))
                save_data(students)
                break

# Filter data based on scholarship status
def filter_data():
    filter_status = filter_var.get()
    tree.delete(*tree.get_children())
    for student in students:
        if filter_status == "Semua" or student['beasiswa'] == filter_status:
            tree.insert('', tk.END, values=(student['id'], student['nama'], student['nim'], student['beasiswa']))

# Show or hide scholarship status column
def toggle_beasiswa_column():
    if show_var.get():
        tree['displaycolumns'] = columns
    else:
        tree['displaycolumns'] = ('id', 'nama', 'nim')

# Search data based on name or nim
def search_data():
    query = search_var.get().lower()
    tree.delete(*tree.get_children())
    for student in students:
        if query in student['nama'].lower() or query in student['nim'].lower():
            tree.insert('', tk.END, values=(student['id'], student['nama'], student['nim'], student['beasiswa']))

# Initialize the main window
root = tb.Window(themename="flatly")
root.title("Pendataan Calon Penerima Bantuan KIP")

# Create Treeview
columns = ('id', 'nama', 'nim', 'beasiswa')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('id', text='ID')
tree.heading('nama', text='Nama')
tree.heading('nim', text='NIM')
tree.heading('beasiswa', text='Beasiswa')
tree['displaycolumns'] = ('id', 'nama', 'nim')  # Hide the beasiswa column initially
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Load and insert data into Treeview
students = load_data()
for student in students:
    tree.insert('', tk.END, values=(student['id'], student['nama'], student['nim'], student['beasiswa']))

# Frame for filters and search
filter_search_frame = ttk.Frame(root)
filter_search_frame.pack(pady=10, padx=10, fill=tk.X)

# Filter options
filter_var = tk.StringVar(value="Semua")
filter_label = ttk.Label(filter_search_frame, text="Filter:")
filter_label.pack(side=tk.LEFT, padx=(0, 10))

filter_options = ["Semua", "Ya", "Tidak"]
filter_menu = ttk.Combobox(filter_search_frame, textvariable=filter_var, values=filter_options)
filter_menu.pack(side=tk.LEFT, padx=(0, 10))
filter_button = ttk.Button(filter_search_frame, text="Apply Filter", command=filter_data)
filter_button.pack(side=tk.LEFT, padx=(0, 10))

# Search bar
search_var = tk.StringVar()
search_label = ttk.Label(filter_search_frame, text="Search:")
search_label.pack(side=tk.LEFT, padx=(30, 10))

search_entry = ttk.Entry(filter_search_frame, textvariable=search_var)
search_entry.pack(side=tk.LEFT, padx=(0, 10))

search_button = ttk.Button(filter_search_frame, text="Search", command=search_data)
search_button.pack(side=tk.LEFT, padx=(0, 10))

# Show/Hide scholarship status column
show_var = tk.BooleanVar()
show_check = ttk.Checkbutton(root, text="Show Beasiswa Column", variable=show_var, command=toggle_beasiswa_column)
show_check.pack(pady=(10, 10))

# Add Update Button
update_button = ttk.Button(root, text="Update Beasiswa", command=update_beasiswa)
update_button.pack(pady=(0, 10))

# Run the application
root.mainloop()
