# ________________________________________________________________________ #

"""
**************************
_  Tura I | 02.11.2025   _
~~~~~~~~~rpk.pdf~~~~~~~~~~
************************** 
"""


def znajdz_sciezke(siatka: list[list[int]], n: int, m: int) -> list[tuple[int, int, int]] | None:
    """
    Problem: znaleźć ścieżkę odwiedzającą wszystkie niezerowe komórki.
    Możemy poruszać się tylko w tym samym wierszu lub kolumnie (jak wieża w szachach).
    Trzeci parametr w outputcie to wartość z niezerowej komórki, którą "bierzemy" w danym kroku.
    """
    
    # Zbieramy wszystkie niezerowe komórki
    komorki_niezerowe = []
    for i in range(n):
        for j in range(m):
            if siatka[i][j] != 0:
                komorki_niezerowe.append((i + 1, j + 1, siatka[i][j]))
    
    if not komorki_niezerowe:
        return None
    
    # Sortujemy według wartości (wartość, wiersz, kolumna)
    komorki_posortowane = sorted(komorki_niezerowe, key=lambda x: (x[2], x[0], x[1]))
    
    sciezka = []
    obecna_pozycja = None
    wartosci_dostepne = [k[2] for k in komorki_posortowane]
    indeks_wartosci = 0
    
    # Odwiedzamy wszystkie niezerowe komórki w kolejności posortowanej
    for komorka in komorki_posortowane:
        i_docelowe, j_docelowe, wartosc = komorka
        
        if obecna_pozycja is None:
            # Zaczynamy od pierwszej komórki niezerowej
            wartosc_do_uzu = wartosci_dostepne[indeks_wartosci % len(wartosci_dostepne)]
            sciezka.append((i_docelowe, j_docelowe, wartosc_do_uzu))
            obecna_pozycja = (i_docelowe, j_docelowe)
            indeks_wartosci += 1
        else:
            i_obecne, j_obecne = obecna_pozycja
            
            # Generujemy ścieżkę z obecnej pozycji do docelowej (ruch jak wieża)
            if i_obecne == i_docelowe:
                # Jesteśmy w tym samym wierszu - idziemy poziomo
                start_j = j_obecne + 1 if j_obecne < j_docelowe else j_obecne - 1
                end_j = j_docelowe + 1 if j_obecne < j_docelowe else j_docelowe - 1
                step = 1 if j_obecne < j_docelowe else -1
                
                for j_curr in range(start_j, end_j, step):
                    wartosc_do_uzu = wartosci_dostepne[indeks_wartosci % len(wartosci_dostepne)]
                    sciezka.append((i_obecne, j_curr, wartosc_do_uzu))
                    indeks_wartosci += 1
            elif j_obecne == j_docelowe:
                # Jesteśmy w tej samej kolumnie - idziemy pionowo
                start_i = i_obecne + 1 if i_obecne < i_docelowe else i_obecne - 1
                end_i = i_docelowe + 1 if i_obecne < i_docelowe else i_docelowe - 1
                step = 1 if i_obecne < i_docelowe else -1
                
                for i_curr in range(start_i, end_i, step):
                    wartosc_do_uzu = wartosci_dostepne[indeks_wartosci % len(wartosci_dostepne)]
                    sciezka.append((i_curr, j_obecne, wartosc_do_uzu))
                    indeks_wartosci += 1
            else:
                # Ruch w dwóch krokach: najpierw poziomo, potem pionowo
                # Najpierw idziemy do pozycji (i_obecne, j_docelowe)
                start_j = j_obecne + 1 if j_obecne < j_docelowe else j_obecne - 1
                end_j = j_docelowe + 1 if j_obecne < j_docelowe else j_docelowe - 1
                step_j = 1 if j_obecne < j_docelowe else -1
                
                for j_curr in range(start_j, end_j, step_j):
                    wartosc_do_uzu = wartosci_dostepne[indeks_wartosci % len(wartosci_dostepne)]
                    sciezka.append((i_obecne, j_curr, wartosc_do_uzu))
                    indeks_wartosci += 1
                
                # Potem idziemy do (i_docelowe, j_docelowe)
                start_i = i_obecne + 1 if i_obecne < i_docelowe else i_obecne - 1
                end_i = i_docelowe + 1 if i_obecne < i_docelowe else i_docelowe - 1
                step_i = 1 if i_obecne < i_docelowe else -1
                
                for i_curr in range(start_i, end_i, step_i):
                    wartosc_do_uzu = wartosci_dostepne[indeks_wartosci % len(wartosci_dostepne)]
                    sciezka.append((i_curr, j_docelowe, wartosc_do_uzu))
                    indeks_wartosci += 1
            
            obecna_pozycja = (i_docelowe, j_docelowe)
    
    return sciezka if sciezka else None


def rozwiaz(siatka: list[list[int]], n: int, m: int) -> tuple[bool, list[tuple[int, int, int]]]:
    sciezka = znajdz_sciezke(siatka, n, m)
    
    if sciezka is None:
        return False, []
    
    return True, sciezka


def main() -> None:
    m, n = map(int, input().split())  # m = kolumny, n = wiersze
    
    siatka = []
    for _ in range(n):
        wiersz = list(map(int, input().split()))
        siatka.append(wiersz[:m])
    
    mozna, sciezka = rozwiaz(siatka, n, m)
    
    if mozna:
        print("TAK")
        print(len(sciezka))
        for krok in sciezka:
            print(f"{krok[0]} {krok[1]} {krok[2]}")
    else:
        print("NIE")
    

if __name__ == "__main__":
    main()
