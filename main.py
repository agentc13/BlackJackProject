# Blackjack game

from art import logo
import random

new_game = True

while new_game:
    game_over = False
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    card_dealt = None


    def deal_card():
        global card_dealt
        card_dealt = random.choice(cards)
        return card_dealt


    def calculate_score(location):
        calculation = sum(location)
        if calculation == 21:
            calculation = 0
        if calculation > 21:
            for card in location:
                if card == 11:
                    location.remove(11)
                    location.append(1)
        return calculation


    dealers_hand = []
    players_hand = []
    players_score = 0
    dealers_score = 0
    players_turn = True
    dealers_turn = False

    while not game_over:
        while len(dealers_hand) < 2:  # Deal cards to dealer
            deal_card()
            dealers_hand.append(card_dealt)
        while len(players_hand) < 2:  # Deal cards to player
            deal_card()
            players_hand.append(card_dealt)

        while players_turn:
            print(dealers_hand[1])
            print(players_hand)
            players_score = calculate_score(players_hand)
            dealers_score = calculate_score(dealers_hand)
            if players_score == 0 and dealers_score != 0:
                print("Black Jack! You win.")
                game_over = True
                players_turn = False
            elif players_score == 0 and dealers_score == 0:
                print("Push! You tie.")
                game_over = True
                players_turn = False
            elif players_score > 21:
                print("Bust, you lose")
                game_over = True
                players_turn = False
            else:
                hit = input(f"Your score is {calculate_score(players_hand)}, press 'h' to Hit, press 's' to Stand.: ")
                if hit == "s":
                    players_turn = False
                    dealers_turn = True
                if hit == "h":
                    deal_card()
                    players_hand.append(card_dealt)

        print(f"Dealer has:{dealers_hand}")
        while dealers_turn:
            dealers_score = calculate_score(dealers_hand)
            if dealers_score == 0:
                print("Black Jack, Dealer wins!")
                dealers_turn = False
                game_over = True
            elif dealers_score > 21:
                print("Dealer busts, player wins!")
                dealers_turn = False
                game_over = True
            elif dealers_score < 17 or dealers_score < players_score:
                deal_card()
                dealers_hand.append(card_dealt)
                print(f"Dealer has {dealers_score} + {card_dealt} = {calculate_score(dealers_hand)}")
            elif players_score == dealers_score:
                print("Push, it's a tie!")
                game_over = True
                dealers_turn = False
            elif dealers_score > players_score:
                print("Dealer wins!")
                game_over = True
                dealers_turn = False

    play_again = input("Do you want to play again?: 'y/n'")
    if play_again == "y":
        new_game = True
    else:
        new_game = False
