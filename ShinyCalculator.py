import csv
import os

class Shiny:
    # Constructor
    def __init__(self, name, attempts, modifier=1):
        self.name = name
        self.attempts = int(attempts)
        self.modifier = modifier
    # Test if Constructor went in properly
    def reveal(self):
        print(self.name)
        print(self.attempts)
        print(self.modifier)
    
    # Geometric Distribution
    ## the probability we encounter our first shiny on the nth attempt

    def geometric(self, n):
        p = (1*int(self.modifier))/4096
        return p*(1-p)**(n-1)
    
    # Summation of Geometric Distribution
    ## the probability we encounter our first shiny on or before the nth attempt
    def sum_geometric(self):
        return sum(self.geometric(i) for i in range(1,int(self.attempts)))


def main():
    # Load File
    # input_file = input("File Name: ")
    input_file = "poke_test3"
    # Check if File exists
    if not os.path.isfile(f"{input_file}.csv"):
        poke_write(input_file)
    # Recieve list of Shiny objects
    pokedex = poke_read(input_file)
    # For every Shiny pokemon in list...
    for i in range(len(pokedex)):
        # Print name and "luck value"
        print(pokedex[i].name, pokedex[i].sum_geometric())

def poke_read(input_file):
    with open(f"{input_file}.csv", "r") as file:
        reader = csv.DictReader(file)
        pokedex = []
        for row in reader:
            pokedex.append(Shiny(row["pokemon_name"],row["attempts"],row["modifier"]))
        return pokedex

def poke_write(input_file):
    with open(f"{input_file}.csv", "w") as file:
        # Set Up csv file
        writer = csv.DictWriter(file, fieldnames=["pokemon_name", "attempts", "modifier"])
        writer.writeheader()
        while True:
            pokemon_name = input("Pokemon Name? ")
            attempts = input("How many attempts? ")
            modifier = ask_modifier()
            writer.writerow({"pokemon_name":pokemon_name, "attempts":attempts, "modifier":modifier})
            ask_continue = input("Continue? [y/n] ")      
            if ask_continue.lower() == "n":
                break

def ask_modifier():
    while True: 
        modifier = input("Did you use a Shiny Charm? [y/n] ")
        if modifier.lower() == "y":
            return 2
        elif modifier.lower() == "n":
            return 1


if __name__ == '__main__':
    main()