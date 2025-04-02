bank_krtasi=(input("karta raqamini kiriting:"))
pinkod=(input("pinkodni kiriting:"))
bank_acauntlar= { "1234567890":{"pin":"2005","balanc": 10000},
"123412345":{"pin":"1234","balanc":23000}
}
while True :
	if bank_krtasi in bank_acauntlar and pinkod ==bank_acauntlar[bank_krtasi]["pin"]:
		pul_yechish=int(input("miqdorni kiriting:"))
		if pul_yechish<=bank_acauntlar[bank_krtasi]["balanc"]:
			bank_acauntlar[bank_krtasi]["balanc"]-=  pul_yechish
			yangi_balanc=bank_acauntlar[bank_krtasi]["balanc"]
			print("\n====== CHEK ======")
			print("Karta raqami: {}".format(bank_krtasi))
			print("Yechilgan summa: {} so‘m".format(pul_yechish))
			print("Yangi balans: {} so‘m".format(yangi_balanc))
			print("====================\n")
		else:
			print("balansingizda pul yetarli emas!")
	else:
		print("pin kod yoki karta raqam xato")
	break

