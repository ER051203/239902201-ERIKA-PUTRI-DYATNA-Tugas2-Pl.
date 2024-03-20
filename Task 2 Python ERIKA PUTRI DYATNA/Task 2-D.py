print("---MENULIS NILAI ATAU ANGKA HINGGA -1---")

nilai = []
total = 0
jumlah = 0

while True:
  nilai_baru = int(input("Masukan Nilai (-1 = selesai memasukan nilai): "))
  if nilai_baru == -1:
    break

  nilai.append(nilai_baru)
  total += nilai_baru
  jumlah += 1

if jumlah == 0:
  print("Tidak ada nilai, silahkan masukan angka lain.")
else:
  rata_rata = int(total / jumlah)
  print(f"rata rata: {rata_rata}")
  print("Nilai:")
  for nilai in nilai:
    print(nilai)
