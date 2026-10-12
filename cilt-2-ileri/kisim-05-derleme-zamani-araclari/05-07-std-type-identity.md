---
cilt: "II — İleri"
kisim: "5 — Derleme Zamanı Araçları"
baslik: "5.7 `std::type_identity`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 5.7 `std::type_identity`

C++20 ile eklendi. Karşılık geldiği türü aynen döndürür; görünürde hiçbir şey yapmaz.

```cpp
template<typename T>
struct type_identity { using type = T; };
```

İşlevi, **tür çıkarımını engellemektir.** Bir şablon parametresi `type_identity_t<T>`
içinden geçerse, o parametre çıkarıma katılmaz; çıkarım diğer parametrelerden yapılır.

```cpp
template<typename T>
void func(T a, std::type_identity_t<T> b);

func(1, 2.5);      // T = int; ikinci argüman int'e dönüştürülür
```

`type_identity` olmasaydı `T` ilk argümandan `int`, ikinciden `double` çıkarılır ve
çelişki sentaks hatası verirdi (bkz. Cilt I Kısım 22.2).

Bu tür bağlamlara **çıkarılmayan bağlam** *(non-deduced context)* denir.
