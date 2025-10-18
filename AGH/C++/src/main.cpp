#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
using namespace std;
/*
vector<string> zbierz_wszystkie_linie(const vector<string>& plansza, int rozmiar_N);
bool jest_palindrom(const string& s);
vector<string> zbierz_wszystkie_palindromy(const vector<string>& linie, int min_dlugosc);
string znajdz_rozwiazanie(const vector<string>& palindromy, int min_liczba_wystapien);

// ================================
//             Palindrom
// ================================

bool jest_palindrom(const string& s) {
    int l = 0, r = (int)s.size() - 1;
    while (l < r) if (s[l++] != s[r--]) return false;
    return true;
}

vector<string> zbierz_wszystkie_linie(const vector<string>& plansza, int rozmiar_N) {
    vector<string> linie;

    linie.insert(linie.end(), plansza.begin(), plansza.end());

    for (int kolumna = 0; kolumna < rozmiar_N; ++kolumna) {
        string linia; linia.reserve(rozmiar_N);
        for (int wiersz = 0; wiersz < rozmiar_N; ++wiersz)
            linia.push_back(plansza[wiersz][kolumna]);
        linie.push_back(std::move(linia));
    }

    for (int przesuniecie = 1 - rozmiar_N; przesuniecie < rozmiar_N; ++przesuniecie) {
        string linia;
        for (int wiersz = 0; wiersz < rozmiar_N; ++wiersz) {
            int kolumna = wiersz - przesuniecie;
            if (0 <= kolumna && kolumna < rozmiar_N) linia.push_back(plansza[wiersz][kolumna]);
        }
        if (!linia.empty()) linie.push_back(std::move(linia));
    }

    for (int suma = 0; suma < 2 * rozmiar_N - 1; ++suma) {
        string linia;
        for (int wiersz = 0; wiersz < rozmiar_N; ++wiersz) {
            int kolumna = suma - wiersz;
            if (0 <= kolumna && kolumna < rozmiar_N) linia.push_back(plansza[wiersz][kolumna]);
        }
        if (!linia.empty()) linie.push_back(std::move(linia));
    }
    return linie;
}

vector<string> zbierz_wszystkie_palindromy(const vector<string>& linie, int min_dlugosc) {
    vector<string> wynik;
    for (const string& linia : linie) {
        int L = (int)linia.size();
        for (int dl = max(min_dlugosc, 1); dl <= L; ++dl) {
            for (int i = 0; i + dl <= L; ++i) {
                string frag = linia.substr(i, dl);
                if (jest_palindrom(frag)) wynik.push_back(std::move(frag));
            }
        }
    }
    return wynik;
}

string znajdz_rozwiazanie(const vector<string>& palindromy, int min_liczba_wystapien) {
    unordered_map<string, int> licznik;
    for (const auto& p : palindromy) ++licznik[p];

    unordered_set<string> widziane;
    for (const auto& p : palindromy) {
        if (!widziane.insert(p).second) continue;
        if (licznik[p] >= min_liczba_wystapien) return p;
    }
    return "";
}

int main() {
    int rozmiar_N;
    cin >> rozmiar_N;
    vector<string> plansza(rozmiar_N);
    for (int i = 0; i < rozmiar_N; ++i) cin >> plansza[i];

    vector<string> linie = zbierz_wszystkie_linie(plansza, rozmiar_N);
    vector<string> palindromy = zbierz_wszystkie_palindromy(linie, 5);
    string rozwiazanie = znajdz_rozwiazanie(palindromy, 2);

    cout << rozwiazanie << '\n';
    return 0;
}
*/
/*
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

// ================================
//             Skoczek
// ================================

int minimalna_liczba_skokow(const vector<int>& napoje) {
    int dlugosc_N = (int)napoje.size();

    if (dlugosc_N == 0) return -1;
    if (dlugosc_N == 1) return 0;

    unordered_map<int, int> warstwa{ {0, napoje[0] } }, nowa_warstwa;
    int skoki = 0;

    while (!warstwa.empty()) {
        ++skoki; nowa_warstwa.clear();

        for (auto& para : warstwa) {
            int pozycja = para.first, energia = para.second;
            int maks_skok = min(energia, dlugosc_N - 1 - pozycja);

            for (int zasieg = 1; zasieg <= maks_skok; ++zasieg) {
                int nowa_pozycja = pozycja + zasieg;
                int energia_po_skoku = energia - zasieg + napoje[nowa_pozycja];

                if (nowa_pozycja == dlugosc_N - 1) return skoki;

                if (energia_po_skoku > nowa_warstwa[nowa_pozycja]) nowa_warstwa[nowa_pozycja] = energia_po_skoku;
            }
        }
        warstwa.swap(nowa_warstwa);
    }
    return -1;
}


int main() {
    int N;
    cin >> N;
    vector<int> napoje(N);
    for (int i = 0; i < N; ++i) cin >> napoje[i];

    int wynik = minimalna_liczba_skokow(napoje);
    if (wynik < 0) cout << "BRAK\n";
    else cout << wynik << '\n';

    return 0;
}
*/
/*
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <unordered_set>
#include <algorithm>
#include <stdexcept>

using namespace std;
// ================================
//             Podzialy
// ================================

bool czy_jest_pierwsza(long long liczba){
    if (liczba < 2) return false;
    for (long long i = 2; i * i <= liczba; ++i) if (liczba % i == 0) return false;
    return true;
}

bool czy_cyfry_sa_unikalne(const string& fragment) {
    unordered_set<char> cyfry;
    for (char c : fragment) {
        if (cyfry.count(c)) return false;
        cyfry.insert(c);
    }
    return true;
}

int znajdz_minimalny_podzial(const string& ciag_cyfr) {
    int dlugosc = ciag_cyfr.size();
    int nieskonczonosc = dlugosc + 1;
    vector<int> min_kawalkow(dlugosc + 1, nieskonczonosc);
    min_kawalkow[0] = 0;

    for (int i = 1; i <= dlugosc; i++){
        for (int j = 0; j < i; j++){
            if (min_kawalkow[j] == nieskonczonosc) continue;
            string fragment = ciag_cyfr.substr(j, i - j);

            if (fragment.size() > 1 && fragment[0] == '0') continue;
            if (czy_cyfry_sa_unikalne(fragment)) {
            long long liczba = stoll(fragment);

            if (czy_jest_pierwsza(liczba)) min_kawalkow[i] = min(min_kawalkow[i], min_kawalkow[j] + 1);
            }
        }
    }
    return min_kawalkow[dlugosc] > dlugosc ? -1 : min_kawalkow[dlugosc];
}

int main() {
    string ciag; cin >> ciag;
    int wynik = znajdz_minimalny_podzial(ciag);
    
    if (wynik == -1 || wynik < 2) {
        cout << "BRAK\n";
    } else {
        cout << wynik << '\n';
    }

    return 0;
}
*/
// /*
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include <algorithm>

