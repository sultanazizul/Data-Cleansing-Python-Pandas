import pandas as pd

#Extract
df = pd.read_excel("/Users/sultanazizul/Documents/karyawan.xlsx")
# print(df)

#Transform
#menggabungkan kolom
df['full_name']= df['nama_awal']+' '+ df['nama_akhir']

# Menambahkan kolom bonus berdasarkan gaji (misalnya, 10% bonus)
#df['bonus'] = df['gaji'] * 0.1

# menghapusan kolom 'nama_awal' dan 'nama_akhir'
df = df.drop(['nama_awal', 'nama_akhir'], axis=1)

print(df)

# Load
df.to_csv('data_hasil_etl.csv', index=False)






# Menghitung pajak gaji (misalnya, 10% dari gaji)
# df['pajak'] = 0.1 * df['gaji']

# Menambahkan kolom status karyawan berdasarkan gaji (misalnya, "Kaya" jika gaji di atas 5 juta, "Miskin" jika di bawah 5 juta)
# df['status_karyawan'] = df['gaji'].apply(lambda x: 'Kaya' if x > 5000000 else 'Miskin')

# Mengelompokkan karyawan berdasarkan status karyawan
# status_group = df.groupby('status_karyawan')
# status_group_mean = status_group.mean()

# Mengurutkan karyawan berdasarkan gaji secara menurun
# df = df.sort_values(by='gaji', ascending=False)

# engine=sa.create_engine('mysql+pyodbc://10/db_dwh?driver=SQL+Server+Native+Client+8.1.0 ')
# df.to_sql(name="Tabelname", con=engine, index = False, if_exists='fail|replace|append')