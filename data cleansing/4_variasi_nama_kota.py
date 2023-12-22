import pandas as pd
import PySimpleGUI as sg

# Load dataset
df = pd.read_csv("pandas/dataset/sample_dataset_cleansing.csv")

# Load dataset referensi penulisan nama kota
df_mapping = pd.read_csv("mapping_nama_kota.csv")

# Mapping untuk menyejajarkan penulisan nama kota
nama_kota_mapping_lengkap = dict(zip(df_mapping['Nama Lengkap'], df_mapping['Singkatan']))
nama_kota_mapping_singkatan = dict(zip(df_mapping['Singkatan'], df_mapping['Nama Lengkap']))

# Fungsi untuk menyamakan penulisan nama kota
def seragamkan_nama_kota(nama_kota, tipe):
    if tipe == "Singkatan":
        return nama_kota_mapping_lengkap.get(nama_kota, nama_kota)
    elif tipe == "Lengkap":
        return nama_kota_mapping_singkatan.get(nama_kota, nama_kota)

# Fungsi untuk mengupdate tabel setelah combo box dipilih
def update_tabel(values, window):
    tipe_penulisan = values['Tipe']
    df_seragam = df.copy()
    df_seragam['Nama Kota'] = df_seragam['Nama Kota'].apply(lambda x: seragamkan_nama_kota(x, tipe_penulisan))
    window.Element("Tabel2").Update(values=df_seragam.values.tolist())

# Layout GUI
layout = [
    [sg.Text('Tabel Dataset Asli'), sg.Text(' '* 90), sg.Text('Tabel Hasil Setelah Seragamkan')],
    [sg.Table(values=df.values.tolist(), headings=df.columns.tolist(),
              auto_size_columns=False, justification='right',
              display_row_numbers=False, num_rows=min(25, len(df)), key="Tabel1"),
     sg.Table(values=df.values.tolist(), headings=df.columns.tolist(),
              auto_size_columns=False, justification='right',
              display_row_numbers=False, num_rows=min(25, len(df)), key="Tabel2")],
    [sg.Text('Pilih Tipe Penulisan Nama Kota:'),
     sg.Combo(values=["Singkatan", "Lengkap"], default_value="Singkatan", key="Tipe", enable_events=True)],
    [sg.Button('Simpan')],
]

# Create the window
window = sg.Window('Seragamkan Nama Kota', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Simpan':
        tipe_penulisan = values['Tipe']
        df_seragam = df.copy()
        df_seragam['Nama Kota'] = df_seragam['Nama Kota'].apply(lambda x: seragamkan_nama_kota(x, tipe_penulisan))
        df_seragam.to_csv(f"hasil_seragamkan_nama_kota_{tipe_penulisan.lower()}.csv", index=False)
        sg.popup(f"Data berhasil disimpan di hasil_seragamkan_nama_kota_{tipe_penulisan.lower()}.csv")
    elif event == 'Tipe':
        update_tabel(values, window)

# Close the window
window.close()
