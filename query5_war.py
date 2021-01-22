# 戦争ゲームのコードです。
# __lt__ __gt__メソッドについて知りたいです。
# Ln36:50で__lt__ __gt__を定義しているが、これがなぜ必要なのか？
# 仮説を立てたので、その理解であっているか教えて欲しいです。

## My assumption:
## __lt__ and __gt__ define the protocol of comparing cards (Ln36:42, Ln44:50).
## This helps program compare "cards" that have two values: value and suit.
## Even though value and suit have been already converted into integers,
## program can't judge which value prevails the other so can't make a comparison.
## So when I want my program to compare objects containing multiple values,
## defining the protocol of comparison by __lt__ and __gt__ is necessary.
## 仮説:
## __lt__、__gt__はカードの強さを比較するプロトコルを定義している。
## カードは二つの別々の値（数字とマーク）を持っているため、どの順で比較するかの定義が必要。
## その定義をLn36:50でやっている。
## つまり、プログラムに２種類以上の値を持つオブジェクト同士を比較させたいときは、
## __lt__, __gt__で、それらをどの様で比較すれば良いかを定める必要が発生してくる。



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
        elif self.value == c2.value:
            return self.suit < c2.suit
        else:
            return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        elif self.value == c2.value:
            return self.suit > c2.suit
        else:
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

    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

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

    def print_winner(self, winner):
        w = "{} wins this round"
        print(w.format(winner.name))

    def print_draw(self, p1, p2):
        d = "{} drew {}; {} drew {}"
        print(d.format(p1.name, p1.card, p2.name, p2.card))

    def play_game(self):
        cards = self.deck.cards
        print("begging War!")
        while len(cards) >= 2:
            m = "q to quit. Any key to play: "
            resp = input(m)
            if resp == "q":
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1, self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)
                
        win = self.winner(self.p1, self.p2)
        print("War is over. {} wins this war.".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p1.wins < p2.wins:
            return p2.name
        else:
            return "It was a tie!"

game = Game()
game.play_game()
