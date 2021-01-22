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
# Does it mean I can't start a variable name from number?

# Query 3
try:
    'animals'.index('z')
except:
    print('there is no z in the spelling')

# Why doesn't the except header specify an error type (like ValuError)?
# How is Ln53:56 (try/except) different from the coding with if/else?
