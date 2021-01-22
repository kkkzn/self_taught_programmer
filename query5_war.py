class Card:
    suits = ("spades", "hearts",
             "diamonds", "clubs")

    values = (None, None, "2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace")

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of "\
            + self.suits[self.suit]
        return v

from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
# Ln53 is the first time I see [return] keyword is used with [.pop] method.
# Please check if my assumption is correct.
## My assumption for what [return XXX.pop()] does:
## [return XXX.pop()] removes the last item from the container(XXX),
## and returns the removed item.

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("p1 name: ")
        name2 = input("p2 name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {}; {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("begging War!")
        while len(cards) >= 2:
            m = "q to quit. Any key to play: "
            resp = input(m)
            if resp == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
# What would happen here if I didn't define __lt__ and __gt__ in Ln15:33?
# Can the program process [Ln97 p1c > p2c] correctly without Ln15:33?

# As for this query, please check if my assumption is correct.
## My assumption:
## __lt__ and __gt__ define the protocol of comparing cards (Ln16:22, Ln26:32).
## This helps program compare cards, which have two values: value and suit.
## Even though value and suit have been already converted into integers,
## program can't judge which value prevails the other so can't make a comparison.
## So when you want your program to compare objects containing multiple values,
## defining the protocol of comparison by __lt__ and __gt__ is necessary.

# Another question about Ln15:33:
# Do we really need Ln23 and Ln33?
                
        win = self.winner(self.p1, self.p2)
        print("War is over. {} wins this war.".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

game = Game()
game.play_game()
