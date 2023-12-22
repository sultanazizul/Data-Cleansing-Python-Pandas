import pandas as pd
from faker import Faker
import random

def generate_random_data_alumni(num_records):
    fake = Faker('id_ID')  # Pengaturan untuk bahasa Indonesia

    data = {
        'NIP': [fake.unique.random_number(digits=8, fix_len=True) for _ in range(num_records)],
        'Nama Pegawai': [fake.name() for _ in range(num_records)],
        'Alamat': [fake.address() for _ in range(num_records)],
        'Kode Pos': [fake.postcode() for _ in range(num_records)],
        'Tanggal Lahir': [fake.date_of_birth(minimum_age=22, maximum_age=30).strftime('%Y-%m-%d') for _ in range(num_records)],
        'Email': [fake.email() for _ in range(num_records)],
        'Golongan Darah': [random.choice(['A', 'B', 'AB', 'O']) for _ in range(num_records)],
    }

    return data

jumlah_data_dosen= 100

df_alumni = pd.DataFrame(generate_random_data_alumni(jumlah_data_dosen))

df_alumni.to_csv('db_pegawai.csv', index=False)

print(df_alumni.head())
