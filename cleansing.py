import pandas as pd
import re

#Extract
df = pd.read_csv("dataset/sample_dataset_cleansing.csv")

#Transform
# 1. Menyeragamkan variasi format tanggal
# Fungsi untuk mengubah format tanggal
def ubah_format_tanggal(tanggal):
    try:
        # Menggunakan ekspresi reguler untuk mengenali format 'DD Bulan YYYY'
        match = re.match(r'(\d{1,2})\s(Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember)\s(\d{4})', tanggal)
        if match:
            day, month, year = match.groups()
            month_dict = {
                'Januari': '01',
                'Februari': '02',
                'Maret': '03',
                'April': '04',
                'Mei': '05',
                'Juni': '06',
                'Juli': '07',
                'Agustus': '08',
                'September': '09',
                'Oktober': '10',
                'November': '11',
                'Desember': '12'
            }
            return f'{day}/{month_dict[month]}/{year}'
        else:
            return pd.to_datetime(tanggal, errors='coerce').strftime('%d/%m/%Y')
    except:
        return tanggal

# Terapkan fungsi pada kolom 'Tanggal Lahir'
df['Tanggal Lahir'] = df['Tanggal Lahir'].apply(ubah_format_tanggal)


# 4. Menyeragamkan variasi nama kota
# Kamus pemetaan variasi nama kota
pemetaan_kota = {
    'Jimbran': 'Jimbaran',
    'DPS': 'Denpasar',
    'dps': 'Denpasar',
}

def seragamkan_kota(nama_kota): # Fungsi untuk menyamakan nama kota
    return pemetaan_kota.get(nama_kota, nama_kota)

df['Nama Kota'] = df['Nama Kota'].apply(seragamkan_kota) # Terapkan fungsi pada kolom 'Nama Kota'

 
# 5. Memisahkan data multiple dalam kolom 'Hobi' menjadi beberapa baris
df['Hobi'] = df['Hobi'].str.split(', ')  # Membagi hobi berdasarkan koma
df = df.explode('Hobi')  # Memisahkan data multiple menjadi baris terpisah


# Load
df.to_csv('data_hasil_cleansing.csv', index=False)



# # 3. Menyeragamkan variasi nama kota
# # Fungsi untuk mengupdate kode pos dan kode kecamatan dari alamat
# def update_kode_pos_kecamatan(alamat):
#     kode_pos = None
#     kode_kecamatan = None

#     # Menggunakan ekspresi reguler untuk mencocokkan kode pos dalam alamat
#     kode_pos_match = re.search(r'(\d{5})', alamat)
#     if kode_pos_match:
#         kode_pos = int(kode_pos_match.group(1))

#     # Menggunakan ekspresi reguler untuk mencocokkan kode kecamatan dalam alamat
#     kode_kecamatan_match = re.search(r',\s(.*?)\sBali', alamat)
#     if kode_kecamatan_match:
#         kode_kecamatan = kode_kecamatan_match.group(1)

#     return kode_pos, kode_kecamatan

# # Terapkan fungsi pada kolom 'Alamat' untuk mengupdate kolom 'Kode Pos' dan 'Kode Kecamatan'
# df['Kode Pos'], df['Kode Kecamatan'] = zip(*df['Alamat'].apply(update_kode_pos_kecamatan))