total_tabungan = 0

nominal = int(input("Masukkan nominal tabungan (0 untuk berhenti): "))
while nominal != 0:
    total_tabungan = total_tabungan + nominal
    nominal = int(input("Masukkan nominal tabungan (0 untuk berhenti): "))

    print("Total tabungan saat ini: ", total_tabungan)