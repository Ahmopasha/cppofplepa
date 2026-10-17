// Derleyici Notu testi: Cilt II 17.6
// Kutunun iddiası: Clang, referans veri elemanının ilk değer verme listesinde geçici
// nesneye bağlanmasını C++11, C++14, C++17, C++20 ve C++23 kiplerinin hepsinde sentaks
// hatası olarak bildirir; bazı derleyiciler kodu hâlâ kabul eder.
// tur: derleme
// kipler: c++11 c++14 c++17 c++20 c++23
// beklenti: clang=hata gcc=derlenir
#include <string>

class Bozuk {
    const std::string& r;
public:
    Bozuk() : r{std::string{"gecici"}} { }
};

int main() { }
