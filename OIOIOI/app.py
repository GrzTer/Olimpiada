"""
**************************
_  Tura I | 13.10.2025   _
~~~~~~~~~sil.pdf~~~~~~~~~~
~~~~   n = 3a + 8b    ~~~~
~ min_b = (2(n % 3) % 3) ~
- Grzegorz Tereszkiewicz -
**************************
"""

from math import frexp

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
_  Tura I | 07.11.2025   _
~~~~~~~~~rpk.pdf~~~~~~~~~~
- Grzegorz Tereszkiewicz -
************************** 
"""
"""
from collections import deque

def bfs(start: tuple[int, int], cel: tuple[int, int], plansza: list[list[int]], n: int) -> list[tuple[int, int]] | None:
    if start == cel: return []
    kolejka = deque([start])
    odwiedzone = {start}
    rodzic = {start: None}
    
    while kolejka:
        poz = kolejka.popleft()
        if poz == cel:
            sciezka = []
            while rodzic[poz]:
                sciezka.append(rodzic[poz])
                poz = rodzic[poz]
            return sciezka[::-1]
        
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0: continue
                nowa = (poz[0] + dx, poz[1] + dy)
                if 0 <= nowa[0] < n and 0 <= nowa[1] < n and nowa not in odwiedzone and plansza[nowa[0]][nowa[1]] == 0:
                    odwiedzone.add(nowa)
                    rodzic[nowa] = poz
                    kolejka.append(nowa)
    return None

def main() -> None:
    n, k = map(int, input().split())
    plansza = [list(map(int, input().split())) for _ in range(n)]
    docelowa = [input().split() for _ in range(n)]

    pozycje = {}
    cele = {}
    for i in range(n):
        for j in range(n):
            if plansza[i][j] > 0: pozycje[plansza[i][j]] = (i, j)
            if int(docelowa[i][j]) > 0: cele[int(docelowa[i][j])] = (i, j)

    ruchy = []
    for krol in range(1, k + 1):
        if pozycje[krol] == cele[krol]: continue
        sciezka = bfs(pozycje[krol], cele[krol], plansza, n)
        if not sciezka:
            print("NIE")
            exit()
        for x, y in sciezka:
            ruchy.append((krol, x + 1, y + 1))
            plansza[pozycje[krol][0]][pozycje[krol][1]] = 0
            plansza[x][y] = krol
            pozycje[krol] = (x, y)

    print("TAK")
    print(len(ruchy))
    for ruch in ruchy: print(*ruch)
if __name__ == "__main__": main()
"""


# ________________________________________________________________________ #
"""
**************************
_  Tura I | 09.11.2025   _
~~~~~~~~~dos.pdf~~~~~~~~~~
- Grzegorz Tereszkiewicz -
************************** 
"""


"""
from collections import deque
def wyznacz_odleglosci(n: int, zablokowane: list[bool], start_indeks: int) -> tuple[list[int], int]:
    N = n * n
    odleglosci = [-1] * N
    odleglosci[start_indeks] = 0
    kolejka = deque([start_indeks])
    najwieksza = 0
    while kolejka:
        pole = kolejka.popleft()
        nowa = odleglosci[pole] + 1
        r = pole // n
        c = pole - r * n
        if c > 0:
            s = pole - 1
            if odleglosci[s] == -1 and not zablokowane[s]:
                odleglosci[s] = nowa
                kolejka.append(s)
                if nowa > najwieksza: najwieksza = nowa
        if c + 1 < n:
            s = pole + 1
            if odleglosci[s] == -1 and not zablokowane[s]:
                odleglosci[s] = nowa
                kolejka.append(s)
                if nowa > najwieksza: najwieksza = nowa
        if r > 0:
            s = pole - n
            if odleglosci[s] == -1 and not zablokowane[s]:
                odleglosci[s] = nowa
                kolejka.append(s)
                if nowa > najwieksza: najwieksza = nowa
        if r + 1 < n:
            s = pole + n
            if odleglosci[s] == -1 and not zablokowane[s]:
                odleglosci[s] = nowa
                kolejka.append(s)
                if nowa > najwieksza: najwieksza = nowa
    return odleglosci, najwieksza

