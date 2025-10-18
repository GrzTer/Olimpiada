########### Interpretacja python do zadania palindrom.pdf, do wykonania w C++ ###########
"""
from collections import Counter


def zbierz_wszystkie_linie(plansza: list[str], rozmiar_N: int) -> list[str]:
    linie: list[str] = []

    linie.extend(plansza)

    for kolumna in range(rozmiar_N):
        linie.append("".join(plansza[wiersz][kolumna] for wiersz in range(rozmiar_N)))

    for i in range(1 - rozmiar_N, rozmiar_N):
        przekatna = "".join(
            plansza[wiersz][wiersz - i]
            for wiersz in range(rozmiar_N)
            if 0 <= wiersz - i < rozmiar_N
        )
        if przekatna:
            linie.append(przekatna)

    for i in range(2 * rozmiar_N - 1):
        anty_przekatna = "".join(
            plansza[wiersz][i - wiersz]
            for wiersz in range(rozmiar_N)
            if 0 <= i - wiersz < rozmiar_N
        )
        if anty_przekatna:
            linie.append(anty_przekatna)
    return linie


def znajdz_wszystkie_palindromy(linie: list[str]) -> list[str]:
    znalezione_palindromy: list[str] = []

    for linia in linie:
        dlugosc_linii = len(linia)
        for dlugosc in range(5, dlugosc_linii + 1):
            for i in range(dlugosc_linii - dlugosc + 1):
                fragment = linia[i : i + dlugosc]
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
    if dlugosc_N == 0:
        return "BRAK"
    elif dlugosc_N == 1:
        return 0

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

                if cel == dlugosc_N - 1:
                    return skoki

                if energia_po_skok > nowe_miejsca.get(cel, -1):
                    nowe_miejsca[cel] = energia_po_skok
        print(f"Runda {skoki}: {miejsca}")
        miejsca = nowe_miejsca

    return "BRAK"


def main() -> None:
    N = int(input())
    napoje: list[int] = []
    while len(napoje) < N:
        napoje.extend(map(int, input().split()))
    napoje = napoje[:N]
    wynik = minimalna_liczba_skokow(napoje)
    print(wynik)


if __name__ == "__main__":
    main()
"""

########### Interpretacja python do zadania podzial.pdf, do wykonania w C++ ###########
"""
import math


def czy_liczba_pierwsza(liczba: int) -> bool:
    if liczba < 2:
        return False
    for i in range(2, int(math.sqrt(liczba)) + 1):
        if liczba % i == 0:
            return False
    return True


def czy_unikalne_cyfry(podciag: str) -> bool:
    return len(set(podciag)) == len(podciag)


def znajdz_minimalny_podzial(ciag_cyfr: str) -> int | None:
    dlugosc_ciagu = len(ciag_cyfr)
    nieskonczonosc = float("inf")

    min_podzialy = [nieskonczonosc] * (dlugosc_ciagu + 1)
    min_podzialy[0] = 0

    for i in range(1, dlugosc_ciagu + 1):
        for j in range(i):
            fragment = ciag_cyfr[j:i]
            if min_podzialy[j] != nieskonczonosc:
                if czy_unikalne_cyfry(fragment):
                    liczba = int(fragment)
                    if czy_liczba_pierwsza(liczba):
                        min_podzialy[i] = min(min_podzialy[i], min_podzialy[j] + 1)
    wynik = min_podzialy[dlugosc_ciagu]

    if wynik == nieskonczonosc:
        return None
    return wynik


def main() -> None:
    ciag_cyfr = input().strip()

    wynik = znajdz_minimalny_podzial(ciag_cyfr)

    if wynik is not None and wynik >= 2:
        print(wynik)
    else:
        print("BRAK")


if __name__ == "__main__":
    main()
"""

########### Interpretacja python do zadania algebraf.pdf, do wykonania w C++ ###########
"""
import itertools


def zamien_na_liczbe(slowo: str, mapa_liter: dict[str, int]) -> int:
    liczba_jako_tekst = "".join(str(mapa_liter[litera]) for litera in slowo)
    return int(liczba_jako_tekst)


def sprawdz_przypisanie(
    rownania: list[tuple[str, str, str]], mapa_liter: dict[str, int]
) -> bool:
    for arg1_str, arg2_str, wynik_str in rownania:
        arg1 = zamien_na_liczbe(arg1_str, mapa_liter)
        arg2 = zamien_na_liczbe(arg2_str, mapa_liter)
        wynik = zamien_na_liczbe(wynik_str, mapa_liter)
        if arg1 + arg2 != wynik:
            return False
    return True


def rozwiaz_algebraf(
    rownania: list[tuple[str, str, str]], unikalne_litery: list[str]
) -> str:
    znalezione_rozwiazania: list[str] = []
    cyfry = range(1, 10)
    liczba_liter = len(unikalne_litery)

    for permutacja in itertools.permutations(cyfry, liczba_liter):
        mapa_liter = dict(zip(unikalne_litery, permutacja))
        if sprawdz_przypisanie(rownania, mapa_liter):
            rozwiazanie_str = "".join(map(str, permutacja))
            znalezione_rozwiazania.append(rozwiazanie_str)
            if len(znalezione_rozwiazania) > 1:
                return "BRAK"

    if len(znalezione_rozwiazania) == 1:
        return znalezione_rozwiazania[0]
    else:
        return "BRAK"


def main() -> None:
    liczba_rownan = int(input())
    tekst_rownan = [input().strip() for _ in range(liczba_rownan)]
    wszystkie_litery = set()
    przetworzone_rownania = []

    for rownanie in tekst_rownan:
        lewa_strona, wynik = rownanie.split("=")
        arg1, arg2 = lewa_strona.split("+")
        przetworzone_rownania.append((arg1, arg2, wynik))
        wszystkie_litery.update(arg1, arg2, wynik)
    posortowane_unikalne_litery = sorted(list(wszystkie_litery))
    wynik = rozwiaz_algebraf(przetworzone_rownania, posortowane_unikalne_litery)

    print(wynik)


if __name__ == "__main__":
    main()
"""