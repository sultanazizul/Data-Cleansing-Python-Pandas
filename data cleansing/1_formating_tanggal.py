import pandas as pd
import PySimpleGUI as sg
from dateutil import parser

# Fungsi untuk mengubah format tanggal
def ubah_format_tanggal(tanggal, format_tanggal):
    try:
        # Cek apakah tanggal memiliki format nama bulan
        is_nama_bulan = any(bulan.lower() in tanggal.lower() for bulan in df_bulan['NamaBulan'])

        if is_nama_bulan:
            # Jika tanggal memiliki format nama bulan, konversi nama bulan ke angka
            tanggal = ' '.join(str(konversi_nama_bulan(bulan)) for bulan in tanggal.split())

        tanggal_obj = parser.parse(tanggal)

        if format_tanggal.lower() == 'dd/mm/yyyy':
            return tanggal_obj.strftime('%d/%m/%Y')
        elif format_tanggal.lower() == 'dd-mm-yyyy':
            return tanggal_obj.strftime('%d-%m-%Y')
        elif format_tanggal.lower() == 'mm/dd/yyyy':
            return tanggal_obj.strftime('%m/%d/%Y')
        elif format_tanggal.lower() == 'yyyy-mm-dd':
            return tanggal_obj.strftime('%Y-%m-%d')
        elif format_tanggal.lower() == 'yyyy/mm/dd':
            return tanggal_obj.strftime('%Y/%m/%d')
        elif format_tanggal.lower() == 'dd.mm.yyyy':
            return tanggal_obj.strftime('%d.%m.%Y')
        elif format_tanggal.lower() == 'yyyy.mm.dd':
            return tanggal_obj.strftime('%Y.%m.%d')
        elif format_tanggal.lower() == 'dd-mm-yyyy':
            return tanggal_obj.strftime('%d-%m-%Y')
        elif format_tanggal.lower() == 'dd/mm/yy':
            return tanggal_obj.strftime('%d/%m/%y')
        elif format_tanggal.lower() == 'yy/mm/dd':
            return tanggal_obj.strftime('%y/%m/%d')
        elif format_tanggal.lower() == 'dd mon yyyy':
            return tanggal_obj.strftime('%d %b %Y')
        elif format_tanggal.lower() == 'mon dd, yyyy':
            return tanggal_obj.strftime('%b %d, %Y')
        elif format_tanggal.lower() == 'month dd, yyyy':
            return tanggal_obj.strftime('%B, %d, %Y')
        else:
            return tanggal_obj.strftime(format_tanggal)
    except ValueError:
        return tanggal  # Kembalikan tanggal asli jika tidak dapat diubah

# Fungsi untuk konversi nama bulan ke dalam angka
def konversi_nama_bulan(nama_bulan):
    bulan_dict = dict(zip(df_bulan['NamaBulan'], df_bulan['AngkaBulan']))
    return str(bulan_dict.get(nama_bulan.lower(), nama_bulan))


# Fungsi untuk membersihkan data dan mengubah format tanggal
def cleansing_data(file_path, format_tanggal):
    df = pd.read_csv("pandas/dataset/sample_dataset_cleansing.csv")

    # Ubah format tanggal pada kolom "Tanggal Lahir"
    df["Tanggal Lahir"] = df["Tanggal Lahir"].apply(lambda x: ubah_format_tanggal(x, format_tanggal)
                                                     if pd.notnull(x) else x)

    return df

# Fungsi untuk menampilkan tabel dan GUI
def tampilkan_GUI(dataframe):
    layout = [
        [sg.Text(f"Jumlah Baris Data: {len(dataframe)}", key="JumlahBaris")],
        [sg.Table(values=dataframe.values.tolist(), headings=dataframe.columns.tolist(),
                  auto_size_columns=False, justification='right',
                  display_row_numbers=False, num_rows=min(25, len(dataframe)), key="Tabel")],
        [sg.Text("Pilih Format Tanggal:"),
         sg.Combo(values=["MM/DD/YYYY", "YYYY/MM/DD", "DD/MM/YYYY", "YYYY-MM-DD", "DD.MM.YYYY",
                          "YYYY.MM.DD", "DD-MM-YYYY", "DD/MM/YY", "YY/MM/DD", "DD Mon YYYY", "Mon DD, YYYY", "Month DD, YYYY"],
                  default_value="MM/DD/YYYY", key="FormatTanggal", enable_events=True)],
        [sg.Button("Simpan Data")],
    ]

    window = sg.Window('Formating Tanggal').Layout(layout)

    while True:
        event, values = window.Read()

        if event is None or event == 'Exit':
            break
        elif event == 'Simpan Data':
            format_tanggal = values["FormatTanggal"]
            df_cleansed = cleansing_data("pandas/dataset/sample_dataset_cleansing.csv", format_tanggal)
            window.Element("Tabel").Update(values=df_cleansed.values.tolist())
            window.Element("JumlahBaris").Update(f"Jumlah Baris Data: {len(df_cleansed)}")

            # Simpan data ke dalam file hasil_formating_tanggal.csv
            df_cleansed.to_csv("hasil_formating_tanggal.csv", index=False)

            sg.Popup("Data berhasil disimpan di hasil_formating_tanggal.csv")

        elif event == 'FormatTanggal':
            format_tanggal = values["FormatTanggal"]
            df_cleansed = cleansing_data("pandas/dataset/sample_dataset_cleansing.csv", format_tanggal)
            window.Element("Tabel").Update(values=df_cleansed.values.tolist())
            window.Element("JumlahBaris").Update(f"Jumlah Baris Data: {len(df_cleansed)}")

    window.Close()

if __name__ == '__main__':
    # Load dataset nama bulan
    df_bulan = pd.read_csv("pandas/data cleansing/nama_bulan.csv")
    df_awal = pd.read_csv("pandas/dataset/sample_dataset_cleansing.csv")
    tampilkan_GUI(df_awal)
