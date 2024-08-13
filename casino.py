import random

class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def toString(self):
        return self.rank + " of " + self.suit

    def get_value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

class Blackjack:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        deck = [Cards(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def deal_card(self, hand):
        card = self.deck.pop()
        hand.append(card)
        return card

    def calculate_hand_value(self, hand):
        value = sum(card.get_value() for card in hand)
        aces = sum(1 for card in hand if card.rank == 'A')
        
        # Adjust for Aces if necessary
        while value > 21 and aces:
            value -= 10
            aces -= 1
            
        return value

    def show_hand(self, hand, hidden=False):
        if hidden:
            print("[Hidden]")
            for card in hand[1:]:
                print(card.toString())
        else:
            for card in hand:
                print(card.toString())

    def play(self):
        # Initial deal
        self.deal_card(self.player_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.dealer_hand)

        print("\nYour hand:")
        self.show_hand(self.player_hand)
        print()
        print("Dealer's hand:")
        self.show_hand(self.dealer_hand, hidden=True)
        print()

        # Player's turn
        while self.calculate_hand_value(self.player_hand) < 21:
            action = input("Do you want to 'hit' or 'stand'? ").lower()
            if action == "hit":
                self.deal_card(self.player_hand)
                print("Your hand:")
                self.show_hand(self.player_hand)
            elif action == "stand":
                break

        player_value = self.calculate_hand_value(self.player_hand)
        if player_value > 21:
            print("You busted! Dealer wins.")
            return

        # Dealer's turn
        print("\nDealer's turn:")
        self.show_hand(self.dealer_hand)
        while self.calculate_hand_value(self.dealer_hand) < 17:
            print()
            self.deal_card(self.dealer_hand)
            self.show_hand(self.dealer_hand)

        dealer_value = self.calculate_hand_value(self.dealer_hand)

        # Determine the winner
        print("\nFinal results:")
        print(f"Your hand value: {player_value}")
        print(f"Dealer's hand value: {dealer_value}")

        if dealer_value > 21:
            print("Dealer busted! You win!")
        elif player_value > dealer_value:
            print("You win!")
        elif player_value < dealer_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")

# Create a game instance and start the game
game = Blackjack()
game.play()
