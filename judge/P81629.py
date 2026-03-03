#Banknotes of 500 euros= 
#Banknotes of 200 euros= 
#Banknotes of 100 euros= 
#Banknotes of 50 euros= 
#Banknotes of 20 euros= 
#Banknotes of 10 euros= 
#Banknotes of 5 euros= 
#Coins of 2 euros= 
#Coins of 1 euro=
#Coins of 50 cents= 
#Coins of 20 cents= 
#Coins of 10 cents= 
#Coins of 5 cents= 
#Coins of 2 cents=
#Coins of 1 cents=

total_cents = e * 100 + c
Banknotes500euros=500000
Banknotes200euros= 20000
Banknotes100euros= 10000
Banknotes50euros= 5000
Banknotesof20euros= 2000
Banknotes10euros= 1000
Banknotes5euros= 500
Coins2euros= 200
Coins1euro=100
Coins50cents= 50
Coins20cents= 20
Coins10cents= 10
Coins5cents= 5
Coins2cents=2
Coins1cents=1



for value, name in denominations:
    count = total_cents // value
    print(f"{name}: {count}")
    total_cents -= count * value