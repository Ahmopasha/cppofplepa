---
cilt: "II — İleri"
kisim: "15 — Eşzamanlılık"
baslik: "15.6 `std::async`"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 15.6 `std::async`

`promise` ve `future` nesneleriyle uğraşmadan aynı işi yapar.

```cpp
std::future<int> f = std::async(std::launch::async, [] { return 42; });
int sonuc = f.get();
```

**Başlatma ilkesi** *(launch policy)* için standart iki değer tanımlar. Değerler bir bit
maskesidir, birleştirilebilir, ve gerçekleme ek değerler tanımlayabilir. İlke **açıkça
yazılmalıdır**:

| İlke | Davranış |
|---|---|
| `std::launch::async` | Sanki yeni bir iş parçacığında çalışır |
| `std::launch::deferred` | İlk `get()` ya da `wait()` çağrısına kadar çalışmaz, sonra o çağrıyı yapan iş parçacığında çalışır; `wait_for` ve `wait_until` onu çalıştırmaz |

İlke yazılmazsa çağrı `std::launch::async | std::launch::deferred` ile aynıdır ve seçim
**gerçeklemeye bırakılır**. Seçim çalışma anında da yapılabilir; kodunuz eşzamanlı
çalışmayabilir.

Bir tuzağı daha vardır: `std::launch::async` ile (ya da birden çok ilke verildiğinde veya
ilke yazılmadığında gerçeklemenin `async`'i seçmesiyle) başlatılmış ve henüz bitmemiş bir
işin son `future` nesnesi yok edilirken **sonlandırıcı işlev işin bitmesini bekler.**
(`std::launch::deferred` ile başlatılan işi sonlandırıcı işlev çalıştırmaz; daha önce
`get()` ya da `wait()` çağrılmadıysa iş hiç çalışmaz.) `std::launch::async` ile yapılan
bir `std::async` çağrısının döndürdüğü `future`'ı bir değişkende tutmazsanız geçici
`future` hemen yok olur ve satır, iş bitene kadar bekler:

<!-- kod-baglam
void is();
-->
```cpp
std::async(std::launch::async, is);     // eşzamanlı DEĞİL — bu satır bekler
auto f = std::async(std::launch::async, is);   // doğrusu
```
