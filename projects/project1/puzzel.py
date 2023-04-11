import random

print("Welkom bij steen, papier, schaar")

# score update functions
def puntGelijk():
    print("Gelijk spel.")
    gelijk += 1
    stand()

def puntVerloren():
    print("De computer wint.")
    verloren += 1
    stand()

def puntGewonnen():
    print("Jij wint!")
    gewonnen += 1
    stand()

def stand():
    print(f"Gewonnen: {gewonnen}, Verloren: {verloren}, Gelijk spel: {gelijk}")

mogelijkeAntwoorden = ["steen", "papier", "schaar"]
gewonnen, verloren, gelijk = 0, 0, 0

while True:
    antwoord = input("Steen, papier of schaar? ")
    antwoord = antwoord.lower()

    if antwoord != "steen" and antwoord != "papier" and antwoord != "schaar":
        print("Antwoord: steen of papier of schaar.")
        break
    else:
        computerAntwoord = random.choice(mogelijkeAntwoorden)
        
        print(f"{antwoord} VS {computerAntwoord}")

        if computerAntwoord == antwoord:
            puntGelijk()
        elif computerAntwoord == "schaar" and antwoord == "papier":
            stand()
        elif computerAntwoord == "papier" and antwoord == "steen":
            stand()
        elif computerAntwoord == "steen" and antwoord == "schaar":
            stand()
        elif antwoord == "papier" and computerAntwoord == "steen":
            puntGewonnen()
        elif antwoord == "schaar" and computerAntwoord == "papier":
            puntGewonnen()
        elif antwoord == "steen" and  computerAntwoord == "schaar":
            puntGewonnen()
        elif antwoord == "sluiten":
            False
        else:
            print("Er is denk ik iets fout gegaan.")