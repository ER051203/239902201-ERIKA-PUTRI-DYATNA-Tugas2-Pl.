print ("---MENCETAK ANGKA TANGGAL JUMLAH HARI DARI SEKARANG---") 
import datetime 

hari_ini = datetime.date.today()
print(f"Hari = {hari_ini: %A}")
print(f"Bulan = {hari_ini: %B}")
print(f"Tahun = {hari_ini: %G}")
print ("Hari ini tanggal : ",hari_ini)
