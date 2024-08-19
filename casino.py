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

# # Create a game instance and start the game
# game = Blackjack()
# game.play()


class SlotMachine():
    dict = {
        1: 3,
        2: 7,
        3: 13,
        4: 7,
        5: 17,
        6: 1,
        7: 1,
        8: 9,
        9: 5,
        10: 20,
        11: 20,
        12: 20,
        13: 20,
        14: 20,
        15: 18,
        16: 18,
        17: 18,
        18: 18,
        19: 16,
        20: 16,
        21: 14,
        22: 14,
        23: 14,
        24: 12,
        25: 12,
        26: 12,
        27: 12,
        28: 12,
        29: 12,
        30: 12,
        31: 10,
        32: 10
    }

    dict2 = {
        1: "bar",
        2: "blank",
        3: "seven",
        4: "blank",
        5: "cherry",
        6: "blank",
        7: "bar",
        8: "blank",
        9: "bell",
        10: "blank",
        11: "seven",
        12: "blank",
        13: "grape",
        14: "blank",
        15: "orange",
        16: "blank",
        17: "bar",
        18: "blank",
        19: "seven",
        20: "blank",
        21: "cherry",
        22: "blank"
    }

    def play(self, money):
        money -= 1000

        num = random.randint(1, 32)
        slot1 = self.dict2[self.dict[num]]
        
        num = random.randint(1, 32)
        slot2 = self.dict2[self.dict[num]]

        num = random.randint(1, 32)
        slot3 = self.dict2[self.dict[num]]

        # print(slot1 + " " + slot2 + " " + slot3)
        
        if slot1 == slot2 == slot3 == "seven":
            money += 15000
        elif slot1 == slot2 == slot3 == "bell":
            money += 7500
        elif slot1 == slot2 == slot3 == "grape":
            money += 5000
        elif slot1 == slot2 == slot3 == "cherry":
            money += 5000
        elif slot1 == "seven" or slot2 == "seven" or slot3 == "seven":
            money += 2500
        elif slot1 == "bell" or slot2 == "bell" or slot3 == "bell":
            money += 2000
        elif slot1 == "grape" or slot2 == "grape" or slot3 == "grape":
            money += 1500
        elif slot1 == "cherry" or slot2 == "cherry" or slot3 == "cherry":
            money += 1500
        elif slot1 == slot2 == slot3 == "bar":
            money += 700
        elif slot1 == "bar" or slot2 == "bar" or slot3 == "bar":
            money += 300
        
        # print(self.money)

        return slot1, slot2, slot3, money


# game = SlotMachine()
# output = game.play(1000)
# print(output[0] + " " + output[1] + " " + output[2] + " " + str(output[3]))