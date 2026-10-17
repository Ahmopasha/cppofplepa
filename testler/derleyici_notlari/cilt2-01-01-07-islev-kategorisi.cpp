// Derleyici Notu testi: Cilt II 1.1.7
// Kutunun iddiası: işlevler hangi referans türüne dönüştürülürse dönüştürülsün L-Value
// kalır; MSVC ise std::move(foo) gibi bir ifade için X-Value bildirir.
// tur: cikti
// kipler: c++23
// beklenti: clang=L-Value gcc=L-Value msvc=X-Value
#include <iostream>
#include <utility>

template<typename T>
constexpr const char* p = "PR-Value";

template<typename T>
constexpr const char* p<T&> = "L-Value";

template<typename T>
constexpr const char* p<T&&> = "X-Value";

void foo() { }

int main()
{
    std::cout << p<decltype((std::move(foo)))> << '\n';
}
