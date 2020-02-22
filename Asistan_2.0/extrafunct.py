import time
from gtts import gTTS
import random
from playsound import playsound
from variables import *
#Brand Text
def brand():

    print("    _    ____ ___ ____ _____  _    _   _ ")
    print("   / \  / ___|_ _/ ___|_   _|/ \  | \ | |")
    print("  / _ \ \___ \| |\___ \ | | / _ \ |  \| |")
    print(" / ___ \ ___) | | ___) || |/ ___ \| |\  |")
    print("/_/   \_\____/___|____/ |_/_/   \_\_| \_|  2.0 \n\n")


# Author Info

def authorinf():

	print("\nEnes Kasapoğlu")
	time.sleep(3)
	print("https://kilavuzkod.blogspot.com\n")

def dizi():

	number = random.randint(1,10)

	if(number == 1):

		request = ("Sana Black Mirror Dizisini öneriyorum.")
		print("Sana Black Mirror Dizisini Öneriyorum")
		tts = gTTS(text = request, lang="tr")
		tts.save("speakeraudio.mp3")
		playsound('speakeraudio.mp3')

	elif(number == 2):
		request = ("Sana The 100 dizisini öneriyorum")
		print("Sana The 100 Dizisini Öneriyorum")
		tts = gTTS(text = request,lang = "tr")
		tts.save("speakeraudio.mp3")
		playsound('speakeraudio.mp3')

	elif(number == 3):
		request = ("Sana Rick and Morty dizisini öneriyorum.")
		print("Sana Rick and Morty Dizisini Öneriyorum.")
		tts = gTTS(text = request, lang = "tr")
		tts.save("speakeraudio.mp3")
		playsound('speakeraudio.mp3')

	elif(number == 4):
		request = ("Sana Stranger Things dizisini öneriyorum")
		print("Sana Stranger Things Dizisini Öneriyorum")
		tts = gTTS(text = request,lang = "tr")
		tts.save("speakeraudio.mp3")
		playsound('speakeraudio.mp3')

	elif(number == 5):
		request = ("Sana Breaking Bad dizisini öneriyorum")
		print("Sana Breaking Breaking Dizisini Öneriyorum")
		tts = gTTS(text = request,lang = "tr")
		tts.save("speakeraudio.mp3")
		playsound('speakeraudio.mp3')

	elif(number == 6):
		request = ("Sana La Casa De Papel dizisini öneriyorum")
		print("Sana La Casa De Papel Dizisini Öneriyorum")
		tts = gTTS(text = request,lang = "tr")
		tts.save("speakeraudio.mp3")
		playsound('speakeraudio.mp3')

	elif(number == 7):
		request = ("Sana Game of Thrones dizisini öneriyorum")
		print("Sana Game of Thrones Dizisini Öneriyorum")
		tts = gTTS(text = request,lang = "tr")
		tts.save("speakeraudio.mp3")
		playsound('speakeraudio.mp3')	

	elif(number == 8):
		request = ("Sana Sherlock dizisini öneriyorum")
		print("Sana Sherlock Dizisini Öneriyorum")
		tts = gTTS(text = request,lang = "tr")
		tts.save("speakeraudio.mp3")
		playsound('speakeraudio.mp3')

	elif(number == 9):
		request = ("Sana Simpsons dizisini öneriyorum")
		print("Sana Simpsons Dizisini Öneriyorum")
		tts = gTTS(text = request,lang = "tr")
		tts.save("speakeraudio.mp3")
		playsound('speakeraudio.mp3')

	elif(number == 10):
		request = ("Sana The Walking dead dizisini öneriyorum")
		print("Sana The Walking Dead Dizisini Öneriyorum")
		tts = gTTS(text = request,lang = "tr")
		tts.save("speakeraudio.mp3")
		playsound('speakeraudio.mp3')

def kitap():

	readnumber = random.randint(1,10)

	if(readnumber == 1):
		print(kitapone)
	elif(readnumber == 2):
		print(kitaptwo)
	elif(readnumber == 3):
		print(kitapthree)
	elif(readnumber == 4):
		print(kitapfour)
	elif(readnumber == 5):
		print(kitapfive)
	elif(readnumber == 6):
		print(kitapsix)
	elif(readnumber == 7):
		print(kitapseven)
	elif(readnumber == 8):
		print(kitapeight)
	elif(readnumber == 9):
		print(kitapnine)
	elif(readnumber == 10):
		print(kitapten) 

