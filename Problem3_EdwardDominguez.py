#problem 3: batting average calculator
#Edward Dominguez

def main():
    #user inputs name, hits, and at-bats
    player_name = input("What is the player's name?: ")
    player_hits = int(input("How many hit's did " + player_name + " " + "achieve?: "))
    player_atbat = int(input("How many at-bats did " + player_name +" " + "have?: "))

    #user inputs used for the calculation
    batting_average = player_hits / player_atbat

    print(player_name + "'s" + " " + "batting average is: " + str(batting_average))

main()