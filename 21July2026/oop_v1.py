
"""
variables --> oop me isko kehty attributes..
functions --> inko methods kehty...
"""

# class FootballPlayer:
#     name = "Iftikhar"
#
# player1 = FootballPlayer()
# player2 = FootballPlayer()
#
# print(player1.name)
# print(player2.name)
# print(player2.age)


class FootballPlayer:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.country = "United Kingdom"

    def get_prefix_for_player(self):
        prefix = "Sr" if self.age >= 25 else "Jr"
        return prefix

    def remaining_retirement_yrs(self):
        remaining_yrs = 40 - self.age
        print(f"Remaining retirement years of {self.get_prefix_for_player()} {self.name}: {remaining_yrs}")

    def __str__(self):
        return f"My football player: {self.name}"

# p1 = FootballPlayer("Iftikhar", 29, "iftikhar@gmail.com")
# print(p1)
# print(p1.name)
# print(p1.age)
# print(p1.email)
# print(p1.country)
# p1.country = "USA"
# print(p1.country)
# p1.remaining_retirement_yrs()
# p1.add = "address"
# print(p1.add)
#
# p2 = FootballPlayer("Ali", 24, "")
# print(p2)
# print(p2.name)
# print(p2.age)
# print(p2.email)
# print(p2.country)
# p2.remaining_retirement_yrs()

player1 = FootballPlayer("Iftikhar", 29, "iftikhar@gmail.com")
print(player1)
