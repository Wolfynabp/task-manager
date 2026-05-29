def hlavni_menu():
    """
    Zobrazuje hlavní menu programu a umožňuje práci s úkoly.

    Návratová hodnota:
        None
    """

    ukoly_menu = []
    while True:
        print("\n--- Správce úkolů - Hlavní menu ---")
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Odstranit úkol")
        print("4. Konec")

        volba = input("Vyber možnost (1-4): ")

        if volba == "1":
           ukoly_menu = pridat_ukol(ukoly_menu)
        elif volba == "2":
            zobrazit_ukoly(ukoly_menu)
        elif volba == "3":
           ukoly_menu = odstranit_ukol(ukoly_menu)
        elif volba == "4":
            print("Ukončuji program., měj se hezky..")
            break
        else:
            print("Neplatná volba, zkus to znovu, vyber možnost (1-4)")

def pridat_ukol(seznam_ukolu: list) -> list:
    """
    Přidá nový úkol do seznamu úkolů.

    Parametry:
        seznam_ukolu (list): Seznam úkolů.

    Návratová hodnota:
        list: Aktualizovaný seznam úkolů.
    """

    # Validace názvu
    while True:
        nazev = input("Zadejte název úkolu: ")

        if not nazev.strip():
            print("Chyba! Název nesmí být prázdný.")
        else:
            break

    # Validace popisu
    while True:
        popis = input("Zadejte popis úkolu: ")

        if not popis.strip():
            print("Chyba! Popis nesmí být prázdný.")
        else:
            break

    ukol = {
        "nazev": nazev,
        "popis": popis
    }

    seznam_ukolu.append(ukol)
    print("Úkol byl úspěšně přidán")
    return seznam_ukolu

def zobrazit_ukoly(seznam_ukolu: list):
    """
    Zobrazí všechny úkoly uložené v seznamu.

    Parametry:
        seznam_ukolu (list): Seznam úkolů.
    """

    if not seznam_ukolu:
        print("Seznam je prázdný")
    else:
        print("Seznam úkolů:")


        for i, ukol in enumerate(seznam_ukolu, start=1):

            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")


def odstranit_ukol(seznam_ukolu: list) -> list:
    """
    Odstraní vybraný úkol ze seznamu úkolů.

    Parametry:
        seznam_ukolu (list): Seznam úkolů.

    Návratová hodnota:
        list: Aktualizovaný seznam úkolů.
    """

    ukoly_odstranit = seznam_ukolu

    if not ukoly_odstranit:
        print("Seznam úkolů je prázdný.")
        return ukoly_odstranit

    zobrazit_ukoly(ukoly_odstranit)

    volba = input("Zadejte číslo úkolu,který chcete odstranit:")

    if not volba.isdigit():
        print("Neplatný vstup – zadejte číslo.")
        return ukoly_odstranit

    index = int(volba) - 1

    if index < 0 or index >= len(ukoly_odstranit):
        print("Neplatné číslo úkolu.")
        return ukoly_odstranit

    print(f"Úkol '{ukoly_odstranit[index]['nazev']}' byl úspěšně odstraněn")
    ukoly_odstranit.pop(index)

    return ukoly_odstranit

hlavni_menu()
