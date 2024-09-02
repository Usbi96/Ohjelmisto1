# while silmukat
# ikuinen silmukka ei hyvä!!
'''while True:
    print("moro")
    print("Matti")
    '''
import random

counter = 0

'''while counter < 5:
    print(f"{counter}.hyvä")
    counter = counter + 1
print(f"laskurin arvo: {counter}")

Max_count = int(input("Monta kertaa kukutaan?"))
while counter < Max_count:
    counter = counter + 1
    print(f"{counter}.kukkuu")
print(f"laskurin arvo: {counter}")
'''

# ohjelma komentorivikäyttöliittymällä
'''command = ""
while command != "lopeta":
    command = input("Komento, kiitos> ")
    if command == "Lopeta":
        print("lopetetaan.")
        #break #"heittää ulos silmukasta, ei paras ohjelmointikäytäntö
    else:
        print("En ymmärrä komentoa, yritä uudestaan!")
print("Ohjelma on sammutettu.")
'''

#Noppapeli
rounds = 10000

round_counter = 0
total_rolls = 0
while round_counter < rounds:
    round_counter += 1
    die1 = die2 = roll_counter = 0
    while die1 < 6 or die2 < 6:
        roll_counter +=1
        die1 = random.randint (1,6)
        die2 = random.randint (1,6)
        print(f"{roll_counter},Nopan silmäluvut on: {die1} ja {die2}")
    print(f"noppaa heitettiin {roll_counter} kertaa")
    total_rolls = total_rolls + roll_counter
print(f"Kaksi kutosta saatiin keskimäärin {total_rolls / rounds} heitolla!")
