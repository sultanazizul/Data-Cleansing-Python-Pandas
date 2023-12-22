import pandas as pd
from sqlalchemy import create_engine


#EXTRACT
df = pd.read_csv("db_dosen.csv")

#LOAD
# Konfigurasi koneksi database
engine = create_engine('mysql+mysqlconnector://root@localhost/db_kepegawaian')

# Nama tabel dalam basis data SQL
nama_tabel = 'tb_dosen'

# Memuat ke tabel dalam basis data SQL
df.to_sql(nama_tabel, con=engine, if_exists='replace', index=False)


#- Library yang perlu di instal-
#pip install pandas
#pip install sqlalchemy
#pip install mysqlclient
