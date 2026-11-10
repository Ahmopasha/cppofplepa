---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.2 İmza neyi içerir"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 9.2 İmza neyi içerir

| İmzanın parçası | İmzanın parçası değil |
|---|---|
| İşlev ismi ve bulunduğu isim alanı (Kısım 16.2); üye işlevlerde üyesi olduğu sınıf (Kısım 12) | Geri dönüş türü (şablon olmayan işlevlerde; şablonlar: Kısım 22.2) |
| Parametre türleri ve sırası | Parametre isimleri |
| Üye işlevlerde `const`luk (Kısım 12.7) | Değer parametrelerdeki üst düzey `const` |
| Üye işlevlerde referans niteleyicisi (Cilt II, Kısım 16.2) | Varsayılan argümanlar |

Geri dönüş türünün imzaya dahil olmaması önemlidir:

```cpp
int  func(int);
double func(int);      // sentaks hatası — yalnızca geri dönüş türü farklı
```

Değer parametrelerdeki üst düzey `const` da yok sayılır. Aşağıdaki iki bildirim yükleme
oluşturmaz; ikisi de aynı işlevi bildirir. **Bu örnekte sentaks hatası ancak aynı işlev
ikinci kez tanımlandığında çıkar:**

```cpp
void func(int);
void func(const int);         // geçerli — aynı işlevin yeniden bildirimi

void func(const int x) { }    // geçerli — ilk tanım
void func(int x) { }          // sentaks hatası — aynı işlev ikinci kez tanımlanıyor
```

Tanımdaki `const` yalnızca gövdenin içini ilgilendirir: o gövdede `x` değiştirilemez.

Ama referanslarda ve göstericinin gösterdiği nesnede `const` imzanın parçasıdır
(göstericinin kendi `const`u üst düzeydir, yok sayılır):

```cpp
void func(int&);
void func(const int&); // geçerli yükleme
```
