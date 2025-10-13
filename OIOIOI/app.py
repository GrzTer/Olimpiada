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

################################################################################################
"""
**************************
_  Tura I | 13.10.2025   _
~~~~~~~~~rpk.pdf~~~~~~~~~~
~~~~   n = 3a + 8b    ~~~~
~ min_b = (2(n % 3) % 3) ~
- Grzegorz Tereszkiewicz -
************************** 
"""

# def sil(ciezar: int) -> str:
#     mod = ciezar % 3
#     min_b = (2 * mod) % 3
#     return "TAK" if ciezar >= 8 * min_b else "NIE"

# def main() -> None:
#     n, m = map(int, input().split())
#     print(sil(n))

# if __name__ == "__main__":
#     main()

