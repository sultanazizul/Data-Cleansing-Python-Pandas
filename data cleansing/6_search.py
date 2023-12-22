import pandas as pd
import PySimpleGUI as sg
import calendar

# Membaca dataset
df = pd.read_csv("hasil_formating_tanggal.csv")

# Fungsi pencarian data double berdasarkan nama
def search_by_name(nama_query):
    return df[df['Nama'].str.contains(nama_query, case=False)]

# Fungsi pencarian data double berdasarkan tanggal, bulan, dan tahun
def search_by_birthdate(tanggal_query, bulan_query, tahun_query):
    df_copy = df.copy()  # Buat salinan DataFrame untuk memastikan format tanggal tidak berubah
    df_copy['Tanggal Lahir'] = pd.to_datetime(df_copy['Tanggal Lahir'], errors='coerce')

    query_conditions = []

    if tanggal_query:
        query_conditions.append(df_copy['Tanggal Lahir'].dt.day == int(tanggal_query))

    if bulan_query:
        query_conditions.append(df_copy['Tanggal Lahir'].dt.month == int(bulan_query))

    if tahun_query:
        query_conditions.append(df_copy['Tanggal Lahir'].dt.year == int(tahun_query))

    if query_conditions:
        result_df = df_copy[query_conditions[0] if len(query_conditions) == 1 else (query_conditions[0] & query_conditions[1])]
        result_df['Tanggal Lahir'] = result_df['Tanggal Lahir'].dt.strftime('%d %b %Y')  # Format tanggal
        return result_df
    else:
        return pd.DataFrame()

# Layout GUI
layout = [
    [sg.Text('Cari Nama     :'), sg.InputText(key='NamaQuery', size=(42, 1))],
    [sg.Text('Tanggal Lahir :'), sg.Combo(values=[str(i).zfill(2) for i in range(1, 32)], key='TanggalQuery', size=(4, 1)),
     sg.Text(' Bulan :'), sg.Combo(values=[calendar.month_abbr[i] for i in range(1, 13)], key='BulanQuery', size=(4, 1)),
     sg.Text(' Tahun :'), sg.InputText(key='TahunQuery', size=(8, 1))],
    [ sg.Button('Cari Nama'), sg.Button('Cari Tanggal')],
    [ sg.Table(values=[], headings=df.columns.tolist(), auto_size_columns=False, justification='right', display_row_numbers=False, num_rows=10, key="TabelHasil")],
    [sg.Button('Simpan Hasil Pencarian ke CSV')],
]

# Create the window
window = sg.Window('Pencarian Data Double', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Cari Nama':
        nama_query = values['NamaQuery']
        hasil_pencarian = search_by_name(nama_query)
        window.Element("TabelHasil").Update(values=hasil_pencarian.values.tolist())
    elif event == 'Cari Tanggal':
        tanggal_query = values['TanggalQuery']
        bulan_query = str(list(calendar.month_abbr).index(values['BulanQuery'])) if values['BulanQuery'] else ''
        tahun_query = values['TahunQuery']
        hasil_pencarian = search_by_birthdate(tanggal_query, bulan_query, tahun_query)
        window.Element("TabelHasil").Update(values=hasil_pencarian.values.tolist())
    elif event == 'Simpan Hasil Pencarian ke CSV':
        if not hasil_pencarian.empty:
            hasil_pencarian.to_csv("hasil_pencarian.csv", index=False)
            sg.popup(f"Data berhasil disimpan di hasil_pencarian.csv")
        else:
            sg.popup("Tidak ada data untuk disimpan")

# Close the window
window.close()
