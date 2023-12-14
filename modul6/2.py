from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan pillow
img_path = r'D:\PRAK SMT 5\FUNGSIONAL\PRAK\FOTO\test.jpg'  # Ganti dengan path gambar Anda
image = Image.open(img_path)

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(1.2)

# TODO 3: Simpan gambar hasil edit
save_path = r'D:\PRAK SMT 5\FUNGSIONAL\PRAK\FOTO\hasil_edit.jpg'  # Ganti dengan path penyimpanan yang diinginkan
final_image.save(save_path)

# TODO 4: Tampilkan
final_image.show()
