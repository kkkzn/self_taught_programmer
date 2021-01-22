# Query 1
numbers = [1, 3, 5, 6]
while True:
    answer = input('Guess a number or type q to quit.')
    if answer == 'q':
        break
    try:
        answer = int(answer)
    except ValueError:
        print('Please type a number or you can quit by typing q')
    if answer in numbers:
        print('You guessed correctly!')
    else:
        print('Not in the list!')

# When exception occurs, for-else message "Not in the list!" also shows up.
# How can I disable this for-else message while responding to exception?
# exception が起こると"Not in the list"までprintされてしまう。
# exceptionメッセージ "Please type a number or you can quir by typing q" だけprintするようできないだろうか？

# Query 2
class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6
        print("Created!")

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4\
               + self.side5 + self.side6

H1 = Hexagon(3, 3, 4, 5, 6, 1)
print(H1.calculate_perimeter())

# 1s or 1side, etc. are regarded as syntax error
# Does it mean we can't begin a parameter name with number?
# Hexagonクラスの初期化でparameterに1sや1sideと打つとsyntax errorになってしまう。
# parameter名を数字から始めることはできない、ということなのだろうか？

# Query 3
try:
    'animals'.index('z')
except:
    print('there is no z in the spelling')

# Why doesn't the except header specify an error type (like ValueError)?
# How is Ln45:48 (try/except) different from the coding with if/else?
# （↑は独学プログラマーの本で出てきたコード）exceptの後にエラータイプが設定されていないけど動く。
# ValueErrorとか打たなくてもOKでしょうか？
# Ln45:48についてはif/else使ってもOK？　違いは何？
