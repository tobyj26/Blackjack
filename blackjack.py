import random, time
seccard_value = 0
turns = 1
dealercont = False
dealstand = False
dealtotal = 0


print("\n Welcome to Blackjack!\n ")
time.sleep(2)
print("\n the goal is to get closest to 21 without going over!\n ")
time.sleep(2)

print("\n Dealing first card...\n")
time.sleep(2)

lstcards = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
random.shuffle(lstcards)

fircard = lstcards[0]

print(f"\n You were dealt a {fircard}\n")
time.sleep(2)

if fircard == "King":
    print(f"{fircard} is worth 10 \n")
    total = 10
    time.sleep(2)

elif fircard == "Jack":
    print(f"{fircard} is worth 10 \n")
    total = 10
    time.sleep(2)


elif fircard == "Queen":
    print(f"{fircard} is worth 10 \n")
    total = 10
    time.sleep(2)


elif fircard == "Ace":
    print(f"{fircard} is worth either 1 or 11 \n")
    acechoice = int(input("Choose its value (1 or 11): "))
    total = acechoice
    time.sleep(2)

else:
    total = int(fircard)
    print(f"{fircard} is worth its face value")
    time.sleep(2)


print(f"\n After the first deal your cards total to {total}\n ")

time.sleep(2)

#DEALER ROLL

print("\n Dealer dealing...\n")
time.sleep(2)

lstcards = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
random.shuffle(lstcards)

fircard = lstcards[0]

print(f"\n Dealer was dealt a {fircard}\n")
time.sleep(2)

if fircard == "King":
    print("Dealer has 10 \n")
    dealtotal = 10
    time.sleep(2)

elif fircard == "Jack":
    print("Dealer has 10 \n")
    dealtotal = 10
    time.sleep(2)


elif fircard == "Queen":
    print("Dealer has 10 \n")
    dealtotal = 10
    time.sleep(2)


elif fircard == "Ace":
    print("Dealer has 11")
    time.sleep(2)

else:
    dealtotal = int(fircard)
    print(f"Dealer has {fircard}")
    time.sleep(2)


print(f"\n After the first deal your cards total to {total} and the dealers to total to {dealtotal}\n ")
time.sleep(2)


while True:
  secchoice = input("Would you like to hit or stand: ")

  if secchoice == "hit":
    hit = True
    turns += 1
  else:
    hit = False



  # second deal

  if hit:

    print(f"\n Dealing for turn {turns}...\n")
    time.sleep(2)

    lstcards = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    random.shuffle(lstcards)

    seccard = lstcards[0]


    print(f"\n You were dealt a {seccard}\n")
    time.sleep(2)


    if seccard == "King":
      print(f"{seccard} is worth 10 \n")
      seccard_value = 10
      time.sleep(2)

    elif seccard == "Jack":
      print(f"{seccard} is worth 10 \n")
      seccard_value = 10
      time.sleep(2)


    elif seccard == "Queen":
      print(f"{seccard} is worth 10 \n")
      seccard_value = 10
      time.sleep(2)


    elif seccard == "Ace":
      print(f"{seccard} is worth either 1 or 11 \n")
      acechoice = int(input("Choose its value (1 or 11): "))
      seccard_value = acechoice
      time.sleep(2)

    else:
      seccard_value = int(seccard)
      print(f"{seccard} is worth its face value")
      time.sleep(2)

    total += seccard_value

    print(f"\n After the second deal your cards total to {total} \n ")

  elif secchoice == "stand":
    print(f"\n Standing, you ended with the total of {total}\n ")
    time.sleep(2)
    dealercont = True

  elif secchoice != "hit" or "stand":
    print("Only enter hit or stand!")
    time.sleep(2)
    continue
  
  if total == 21 and dealtotal == 21:
     print("tie, you both got 21!")
     exit()

  elif total == 21 and dealtotal != 21:
     print("BLACKJACK!! You win!")
     exit()

  if total > 21:
     print(f"Busted! You lost! Dealer won with {dealtotal}")
     exit()

  elif dealercont == True:
     print(f"\n Dealers turn!\n")
     time.sleep(1)

 
 
 
 
  while dealercont == True:
    
    
    print("\n Dealing for dealer...\n")
    time.sleep(2)

    lstcards = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    random.shuffle(lstcards)

    fircard = lstcards[0]

    print(f"\n Dealer was dealt a {fircard}\n")
    time.sleep(2)

    if fircard == "King":
      print("Dealer has 10 \n")
      dealtotal += 10
      time.sleep(2)

    elif fircard == "Jack":
      print("Dealer has 10 \n")
      dealtotal += 10
      time.sleep(2)


    elif fircard == "Queen":
      print("Dealer has 10 \n")
      dealtotal += 10
      time.sleep(2)


    elif fircard == "Ace": 

      if dealtotal + 11 <= 21:                                                                                                                                                                       
        print("Dealer has 11")
        time.sleep(2)
        dealtotal += 11
      else:
         print("Dealer has 1")
         dealtotal += 1
         time.sleep(2)




    else:
      print(f"\n Dealer has {fircard} \n")
      dealtotal += int(fircard)
      time.sleep(2)

    print(f"\n Dealer total is {dealtotal}\n")
    time.sleep(2)

    if dealtotal > 21:
      print("\n Dealer busts, you win!\n ")
      exit()
    if dealtotal == 21:
       print("\n Dealer has Blackjack!!\n")
       continue

    if dealtotal < 17:
      print(f"\n Dealer hits on {dealtotal}...\n")
      time.sleep(2)
      continue

    elif dealtotal >= 17:
       print(f"\n Dealer always stands on {dealtotal}")
       dealstand = True
       dealercont = False
       continue
  
  
  if dealstand:
    if total > dealtotal:
        print("\n You win!\n")
        exit()

    elif total < dealtotal:
        print("\n Dealer wins!\n")
        exit()

    elif total == dealtotal:
        print("\n Draw!\n")
        exit()
