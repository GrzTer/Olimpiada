########### Interpretacja python do zadania palindrom.pdf, do wykonania w C++ ###########
"""
from collections import Counter

def zbierz_wszystkie_linie(plansza: list[str], rozmiar_N: int) -> list[str]:
    linie: list[str] = []

    linie.extend(plansza)

    for kolumna in range(rozmiar_N):
        linie.append("".join(plansza[wiersz][kolumna] for wiersz in range(rozmiar_N)))

    for i in range(1 - rozmiar_N, rozmiar_N):
        przekatna = "".join(plansza[wiersz][wiersz - i] for wiersz in range(rozmiar_N) if 0 <= wiersz - i < rozmiar_N)
        if przekatna:
            linie.append(przekatna)

    for i in range(2 * rozmiar_N - 1):
        anty_przekatna = "".join(plansza[wiersz][i - wiersz] for wiersz in range(rozmiar_N) if 0 <= i - wiersz < rozmiar_N)
        if anty_przekatna:
            linie.append(anty_przekatna)
    return linie


def znajdz_wszystkie_palindromy(linie: list[str]) -> list[str]:
    znalezione_palindromy: list[str] = []

    for linia in linie:
        dlugosc_linii = len(linia)
        for dlugosc in range(5, dlugosc_linii + 1):
            for i in range(dlugosc_linii - dlugosc + 1):
                fragment = linia[i:i + dlugosc]
                if fragment == fragment[::-1]:
                    znalezione_palindromy.append(fragment)
    return znalezione_palindromy


def znajdz_rozwiazanie(palindromy: list[str]) -> str | None:
    licznik_wystapien = Counter(palindromy)

    for palindrom, liczb_wystapien in licznik_wystapien.items():
        if liczb_wystapien >= 2:
            return palindrom
    return None


def main():
    rozmiar_N = int(input())
    plansza = [input().strip() for _ in range(rozmiar_N)]

    wszystkie_linie = zbierz_wszystkie_linie(plansza, rozmiar_N)
    wszystkie_palindromy = znajdz_wszystkie_palindromy(wszystkie_linie)
    wynik = znajdz_rozwiazanie(wszystkie_palindromy)
    print(wynik)

if __name__ == "__main__":
    main()
"""

########### Interpretacja python do zadania skoczek.pdf, do wykonania w C++ ###########
"""
def minimalna_liczba_skokow(napoje: list[int]) -> int:
    dlugosc_N = len(napoje)
    if dlugosc_N == 0: return "BRAK"
    elif dlugosc_N == 1: return 0

    miejsca: dict[int, int] = {0: napoje[0]}
    skoki: int = 0

    while miejsca:
        skoki += 1
        nowe_miejsca: dict[int, int] = {}
        
        for pozycja, energia in miejsca.items():
            najdalszy_skok = min(energia, dlugosc_N - 1 - pozycja)
            for zasieg in range(1, najdalszy_skok + 1):
                cel = pozycja + zasieg
                energia_po_skok = energia - zasieg + napoje[cel]
                
                if cel == dlugosc_N - 1: return skoki
                
                if energia_po_skok > nowe_miejsca.get(cel, -1): nowe_miejsca[cel] = energia_po_skok
        print(f"Runda {skoki}: {miejsca}")
        miejsca = nowe_miejsca

    return "BRAK"

def main() -> None: 
    N = int(input())
    napoje: list[int] = []
    while len(napoje) < N: napoje.extend(map(int, input().split()))
    napoje = napoje[:N]
    wynik = minimalna_liczba_skokow(napoje)
    print(wynik)

if __name__ == "__main__":
    main()
"""

