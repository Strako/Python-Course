from cryptography.fernet import Fernet

# Generar una clave de encriptación
clave = Fernet.generate_key()
cipher_suite = Fernet(clave)

# Texto a encriptar
texto_original = "Este es un mensaje secreto."

# Encriptar el texto
texto_encriptado = cipher_suite.encrypt(texto_original.encode())

print("Texto encriptado:", texto_encriptado)

# Desencriptar el texto
texto_desencriptado = cipher_suite.decrypt(texto_encriptado).decode()
print("Texto desencriptado:", texto_desencriptado)