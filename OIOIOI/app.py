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
from collections import deque

"""
**************************
_  Tura I | 13.10.2025   _
~~~~~~~~~han.pdf~~~~~~~~~~
- Grzegorz Tereszkiewicz -
************************** 
"""

class Hanoj:
    def __init__(self, ilosc_klockow: int, ilosc_stosow: int )-> None:
        self.ilosc_klockow = ilosc_klockow
        self.ilosc_stostow= ilosc_stosow
        self.stosy = [deque(map(int, input().split()[1:])) for _ in range(ilosc_stosow)]

    def han(self) -> None:
        stos_z_1 = -1
        for i in range(self.ilosc_stostow):
            if self.stosy[i] and self.stosy[i][0] == 1:
                stos_z_1 = i
                break
        if stos_z_1 == -1:
            print (-1)
            return

        stos = self.stosy[stos_z_1]
        k = 1
        for i in range(1, len(stos)):
            if stos[i] != stos[i-1] + i: break
            k +=1
        stos_z_miejscem = k < len(stos)

        pusty = -1
        for i in range(self.ilosc_stostow):
            if not self.stosy[i]:
                pusty = i
                break
        if stos_z_miejscem:
            if pusty == -1:
                print(-1)
                return
            cel = pusty
            oczekiwano = 1
            obecny_max = 0
        else:
            cel = stos_z_1
            oczekiwano = k + 1
            obecny_max = stos[-1]

        gory = {self.stosy[i][0]: i for i in range(self.ilosc_stostow) if self.stosy[i]}

        ruchy = []
        for ocz in range(oczekiwano, self. ilosc_klockow + 1):
            if ocz not in gory:
                print(-1)
                return
            a = gory[ocz]
            if ocz <= obecny_max:
                print(-1)
                return
            ruchy.append((a + 1, cel + 1))
            self.stosy[a].popleft()
            del gory[ocz]
            if self.stosy[a]: gory[self.stosy[a][0]] = a
            obecny_max = ocz
        
        h = len(ruchy)
        print(h)
        for ruch in ruchy: print(ruch[0], ruch[1])

def main() -> None:
    n, m = map(int, input().split())
    han = Hanoj(n, m)
    han.han()

if __name__ == "__main__":
    main()
