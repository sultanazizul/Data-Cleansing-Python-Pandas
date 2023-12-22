import pandas as pd
import PySimpleGUI as sg

# Membaca dataset
df_original = pd.read_csv("pandas/dataset/sample_dataset_cleansing.csv")

# Membaca dataset master hobi
df_master_hobi = pd.read_csv("data_hobi.csv")

# Membuat kolom 'Hobi' yang di-split dan di-stack
df_cleansed = df_original.copy()
df_cleansed['Hobi'] = df_cleansed['Hobi'].str.split(', ')
df_cleansed = df_cleansed.explode('Hobi')

# Menggabungkan dengan dataset master hobi untuk mendapatkan id_hobi
df_cleansed = pd.merge(df_cleansed, df_master_hobi, how='left', left_on='Hobi', right_on='nama_hobi')

# Menghapus kolom 'nama_hobi' karena sudah tidak diperlukan
df_cleansed = df_cleansed.drop('nama_hobi', axis=1)

# Layout GUI
layout = [
    [sg.Text('Sebelum')],
    [sg.Table(values=df_original.values.tolist(), headings=df_original.columns.tolist(),
              auto_size_columns=False, justification='left',
              display_row_numbers=False, num_rows=min(10, len(df_original)), key="TabelOriginal")],
    [sg.Text('Sesudah')],
    [sg.Table(values=df_cleansed.values.tolist(), headings=df_cleansed.columns.tolist(),
              auto_size_columns=False, justification='left',
              display_row_numbers=False, num_rows=min(10, len(df_cleansed)), key="TabelCleansed")],
    [sg.Button('Simpan')],
]

# Create the window
window = sg.Window('Memisahkan Multiple Data', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Simpan':
        df_cleansed.to_csv("hasil_cleansing_hobi.csv", index=False)
        sg.popup(f"Data berhasil disimpan di hasil_cleansing_hobi.csv")

# Close the window
window.close()

