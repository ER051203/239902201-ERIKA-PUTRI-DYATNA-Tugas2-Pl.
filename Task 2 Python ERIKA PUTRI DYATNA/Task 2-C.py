print ("---MENGHITUNG TINGGI DAN BERAT BADAN---")

berat_badan_kg = float(input("Weight :"))
tinggi_badan_meter = float(input("Height :"))

tinggi_badan_meter = tinggi_badan_meter/100     #rumus tinggi badan untuk satuan meter
BMI = (berat_badan_kg/(tinggi_badan_meter**2))

print(f"Jadi berat badan Anda : {berat_badan_kg} kg")
print(f"Jadi tinggi badan Anda : {tinggi_badan_meter} meter")






