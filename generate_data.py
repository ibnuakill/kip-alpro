import csv
import random
import faker

# Initialize Faker library
fake = faker.Faker()

# Create sample data
def generate_sample_data(num_records):
    data = []
    for i in range(1, num_records + 1):
        nama = fake.name()
        nim = str(random.randint(10000000, 99999999))
        beasiswa = random.choice(['Ya', 'Tidak'])
        data.append({
            'id': i,
            'nama': nama,
            'nim': nim,
            'beasiswa': beasiswa
        })
    return data

# Save sample data to CSV file
def save_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['id', 'nama', 'nim', 'beasiswa']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for record in data:
            writer.writerow(record)

# Generate and save 100 sample records
sample_data = generate_sample_data(100)
save_to_csv('students.csv', sample_data)