using namespace std;

// ================================
//             Algebraf
// ================================

string zmien_na_liczbe(const string& slowo, const unordered_map<char, int>& mapa) {
    string tekst_liczby;
    for (char litera : slowo) tekst_liczby += '0' + mapa.at(litera);
    return tekst_liczby;
}

bool sprawdz_przypisanie (const vector<tuple<string, string, string>>& rownania, const unordered_map<char, int>& mapa) {
    for (const auto& eq : rownania) {
        string arg1s, arg2s, wyniks;
        tie(arg1s, arg2s, wyniks) = eq;
        long long arg1 = stoll(zmien_na_liczbe(arg1s, mapa));
        long long arg2 = stoll(zmien_na_liczbe(arg2s, mapa));
        long long wynik = stoll(zmien_na_liczbe(wyniks, mapa));
        if (arg1 + arg2 != wynik) return false;
    }
    return true;
}


void rozwiaz_algebraf(int indeks, const vector<tuple<string, string, string>>& rownania, const vector<char>& litery, vector<string>& rozwiazania, vector<int>& przypisania, vector<bool>& uzyte_cyfry) {
    if (indeks == litery.size()) {
        unordered_map<char, int> mapa;
        for (int i = 0; i < litery.size(); ++i) mapa[litery[i]] = przypisania[i];
        if (sprawdz_przypisanie(rownania, mapa)) {
            string rozws;
            for (int cyfra : przypisania) rozws += '0' + cyfra;
            rozwiazania.push_back(rozws);
        }
        return;        
    }
    for (int cyfra = 1; cyfra <= 9; ++cyfra) {
        if (!uzyte_cyfry[cyfra]){
            uzyte_cyfry[cyfra] = true;
            przypisania[indeks] = cyfra;
            rozwiaz_algebraf(indeks + 1, rownania, litery, rozwiazania, przypisania, uzyte_cyfry);
            uzyte_cyfry[cyfra] = false;
        }
    }
}

int main() {
    int liczba_rownan; cin >> liczba_rownan;
    vector<tuple<string, string, string>> rownania;
    set<char> wszystkie_litery;
    
    for (int i = 0; i < liczba_rownan; ++i) {
        string linia; cin >> linia;
        size_t plus_poz = linia.find('+');
        size_t rowna_poz = linia.find('=');
        string arg1 = linia.substr(0, plus_poz);
        string arg2 = linia.substr(plus_poz + 1, rowna_poz - plus_poz - 1);
        string wynik = linia.substr(rowna_poz + 1);
        rownania.push_back(make_tuple(arg1, arg2, wynik));
        for (char c : arg1) wszystkie_litery.insert(c);
        for (char c : arg2) wszystkie_litery.insert(c);
        for (char c : wynik) wszystkie_litery.insert(c);
    }
    
    vector<char> posortowane_litery(wszystkie_litery.begin(), wszystkie_litery.end());
    vector<string> znalezione_rozwiazania;
    vector<int> przypisania (posortowane_litery.size());
    vector<bool> uzyte_cyfry(10, false);
    
    rozwiaz_algebraf(0, rownania, posortowane_litery, znalezione_rozwiazania, przypisania, uzyte_cyfry);
    if (znalezione_rozwiazania.size() == 1) {
        cout << znalezione_rozwiazania[0] << endl;
    } else
    {
        cout << "BRAK" << endl;
    }

    return 0;
}

// */