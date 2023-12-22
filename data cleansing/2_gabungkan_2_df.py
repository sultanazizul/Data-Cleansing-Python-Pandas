import pandas as pd
import PySimpleGUI as sg

# Load dataset

df2 = pd.read_csv("pandas/dataset/sample_dataset_cleansing.csv")
df1 = pd.read_csv("pandas/data cleansing/hasil_formating_tanggal.csv")

# Initial display with Union
selected_variasi = "Union"
df_result = pd.concat([df1, df2]).drop_duplicates().reset_index(drop=True)

# Layout GUI
layout = [
    [sg.Text('Tabel Dataset 1'), sg.Text(' ' * 92), sg.Text('Tabel Dataset 2')],
    [sg.Table(values=df1.values.tolist(), headings=df1.columns.tolist(),
              auto_size_columns=False, justification='left',
              display_row_numbers=False, num_rows=min(10, len(df1)), key="Tabel1"),
     sg.Table(values=df2.values.tolist(), headings=df2.columns.tolist(),
              auto_size_columns=False, justification='left',
              display_row_numbers=False, num_rows=min(10, len(df2)), key="Tabel2")],
    [sg.Text('Pilih Variasi:'),
     sg.Combo(values=["Union", "Concat", "Merge", "Intersection"],
              default_value=selected_variasi, key="Variasi", enable_events=True)],
    [sg.Text('Tabel Hasil')],
    [sg.Table(values=df_result.values.tolist(), headings=df_result.columns.tolist(),
              auto_size_columns=False, justification='left',
              display_row_numbers=False, num_rows=min(25, len(df_result)), key="Tabel3")],
    [sg.Button('Simpan')],
]

# Create the window
window = sg.Window('Penggabungan 2 Tabel', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Simpan':
        if selected_variasi == "Union":
            df_result.to_csv("hasil_variasi_union.csv", index=False)
        elif selected_variasi == "Concat":
            df_result.to_csv("hasil_variasi_concat.csv", index=False)
        elif selected_variasi == "Merge":
            df_result.to_csv("hasil_variasi_merge.csv", index=False)
        elif selected_variasi == "Intersection":
            df_result.to_csv("hasil_variasi_intersection.csv", index=False)

        sg.popup(f"Data berhasil disimpan di hasil_variasi_{selected_variasi.lower()}.csv")

    elif event == 'Variasi':
        selected_variasi = values['Variasi']
        if selected_variasi == "Union":
            df_result = pd.concat([df1, df2]).drop_duplicates().reset_index(drop=True)
        elif selected_variasi == "Concat":
            df_result = pd.concat([df1, df2], ignore_index=True)
        elif selected_variasi == "Merge":
            df_result = pd.merge(df1, df2, how='outer', indicator=True).query('_merge=="left_only"').drop('_merge', axis=1)
        elif selected_variasi == "Intersection":
            df_result = pd.merge(df1, df2, how='inner', on=df1.columns.tolist())

        window.Element("Tabel3").Update(values=df_result.values.tolist())

# Close the window
window.close()
