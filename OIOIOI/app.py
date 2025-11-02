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

# import sys

"""
**************************
_  Tura I | 27.10.2025   _
~~~~~~~~~han.pdf~~~~~~~~~~
- Grzegorz Tereszkiewicz -
************************** 
"""
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
    """


# ________________________________________________________________________ #

"""
**************************
_  Tura I | 02.11.2025   _
~~~~~~~~~prz.pdf~~~~~~~~~~
- Grzegorz Tereszkiewicz -
************************** 
"""
"""
import heapq

def oblicz_lcp(s1: str, s2: str) -> int:
    i = 0
    m = len(s1) if len(s1) < len(s2) else len(s2)
    while i < m and s1[i] == s2[i]: i += 1
    return i

def oblicz_minimalny_koszt_klawiszy(strony: list) -> tuple:
    n = len(strony)
    if n == 0: return 0, ""

    dl = [len(s) for s in strony]
    minimalny_koszt_dotarcia = dl[:]
    indeks_strony_bazowej = list(range(n))
    odwiedzone = [False] * n
    calkowity_koszt_ruchu = 0
    kolejnosc_odwiedzania = []

    pq = []
    for i in range(n): heapq.heappush(pq, (minimalny_koszt_dotarcia[i], i))

    while pq:
        najlepszy_koszt, u = heapq.heappop(pq)
        if odwiedzone[u]: continue
        odwiedzone[u] = True
        calkowity_koszt_ruchu += najlepszy_koszt
        kolejnosc_odwiedzania.append(u)
        u_len = dl[u]

        for v in range(n):
            if odwiedzone[v]: continue
            l = oblicz_lcp(strony[u], strony[v])
            koszt_przez_tab = 1 + (u_len - l) + (dl[v] - l)
            if koszt_przez_tab < minimalny_koszt_dotarcia[v]:
                minimalny_koszt_dotarcia[v] = koszt_przez_tab
                indeks_strony_bazowej[v] = u
                heapq.heappush(pq, (koszt_przez_tab, v))

    sekwencja_klawiszy_parts = []
    for cel in kolejnosc_odwiedzania:
        cel_str = strony[cel]
        baza = indeks_strony_bazowej[cel]
        if baza == cel: sekwencja_klawiszy_parts.append(cel_str)
        else:
            baza_str = strony[baza]
            l = oblicz_lcp(baza_str, cel_str)
            sekwencja_klawiszy_parts.append("T")
            backspaces = len(baza_str) - l
            if backspaces: sekwencja_klawiszy_parts.append("B" * backspaces)
            if l < len(cel_str): sekwencja_klawiszy_parts.append(cel_str[l:])
        sekwencja_klawiszy_parts.append("E")

    minimalna_liczba_klawiszy = calkowity_koszt_ruchu + n
    return minimalna_liczba_klawiszy, "".join(sekwencja_klawiszy_parts)


def main() -> None:
    n = int(input())
    strony = [input().strip() for _ in range(n)]
    wynik, sekwencja = oblicz_minimalny_koszt_klawiszy(strony)
    print(wynik)
    print(sekwencja)

if __name__ == "__main__":
    main()
"""


# ________________________________________________________________________ #

"""
**************************
_  Tura I | 02.11.2025   _
~~~~~~~~~rpk.pdf~~~~~~~~~~
- Grzegorz Tereszkiewicz -
************************** 
"""

