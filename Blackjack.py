import random

# Data Structures for Suits, Ranks, and Values
suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}

# Define Class Objects: Card, Deck, Player, and Hand
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)
        print("The deck has been shuffled")

    def deal(self):
        return self.cards.pop()


class Player:
    def __init__(self, bank=100):
        self.bank = bank
        self.bet = 0

    def sub_bank(self, amount):
        self.bank -= amount
        self.bet += amount

    def add_bank(self):
        self.bank += self.bet * 2


class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0

    def draw(self, card):
        self.hand.append(card)
        if (card.rank == "Ace" and self.value < 12):
            self.value += (values[card.rank] + 10)
        else:
            self.value += values[card.rank]

    def show(self):
        for card in self.hand:
            print(card)

    def __del__(self):
        pass


# Functions: win_check(), replay(), game_switch()

def win_check():
    if player_hand.value == 21:
        print("You have won!!")
        player.add_bank()
        player_hand.__del__()
        dealer_hand.__del__()
    elif player_hand.value > 21:
        print("You've busted")
        player_hand.__del__()
        dealer_hand.__del__()
    elif dealer_hand.value == 21:
        print("The dealer won!")
        dealer_hand.show()
        player_hand.__del__()
        dealer_hand.__del__()
    elif dealer_hand.value > 21:
        print("The dealer busted so you win!")
        player.add_bank()
        player_hand.__del__()
        dealer_hand.__del__()
    elif dealer_hand.value == player_hand.value:
        print("You tied with the dealer")
        dealer_hand.show()
        player_hand.__del__()
        dealer_hand.__del__()
    elif dealer_hand.value < player_hand.value:
        print("Your hand is higher, so you win!")
        player.add_bank()
        player_hand.__del__()
        dealer_hand.__del__()
    else:
        print("The dealer's hand is higher, so you lose")
        player_hand.__del__()
        dealer_hand.__del__()
        dealer_hand.show()


def replay_check():
    global replay, game_on
    player_replay = str(input("Do you want to keep playing?  (Y/N) "))
    player_replay.lower()
    if player_replay[0] == "y":
        print("Starting new round...")
    else:
        print("Ok, goodbye")
        replay = False
        game_on = False

def game_switch():
    global replay, game_on
    if player.bank <= 0:
        print("You're too poor to play any more.")
        replay = False
        game_on = False


# Game State Variables

game_on = True
replay = True

# Game Loop

while game_on:
    print("Welcome to the Aniela's Blackjack Game")

    player = Player()
    dealer = Player()

    while replay:
        game_deck = Deck()
        game_deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.draw(game_deck.deal())
        dealer_hand.draw(game_deck.deal())
        player_hand.draw(game_deck.deal())
        dealer_hand.draw(game_deck.deal())
        print(f"The dealer is showing: {dealer_hand.hand[0].__str__()}")
        print("Your hand:")
        player_hand.show()
        print(f"Count: {str(player_hand.value)}")
        print(f"You have ${str(player.bank)} left")
        amount = int(input("How much do you want to bet? "))
        player.sub_bank(amount)
        hitorstay = str(input("Would you like to hit or stay? (H/S) "))
        hitorstay.lower()
        while hitorstay == "h" and player_hand.value < 21:
            player_hand.draw(game_deck.deal())
            print("Your hand: ")
            player_hand.show()
            print(f"Count: {str(player_hand.value)}")
            hitorstay = str(input("Would you like to hit or stay? (H/S) "))
            hitorstay.lower()
        print("The dealer has:")
        dealer_hand.show()
        while dealer_hand.value < 17:
            dealer_hand.draw(game_deck.deal())
        win_check()
        player.bet = 0
        replay_check()
        game_switch()