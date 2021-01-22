# is キーワードについて知りたいです。

class Person:
    def __init__(self):
        self.name = "Bob"

bob = Person()
same_bob = bob
print(bob is same_bob)
# ↑True が返ってくる

another_bob = Person()
print(bob is another_bob)
# ↑Falseが返ってくる

## Check if I am guessing correctly:
## Ln 7 instantiates bob as an object in Person class
## Ln 8 assigns this bob a variable same_bob.
## Ln 9 checks the validity of the following statement:
## bob is bob who is assigned a variable same_bob. So this is True.

## Ln 12 instantiates another_bob as another object in Person class.
## Ln 13 checks the validity of the following statement:
## bob is another_bob. So this is not true.
## If another Ln assigns this another_bob a variable bob, Ln 12 will become true.
