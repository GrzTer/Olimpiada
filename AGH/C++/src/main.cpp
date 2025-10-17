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


// ================================
//             Podzialy
// ================================

int main() {
   return 0;
}

/*

// ================================
//             Algebraf
// ================================

int main() {
   return 0;
}

*/