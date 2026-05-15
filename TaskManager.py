ukoly = []

def hlavni_menu():
    while True:
        print("\n--- Správce úkolů - Hlavní menu ---")
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Odstranit úkol")
        print("4. Konec")

        volba = input("Vyber možnost (1-4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukol()
        elif volba == "3":
           odstranit_ukol()
        elif volba == "4":
            print("Ukončuji program., měj se hezky..")
            exit()
        else:
            print("Neplatná volba, zkus to znovu, vyber možnost (1-4)")

def pridat_ukol():

    nazev = ""
    popis = ""

    while not nazev or not popis:
        nazev = input("Zadejte název úkolu:")
        popis = input("Zadejte popis úkolu:")

        if not nazev or not popis:
            print("Chyba! Název ani Popis nesmí být prázdé. Zadejte Název a Popis úkolu!")
            continue
        else:
            ukol = {
                "nazev": nazev,
                "popis": popis
                }
            ukoly.append(ukol)
            print("Úkol byl úspěšně přidán")
            break

def zobrazit_ukol():
    print("Seznam úkolů:")

    for i in range(len(ukoly)):
        #print(ukoly[i]["popis"])
        print(f"{i+1}. {ukoly[i]["nazev"]} - {ukoly[i]["popis"]}")


def odstranit_ukol():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return

    zobrazit_ukol()

    volba = input("Zadejte číslo úkolu,který chcete odstranit:")

    if not volba.isdigit():
        print("Neplatný vstup – zadejte číslo.")
        return

    index = int(volba) - 1

    if index < 0 or index >= len(ukoly):
        print("Neplatné číslo úkolu.")
        return

    print(f"Úkol '{ukoly[index]['nazev']}' byl úspěšně odstraněn")
    ukoly.pop(index)

hlavni_menu()
