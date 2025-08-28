class FootballClub:
    def __init__(self, name, country, founded_year, stadium, coach):
        # Attributes
        self.name = name
        self.country = country
        self.founded_year = founded_year
        self.stadium = stadium
        self.coach = coach
        self.trophies = []
        self.players =[]


    # Add a new player
    def add_player(self, player_name):
        self.players.append(player_name)
        print(f"✅ {player_name} has joined {self.name}!")

    # Remove a player
    def remove_player(self, player_name):
        if player_name in self.players:
            self.players.remove(player_name)
            print(f" {player_name} has left {self.name}.")
        else:
            print(f"️ {player_name} is not in the team.")

    # Win a trophy
    def win_trophy(self, trophy_name):
        self.trophies += 1
        print(f" {self.name} won the {trophy_name}! Total trophies: {self.trophies}")

    # Show club details
    def details(self):
        print(f"\n Club Name: {self.name}")
        print(f" Country: {self.country}")
        print(f" Founded: {self.founded_year}")
        print(f" Stadium: {self.stadium}")
        print(f" Coach: {self.coach}")
        print(f" Players: {', '.join(self.players) if self.players else 'No players yet'}")
        print(f" Trophies Won: {self.trophies}")

# creating d club class
club1 = FootballClub("Chelsea FC", "England", 1905, "Stamford Bridge", "Enzo Maresca")
club2 = FootballClub("Arsenal FC", "England", 1886, "Emirate", "Mikel Arteta")
club3 = FootballClub("Real Madrid", "Spain", 1902, "Santiago Bernabéu", "Carlo Ancelotti")


# adding polymorphism
class EuropeanClub(FootballClub):
    def __init__(self, name, country, founded_year, stadium, coach, uefa_rank):
        super().__init__(name, country, founded_year, stadium, coach)
        self.uefa_rank = uefa_rank

    # Polymorphism
    def win_trophy(self, trophy_name):
        self.trophies.append(trophy_name)
        print(f" {self.name} has conquered Europe with the {trophy_name}!  Total: {len(self.trophies)}")

    # New method unique to EuropeanClub
    def show_rank(self):
        print(f"UEFA Rank of {self.name}: {self.uefa_rank}")

#2 polymorishim challenge
class Vehicle:
    def move(self):
        print(f" This vehicle is moving .........")
#Child class
class car(Vehicle):
    def move(self):
        print(f"this car is driving on the road")

class Ship(Vehicle):
    def move(self):
        print(f"this ship is sailing on water ")
class Boat(Vehicle):
    def move(self):
        print(" The boat is sailing on water!")

class Bike(Vehicle):
    def move(self):
        print(" The bike is pedaling forward!")

Vehicle = [car(),Ship(),Boat(),Bike() ]

for v in Vehicle:
    v.move()