def zbuduj_czestosci_fortow(jest_fort: list[bool], odleglosci: list[int], najwieksza: int) -> tuple[list[int], int]:
    czestosci = [0] * (najwieksza + 1)
    liczba_fortow = 0
    for i, stan in enumerate(jest_fort):
        if stan:
            d = odleglosci[i]
            czestosci[d] += 1
            liczba_fortow += 1
    return czestosci, liczba_fortow

def policz_wynik_z_czestosci(czestosci: list[int]) -> int:
    if sum(czestosci) == 0: return 0
    najlepszy = 0
    sufiks = 0
    for d in range(len(czestosci) - 1, -1, -1):
        sufiks += czestosci[d]
        k = d + sufiks - 1
        if k > najlepszy: najlepszy = k
    return najlepszy

def przelacz_fort(x: int, y: int, n: int, jest_fort: list[bool], odleglosci: list[int], czestosci: list[int]) -> int:
    i = (x - 1) * n + (y - 1)
    d = odleglosci[i]
    if jest_fort[i]:
        jest_fort[i] = False
        czestosci[d] -= 1
        return -1
    else:
        jest_fort[i] = True
        czestosci[d] += 1
        return +1

def wczytaj_zmiany(q: int) -> list[tuple[int, int]]:
    zmiany: list[tuple[int, int]] = []
    while len(zmiany) < q:
        w = input()
        if not w: continue
        p = w.strip().split()
        if len(p) < 2: continue
        x, y = int(p[0]), int(p[1])
        zmiany.append((x, y))
    return zmiany

def main() -> None:
    pierwsza = ""
    while not pierwsza:
        pierwsza = input().strip()
    n_str, q_str = pierwsza.split()
    n = int(n_str)
    q = int(q_str)

    plansza: list[str] = []
    while len(plansza) < n:
        w = input()
        if not w: continue
        plansza.append(w.strip())
    zmiany = wczytaj_zmiany(q)

    N = n * n
    zablokowane = [False] * N
    jest_fort = [False] * N
    start = 0

    for r in range(n):
        w = plansza[r]
        b = r * n
        for c in range(n):
            ch = w[c]
            i = b + c
            if ch == '#': zablokowane[i] = True
            elif ch == 'F': jest_fort[i] = True
            elif ch == 'Z': start = i

    odleglosci, najw = wyznacz_odleglosci(n, zablokowane, start)
    czestosci, liczba_fortow = zbuduj_czestosci_fortow(jest_fort, odleglosci, najw)

    wyniki: list[int] = []
    wyniki.append(policz_wynik_z_czestosci(czestosci))
    for x, y in zmiany:
        liczba_fortow += przelacz_fort(x, y, n, jest_fort, odleglosci, czestosci)
        wyniki.append(policz_wynik_z_czestosci(czestosci))

    print("\n".join(map(str, wyniki)))

if __name__ == "__main__":main()
"""

# ________________________________________________________________________ #

import sys
from math import gcd

"""
**************************
_  Tura I | 10.11.2025   _
~~~~~~~~~laz.pdf~~~~~~~~~~
- Grzegorz Tereszkiewicz -
************************** 
"""

import sys
from math import gcd

def generuj_sekwencje(n: int, m: int) -> tuple[int, str]:
    nwd = gcd(n, m)
    k = max(2, nwd)
    mozliwe_a = []
    for a in range(1, k):
        if gcd(a, n) == 1 and gcd(k - a, m) == 1: mozliwe_a.append(a)
    if not mozliwe_a:
        ruch1 = "D" if n <= m else "P"
        ruch2 = "P" if n <= m else "D"
        ciag = ""
        for i in range(k):
            if i % 2 == 0: ciag += ruch1
            else: ciag += ruch2
        return k, ciag
    if n > m: a = max(mozliwe_a)
    else: a = min(mozliwe_a)
    b = k - a
    pion = "D"
    poziom = "P"
    if a > b: ciag = pion * a + poziom * b
    else: ciag = poziom * b + pion * a
    return k, ciag

def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    k, sekwencja = generuj_sekwencje(n, m)
    sys.stdout.write(f"{k}\n")
    sys.stdout.write(f"{sekwencja}\n")

if __name__ == "__main__":
    main()



# ____________________________________KONIEC____________________________________ #