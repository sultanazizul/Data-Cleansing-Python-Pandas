import PySimpleGUI as sg
import pandas as pd
import json
import timeit

# Fungsi untuk query menggunakan tipe data array (JSON)
def query_json():
    # Membaca data dari file JSON
    with open("data_saham.json", "r") as json_file:
        data = json_file.read()

    # Melakukan query
    result = pd.read_json(data)
    return result

# Fungsi untuk query menggunakan tipe data tabular
def query_tabular():
    # Membaca data dari file Excel
    df = pd.read_excel("data_saham.xlsx")
    return df

# Fungsi untuk menampilkan tabel hasil query
def display_table(data, key):
    layout_table = [
        [sg.Table(values=data.values.tolist(), headings=data.columns.tolist(),
                  auto_size_columns=False, justification='right',
                  display_row_numbers=False, num_rows=min(25, len(data)), key=key)]
    ]
    return sg.Window('Hasil Query', layout_table)

# Layout GUI utama
layout = [
    [sg.Button('Query JSON'), sg.Button('Query Tabular')],
    [sg.Button('Mulai Uji Coba', key='MulaiUjiCoba')],
]

# Create the window
window = sg.Window('Uji Kecepatan Query', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Query JSON':
        result_json = query_json()
        window_json = display_table(result_json, 'TabelHasilJson')
        event, values = window_json.read()
        window_json.close()
    elif event == 'Query Tabular':
        result_tabular = query_tabular()
        window_tabular = display_table(result_tabular, 'TabelHasilTabular')
        event, values = window_tabular.read()
        window_tabular.close()
    elif event == 'Mulai Uji Coba':
        time_json = timeit.timeit(query_json, number=1)
        time_tabular = timeit.timeit(query_tabular, number=1)
        sg.popup_non_blocking(f'Waktu eksekusi query JSON: {time_json:.4f} detik\nWaktu eksekusi query tabular: {time_tabular:.4f} detik')

window.close()
