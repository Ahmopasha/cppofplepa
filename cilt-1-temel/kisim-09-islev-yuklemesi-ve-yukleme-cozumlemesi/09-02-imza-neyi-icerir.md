---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.2 İmza neyi içerir"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 9.2 İmza neyi içerir

| İmzanın parçası | İmzanın parçası değil |
|---|---|
| İşlev ismi | Geri dönüş türü |
| Parametre türleri ve sırası | Parametre isimleri |
| Üye işlevlerde `const`luk | Değer parametrelerdeki üst düzey `const` |
| Üye işlevlerde referans niteleyicisi | Varsayılan argümanlar |

Geri dönüş türünün imzaya dahil olmaması önemlidir:

```cpp
int  func(int);
double func(int);      // sentaks hatası — yeniden bildirim sayılır
```

Değer parametrelerdeki üst düzey `const` de yok sayılır:

```cpp
void func(int);
void func(const int);  // sentaks hatası — aynı imza
```

Ama referans ve göstericilerde `const` imzanın parçasıdır:

```cpp
void func(int&);
void func(const int&); // geçerli yükleme
```
