# maak een lijst van wachtwoorden van een bepaald aantal karakters 
# import random
import random
def maak_wachtwoord(lengte):
    # maak een wachtwoord van lengte 'lengte' met hoofdletters, kleine letters en cijfers
    hoofdletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kleine_letters = "abcdefghijklmnopqrstuvwxyz"
    cijfers = "0123456789"
    vreemde_tekens = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    
    # combineer alle karakters
    alle_karakters = hoofdletters + kleine_letters + cijfers + vreemde_tekens
    
    # genereer een wachtwoord
    wachtwoord = ''.join(random.choice(alle_karakters) for _ in range(lengte))
    
    return wachtwoord
def main():
    # vraag de gebruiker om de lengte van het wachtwoord
    try:
        lengte = int(input("Voer de gewenste lengte van het wachtwoord in: "))
        if lengte <= 0:
            raise ValueError("De lengte moet een positief getal zijn.")
    except ValueError as e:
        print(f"Fout: {e}")
        return
    
    # genereer en print het wachtwoord
    wachtwoord = maak_wachtwoord(lengte)
    print(f"Genereerd wachtwoord: {wachtwoord}")
if __name__ == "__main__":
    main()
# hussel wachtwoord
# hussel wachtwoord
# 
#             



