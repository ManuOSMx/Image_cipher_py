from tkinter import *
from tkinter import filedialog
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

from PIL import Image
import numpy as np
import io

def obtenerModo(m):
	"""Función cuyo parámetro es la cadena de texto del modo y devuelve el modo en formato AES.MODE_XXX"""
	if m == "ECB": return AES.MODE_ECB
	elif m == "CBC": return AES.MODE_CBC
	elif m == "CFB": return AES.MODE_CFB
	elif m == "OFB": return AES.MODE_OFB
	else: return None


def cifrarECB(ubicacion, key, mode="",nonce=b"1234567890123456"):
	"""Función de descifrado requiere de la ubicación del archivo, la clave de 16 bytes, el modo de cifrado y el vector de inicialización (nonce, opcional para ECB)"""
	"""El vector de inicialización es 1234567890123456 por default si no se incluye en la llamada a la función"""
	# Abrir la imagen a cifrar, convertir para su cifrado y obteer su tamaño
	img = Image.open(ubicacion)
	imagen = np.array(img)
	size = img.size

	#Creación del cifrador según el modo
	if mode=="ECB":
		cipher = AES.new(key, obtenerModo(mode))
	elif mode=="CBC" or mode=="CFB" or mode=="OFB":
		cipher = AES.new(key, obtenerModo(mode), nonce)

	imgC = cipher.encrypt(pad(imagen.tobytes(),16))

	# Escribir nueva imagen cifrada
	cipherimage = Image.frombuffer("RGB", size, np.frombuffer(imgC))
	# Guardado del archivo cifrado con nuevo nombre
	cipherimage.save(ubicacion[:-4]+"_e"+mode+".bmp")


def descifrarECB(ubicacion, key, mode="", nonce=b"1234567890123456"):
	"""Función de descifrado requiere de la ubicación del archivo, la clave de 16 bytes, el modo de cifrado y el vector de inicialización (nonce, opcional para ECB)"""
	"""El vector de inicialización es 1234567890123456 por default si no se incluye en la llamada a la función"""
	# Abrir la imagen a cifrar, convertir para su descifrado y obtener su tamaño
	img = Image.open(ubicacion)
	imagen = np.array(img)
	size = img.size

	# Creación del cifrador según el modo
	if mode=="ECB":
		cipher = AES.new(key, obtenerModo(mode))
	elif mode=="CBC" or mode=="CFB" or mode=="OFB":
		cipher = AES.new(key, obtenerModo(mode), nonce)

	imgD = cipher.decrypt(imagen.tobytes())

	# Escribir nueva imagen descifrada
	plainimage = Image.frombuffer("RGB", size, np.frombuffer(imgD))
	# Guardado del archivo descrifrado con nuevo nombre
	plainimage.save(ubicacion[:-4]+"_d"+mode+".bmp")


# Llamadas a las funciones (solo ejemplo, hacer desde la interfaz con la clave y vector del usuario)
cifrarECB("Imagen1.bmp", b"sixteen byte key","ECB")
descifrarECB("Imagen1_eECB.bmp", b"sixteen byte key", "ECB")

cifrarECB("Imagen1.bmp", b"sixteen byte key","CFB", b"1234567890123456")
descifrarECB("Imagen1_eCFB.bmp", b"sixteen byte key", "CFB", b"1234567890123456")

cifrarECB("Imagen1.bmp", b"sixteen byte key","CBC", b"1234567890123456")
descifrarECB("Imagen1_eCBC.bmp", b"sixteen byte key", "CBC", b"1234567890123456")

cifrarECB("Imagen1.bmp", b"sixteen byte key","OFB", b"1234567890123456")
descifrarECB("Imagen1_eOFB.bmp", b"sixteen byte key", "OFB", b"1234567890123456")
