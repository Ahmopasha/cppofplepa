---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.1.6 İşlev yükleme çözümlemesindeki rolü"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

### 1.1.6 İşlev yükleme çözümlemesindeki rolü

Kategori, hangi yüklemenin seçileceğini belirler. Dört yüklemenin bulunduğu durumda
tercih sırası (1 en yüksek, X bağlanamaz):

| Argümanın kategorisi | `T&` | `const T&` | `T&&` | `const T&&` |
|---|:---:|:---:|:---:|:---:|
| L-Value | 1 | 2 | X | X |
| const L-Value | X | 1 | X | X |
| R-Value | X | 3 | 1 | 2 |
| const R-Value | X | 2 | X | 1 |

```cpp
struct S {};

void foo(S&)        { std::cout << "S&\n"; }
void foo(const S&)  { std::cout << "const S&\n"; }
void foo(S&&)       { std::cout << "S&&\n"; }
void foo(const S&&) { std::cout << "const S&&\n"; }

int main()
{
    S x;            foo(x);              // S&
    const S cx;     foo(cx);             // const S&
                    foo(S{});            // S&&
                    foo(std::move(cx));  // const S&&
}
```

Tablodan çıkan tasarım kuralı, Cilt I, Kısım 2.4.6'daki tavsiyenin gerekçesidir:
`const T&` her şeye bağlandığı için güvenli varsayılandır, `T&&` ise yalnızca kaynağı
devralınabilir olanları yakalar.

`const T&&` yüklemesi pratikte nadiren yazılır. Yazıldığı yer, `const` bir nesnenin
taşınmaya çalışıldığı durumu ayırt etmek istediğiniz zamandır.
