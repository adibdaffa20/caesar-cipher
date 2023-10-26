# Fungsi untuk mengenkripsi pesan menggunakan Caesar Cipher
def encrypt_caesar_cipher(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():  # Enkripsi hanya huruf alfabet
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        else:
            encrypted_char = char  # Biarkan karakter selain huruf tetap sama
        encrypted_text += encrypted_char
    return encrypted_text

# Fungsi untuk mendekripsi pesan yang dienkripsi dengan Caesar Cipher
def decrypt_caesar_cipher(cipher_text, shift):
    return encrypt_caesar_cipher(cipher_text, -shift)  # Mendekripsi dengan pergeseran negatif

# Menu utama
print("Selamat datang di Caesar Cipher!")
print("Pilih menu:")
print("1. Enkripsi")
print("2. Dekripsi")

# Membaca pilihan pengguna
menu_option = int(input("Pilihan (1/2): "))

if menu_option == 1:
    # Enkripsi
    plain_text = input("Masukkan pesan yang akan dienkripsi: ")
    shift = int(input("Masukkan jumlah pergeseran: "))
    encrypted_text = encrypt_caesar_cipher(plain_text, shift)
    print("Pesan Terenkripsi:", encrypted_text)
elif menu_option == 2:
    # Dekripsi
    cipher_text = input("Masukkan pesan yang akan didekripsi: ")
    shift = int(input("Masukkan jumlah pergeseran: "))
    decrypted_text = decrypt_caesar_cipher(cipher_text, shift)
    print("Pesan Terdekripsi:", decrypted_text)
else:
    print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
