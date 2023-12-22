import pandas as pd

# Buat dataset contoh dengan variasi
data = {
    'Nama': ['John Smith', 'Johny Doe', 'Mary Johnson', 'John Smith', 'Lisa Brown', 'James Wilson', 'Sarah Davis', 'Michael Lee',
             'Emily Davis', 'William Johnson', 'Sophia Smith', 'Ethan Doe', 'Olivia Wilson', 'Daniel Smith', 'Ava Davis', 'Logan Johnson',
             'Mia Wilson', 'Benjamin Smith','Mia Wilson', 'Benjamin Smith'],
    'Tanggal Lahir': ['01-12-1990', '05-03-1985', '10/20/1995', '2 Januari 1987', '15 Maret 1992', '20/05/1980', '12-08-1994', '10 Februari 1990',
                      '18-09-1982', '03-07-1991', '30/11/1988', '05 Januari 1993', '17 Mei 1997', '14-03-1989', '25/08/1992', '23 Februari 1985',
                      '01-07-1984', '08-11-1996','01-07-1984', '08-11-1996'],  
    'Hobi': ['Bulu tangkis, voli, nonton film', 'membaca, berenang', 'berenang', 'fotografi, hiking',
             'makan, berenang', 'membaca, berenang', 'fotografi', 'nonton film',
             'bersepeda, hiking', 'memancing, berenang', 'fotografi', 'bersepeda, hiking',
             'membaca, nonton film', 'memancing', 'bersepeda', 'fotografi, hiking',
             'makan, nonton film', 'memancing, berenang', 'bersepeda', 'bersepeda'],            
    'Alamat': [
        'Jl Kampus kembar Udayana No 112, Jimbaran Bali',
        'Kuta Selatan, Badung, Bali, Indonesia',
        'Jl. Gunung Agung No 25, Denpasar, DPS',
        'Jl. Diponegoro No 5, Jimbran, Bali',
        'Jalan Pantai Kuta No 10, Kuta, Bali',
        'Jl. Diponegoro No 15, Denpasar, DPS',
        'Jl. Gatot Subroto No 30, Jimbaran, Bali',
        'Jl. Sudirman No 8, Jimbran, Bali',
        'Jl. Raya Legian No 45, Kuta, Bali',
        'Jl. Hayam Wuruk No 3, Denpasar, DPS',
        'Jl. Pemuda No 17, Badung, Bali',
        'Jl. Pura Batu Pageh No 22, Jimbran, Bali',
        'Jl. Teuku Umar No 11, Denpasar, DPS',
        'Jl. Wana Segara No 6, Jimbaran, Bali',
        'Jl. Imam Bonjol No 32, Kuta, Bali',
        'Jl. Bypass Ngurah Rai No 18, Denpasar, DPS',
        'Jl. By Pass Ngurah Rai No 1, Jimbran, Bali',
        'Jl. Patih Jelantik No 23, Kuta, Bali',
        'Jl. Sunset Road No 10, Denpasar, DPS',
        'Jln. Sunset Road No 7, Jimbaran, Bali',
    ],
    'Nama Kota': ['Jimbaran', 'Denpasar', 'DPS', 'Jimbran', 'Kuta', 'Kuta', 'Jimbaran', 'Jimbran',
                   'Kuta', 'Denpasar', 'Badung', 'Jimbran', 'Denpasar', 'Jimbaran', 'Kuta', 'Denpasar',
                   'Jimbran', 'Kuta', 'Denpasar', 'Jimbaran'],
    
}

# Duplikat data untuk mencapai 50 data
data_list = [data] * 1000

# Gabungkan semua data
all_data = {key: sum((d[key] for d in data_list), []) for key in data_list[0]}

df = pd.DataFrame(all_data)

# Simpan dataset ke file CSV
df.to_csv('sample_dataset_cleansing.csv', index=False)
