class Player:
    def __init__(self, name, age, sport):
        self.name = name
        self.age = age
        self.sport = sport
        
    
    def greeting(self):
        print("Hi I am {} and I play {}".format(self.name, self.sport))

    def identification_code(self):
        print("My player ID is: {}{}". format(self.name, self.age))

player1 = Player("Cristiano", 34, "Footballer")
player2 = Player("Kobe", 41, "Basketballer")
player3 = Player("Sachin", 48, "Footballer")

print(player1.name)
print(player2.name)
print(player3.name)


#subtle differences

player1.identification_code()
print(Player.identification_code(player1))