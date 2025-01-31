import qrcode
import json
import os
import re

# 1. Baca file JSON yang berisi data
file_path = "./txt/pkn11.txt"  # Ganti dengan path file yang benar

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# 2. Ekstrak semua _id dari data
ids = [item["_id"] for item in data["data"]]

# 3. Buat folder penyimpanan jika belum ada
output_dir = "qrcodes"
os.makedirs(output_dir, exist_ok=True)

# 4. Mencari nomor terakhir dari file yang sudah ada
existing_files = [f for f in os.listdir(output_dir) if re.match(r"qr_(\d+)\.png", f)]
existing_numbers = [int(re.search(r"qr_(\d+)\.png", f).group(1)) for f in existing_files]

if existing_numbers:
    start_index = max(existing_numbers) + 1  # Melanjutkan dari nomor terakhir
else:
    start_index = 1  # Jika belum ada file, mulai dari 1

# 5. Loop untuk membuat dan menyimpan QR Code dengan nama yang berurutan
for i, id_value in enumerate(ids, start=start_index):
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=10,  
        border=4,  
    )
    qr.add_data(id_value)
    qr.make(fit=True)

    # Buat gambar QR Code
    img = qr.make_image(fill="black", back_color="white")

    # Simpan gambar dengan nama unik
    qr_filename = os.path.join(output_dir, f"qr_{i}.png")
    img.save(qr_filename)

print(f"QR Codes berhasil dibuat dan disimpan di folder '{output_dir}', dimulai dari qr_{start_index}.png")
