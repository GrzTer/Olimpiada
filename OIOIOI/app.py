"""
**************************
_  Tura I | 13.10.2025   _
~~~~~~~~~sil.pdf~~~~~~~~~~
~~~~   n = 3a + 8b    ~~~~
~ min_b = (2(n % 3) % 3) ~
- Grzegorz Tereszkiewicz -
**************************
"""

"""def sil(ciezar: int) -> str:
    if ciezar > 13:
        return "TAK"

    if ciezar % 3 == 0:
        return "TAK"

    if (ciezar % 8 == 0) % 3 == 0:
        return "TAK"

    return "NIE"

def main() -> None:
    n = int(input())
    print(sil(n))

if __name__ == "__main__":
    main()"""


# def sil(ciezar: int) -> str:
#     mod = ciezar % 3
#     min_b = (2 * mod) % 3
#     return "TAK" if ciezar >= 8 * min_b else "NIE"

# def main() -> None:
#     n = int(input())
#     print(sil(n))

# if __name__ == "__main__":
#     main()

"""

mod = 19 % 3 == 1

min_b = (2 * 1) % 3 == 2

zwraca: "TAK" , jeżeli 19 >= 8 * 2 , w przeciwnym wypadku "NIE"

________

mod = 5 % 3 == 2

min_b = (2 * 2) % 3 == 1

zwraca: "TAK" , jeżeli 5 >= 8 * 1 , w przeciwnym wypadku "NIE"


"""
# ________________________________________________________________________ #

import sys

"""
**************************
_  Tura I | 13.10.2025   _
~~~~~~~~~han.pdf~~~~~~~~~~
- Grzegorz Tereszkiewicz -
************************** 
"""

class Hanoj:
    def __init__(self, ilosc_klockow: int, ilosc_stostow: int)-> None:
        self.ilosc_klockow = ilosc_klockow
        self.ilosc_stostow = ilosc_stostow
        self.nastepny_klocek = [0] * (ilosc_klockow + 1)
        self.stos_gornego_klocka = [-1] * (ilosc_klockow + 1)
        self.pusty = -1
        self.stos_z_1 = -1
        for i in range(ilosc_stostow):
            wiersz_wejscia = sys.stdin.readline().split()
            ilosc_w_stosie = int(wiersz_wejscia[0])
            if ilosc_w_stosie == 0:
                if self.pusty == -1:
                    self.pusty = i
                continue
            gorny_klocek = int(wiersz_wejscia[1])
            self.stos_gornego_klocka[gorny_klocek] = i
            if gorny_klocek == 1:
                self.stos_z_1 = i
            poprzedni = gorny_klocek
            for j in range(2, ilosc_w_stosie + 1):
                obecny = int(wiersz_wejscia[j])
                self.nastepny_klocek[poprzedni] = obecny
                poprzedni = obecny

    def han(self ) -> None:
        if self.stos_z_1 == -1:
            print(-1)
            return

        k = 1
        biezacy_klocek = 1
        while self.nastepny_klocek[biezacy_klocek] and self.nastepny_klocek[biezacy_klocek] == biezacy_klocek + 1:
            biezacy_klocek = self.nastepny_klocek[biezacy_klocek]
            k += 1
        stos_z_miejscem = self.nastepny_klocek[biezacy_klocek] != 0

        if stos_z_miejscem:
            if self.pusty == -1:
                print(-1)
                return
            cel = self.pusty
            oczekiwano = 1
            obecny_max = 0
        else:
            cel = self.stos_z_1
            oczekiwano = k + 1
            obecny_max = biezacy_klocek

        ruchy = []
        for ocz in range(oczekiwano, self.ilosc_klockow + 1):
            if self.stos_gornego_klocka[ocz] == -1:
                print(-1)
                return
            a = self.stos_gornego_klocka[ocz]
            if ocz <= obecny_max:
                print(-1)
                return
            ruchy.append((a + 1, cel + 1))
            self.stos_gornego_klocka[ocz] = -1
            if self.nastepny_klocek[ocz]:
                self.stos_gornego_klocka[self.nastepny_klocek[ocz]] = a
            obecny_max = ocz

        print(len(ruchy))
        for ruch in ruchy:
            print(*ruch)

def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    han = Hanoj(n, m)
    han.han()

if __name__ == "__main__":
    main()