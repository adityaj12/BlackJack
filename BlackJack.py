import turtle
import time
import random

#set screen and main turtle - only one used
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

#function to draw card visuals
def draw_card(x,y,c,color):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.pencolor(color)
  for i in range(2):
    t.fd(90)
    t.rt(90)
    t.fd(135)
    t.rt(90)
  t.penup()
  t.goto(x+45,y-115)
  t.pendown()
  t.write(c, move=False, align="center", font=("Times New Roman", 60, "normal"))

#functions that print end text based on who won
def bust(hand):
  t.penup()
  if hand == "User":
    t.goto(150, 175)
  elif hand == "Dealer":
    t.goto(150, -75)
  t.pendown()
  t.color("yellow")
  t.write("Bust!", move=False, align="left", font=("Times New Roman", 50, "normal"))
  time.sleep(2)

def user_win():
  t.penup()
  t.goto(50,200)
  t.pendown()
  t.color("yellow")
  t.write("You Win!", move=False, align="left", font=("Times New Roman", 32, "normal"))
  time.sleep(2)

def dealer_win():
  t.penup()
  t.goto(50,200)
  t.pendown()
  t.color("yellow")
  t.write("Dealer Wins!", move=False, align="left", font=("Times New Roman", 32, "normal"))
  time.sleep(2)

def tie():
  t.penup()
  t.goto(150,175)
  t.pendown()
  t.color("yellow")
  t.write("Tie!", move=False, align="left", font=("Times New Roman", 50, "normal"))
  time.sleep(2)

#hand setups
def setup():
  screen.reset()
  t.pensize(5)
  t.speed(0)
  t.pencolor("lightblue")
  t.ht()
  t.penup()
  t.goto(-300,175)
  t.pendown()
  t.write("User Hand", move=False, align="left", font=("Times New Roman", 50, "normal"))
  t.penup()
  t.goto(-300,-75)
  t.pendown()
  t.pencolor("violet")
  t.write("Dealer Hand", move=False, align="left", font=("Times New Roman", 50, "normal"))

#main function
def blackjack():

  # print out text for the game start
  print("Welcome to the game of Blackjack!")
  time.sleep(1)
  print("In this game, you will be dealt two cards to start.")
  time.sleep(1)
  print("Your goal is to get as close to 21 as possible without going over - or busting!")
  time.sleep(1)
  print("In this simple version of Blackjack, we only use the cards 2 through 11 (Ace).")
  time.sleep(1)
  print("The dealer will first ask you to hit (take another card) or stay.")
  time.sleep(1)
  print("As long as you don't bust, once you decide to stay, the dealer will then play his hand.")
  time.sleep(1)
  print("The dealer always has to hit until his hand is at least 17. Whoever has the better hand at the end wins!")
  time.sleep(1)

  #start turtle window
  setup()
  user_hand = []
  dealer_hand = []
  for i in range(2):
    user_hand.append(random.randint(2,11))
    dealer_hand.append(random.randint(2,11))

  # main while loop
  while True:
    x = True
    print("\nHere's your hand:")
    print(user_hand)
    x_coor = -300
    x_coor2 = -300
    for num in user_hand:
      draw_card(x_coor,155,str(num),"red")
      x_coor += 110

    # checks for user blackjack
    if sum(user_hand) == 21:
      print("Blackjack! You win!")
      user_win()
      input("\nPress Enter to play!")
      x = False
      setup()
      user_hand = []
      dealer_hand = []
      for i in range(2):
        user_hand.append(random.randint(2,11))
        dealer_hand.append(random.randint(2,11))

    # checks for user bust
    elif sum(user_hand) > 21:
      print("You busted!")
      bust("User")
      input("\nPress Enter to play!")
      x = False
      setup()
      user_hand = []
      dealer_hand = []
      for i in range(2):
        user_hand.append(random.randint(2,11))
        dealer_hand.append(random.randint(2,11))

    # while player hits, add card
    if x == True:
      hit_or_stay = input("\nType in H to hit or S to stay: ")

      if hit_or_stay == 'H':
        val = random.randint(2,11)
        user_hand.append(val)
        draw_card(x_coor, 155, str(val), "red")
        x_coor += 120

    # dealer turn and while loop
      elif hit_or_stay == 'S':
        print("\nDealer's turn!")
        x = True

        while x == True:
          for num in dealer_hand:
              draw_card(x_coor2,-100,str(num),"lightgreen")
              x_coor2 += 120

          while sum(dealer_hand) < 17:
            print("\nHere's the dealer's hand:")
            print(dealer_hand)
            time.sleep(1.33)
            val = random.randint(2,11)
            dealer_hand.append(val)
            draw_card(x_coor2,-100,str(val),"lightgreen")
            x_coor2 += 120

          # checks for dealer blackjack
          if sum(dealer_hand) == 21:
            print("\nHere's the dealer's hand:")
            print(dealer_hand)
            if len(dealer_hand) == 2:
                for num in dealer_hand:
                    draw_card(x_coor2,-100,str(num), "lightgreen")
                    x_coor2 += 120
            print("Blackjack! The dealer won!")
            dealer_win()
            input("\nPress Enter to play!")
            setup()
            user_hand = []
            dealer_hand = []
            for i in range(2):
              user_hand.append(random.randint(2,11))
              dealer_hand.append(random.randint(2,11))
            x = False

          # checks for dealer bust
          elif sum(dealer_hand) >= 21:
            print("\nHere's the dealer's hand:")
            print(dealer_hand)
            print("The dealer busted! You win!")
            bust("Dealer")
            input("\nPress Enter to play!")
            setup()
            user_hand = []
            dealer_hand = []
            for i in range(2):
              user_hand.append(random.randint(2,11))
              dealer_hand.append(random.randint(2,11))
            x = False

          # final comparison of hands
          else:
            print("\nHere's the dealer's hand:")
            print(dealer_hand)
            print("The dealer has finalized his hand.")

            if sum(user_hand) > sum(dealer_hand):
              print("\nYou won!")
              user_win()
              input("\nPress Enter to play!")
              setup()
              user_hand = []
              dealer_hand = []
              for i in range(2):
                user_hand.append(random.randint(2,11))
                dealer_hand.append(random.randint(2,11))
              x = False

            elif sum(user_hand) < sum(dealer_hand):
              print("\nThe dealer won!")
              dealer_win()
              input("\nPress Enter to play!")
              setup()
              user_hand = []
              dealer_hand = []
              for i in range(2):
                user_hand.append(random.randint(2,11))
                dealer_hand.append(random.randint(2,11))
              x = False

            else:
              print("\nIt's a tie!")
              tie()
              input("\nPress Enter to play!")
              setup()
              user_hand = []
              dealer_hand = []
              for i in range(2):
                user_hand.append(random.randint(2,11))
                dealer_hand.append(random.randint(2,11))
              x = False

blackjack()