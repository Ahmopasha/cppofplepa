---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.6 `std::async`"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 15.6 `std::async`

`promise` ve `future` nesneleriyle uğraşmadan aynı işi yapar.

```cpp
std::future<int> f = std::async(std::launch::async, [] { return 42; });
int sonuc = f.get();
```

Çalıştırma ilkesi iki değer alır ve **açıkça yazılmalıdır**:

| İlke | Davranış |
|---|---|
| `std::launch::async` | Yeni iş parçacığında hemen başlar |
| `std::launch::deferred` | `get()` çağrılana kadar hiç çalışmaz, sonra çağıran iş parçacığında çalışır |

İlke yazılmazsa seçim **gerçeklemeye bırakılır**; derleyici ikisinden birini seçebilir ve
kodunuz eşzamanlı çalışmayabilir.

Bir tuzağı daha vardır: `std::async` ile elde edilen `future` nesnesinin **sonlandırıcı
işlevi bloklar.** Dönüş değerini bir değişkende tutmazsanız geçici nesne hemen yok olur
ve satır, iş bitene kadar bekler:

<!-- kod-baglam
void is();
-->
```cpp
std::async(std::launch::async, is);     // eşzamanlı DEĞİL — bu satır bekler
auto f = std::async(std::launch::async, is);   // doğrusu
```
