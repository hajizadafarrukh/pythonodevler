from random import randint


kelimeler = ["faruk","merhaba","selam","dunya","adana","istanbul","ankara","izmir","samsun"]
uzunluk = len(kelimeler)

def RandomKelimebul():
	random_no = randint(0,uzunluk)
	kelime1 = kelimeler[random_no]
	return kelime1	


def gamePlay(rastgele_kelime):
	sansiniz = 7
	is_found = False
	tahmin_edilen = []
	guess = ''
	print('	'+'_ '*len(rastgele_kelime)+'\n')
	while sansiniz>0:
		guess = input('Bir Harf yada Kelimeyi tahmin et: ')
		if guess==rastgele_kelime:
			is_found = True
		else:
			if guess in tahmin_edilen :
				print(f"Bu harfi zaten tahmin ettin {guess}..başka bir harf dene\n")
				continue
			print('	',end='')
			is_current_guess = False
			for letter in rastgele_kelime:
				if letter == guess :
					is_current_guess = True
					tahmin_edilen.append(letter)
					print(letter,end=' ')
					if len(rastgele_kelime) == len(tahmin_edilen):
						is_found = True
				elif letter in tahmin_edilen :
					print(letter,end=' ')
				else:
					print('_',end=' ')	
			print()		
		if is_found:
			print(f"Tebrikler!! Doğru Tahmin ettiniz!!, kelime '{rastgele_kelime}' idi \n")		
			break
		if not is_current_guess:
			print(f'{guess} harfi kelimede yok')
			sansiniz-=1
			print(f'Sizin {sansiniz} şansınız kaldı\n')

	if not is_found:
		print(f"\n Üzgünüm sizin tahmininiz yanlış, kelime '{rastgele_kelime}' idi\n")		


def main():
	print(" Kelime Bulmaca Oyunu".center(60,'-'))
	while True:
		random_word = RandomKelimebul()
		gamePlay(random_word)
		choice = input("Tekrar Oynamak İstermisiniz (evet/hayir) :")
		if choice in ['hayir','h','HAYİR','hayır','no']:
			break


if __name__ == '__main__':
	main()