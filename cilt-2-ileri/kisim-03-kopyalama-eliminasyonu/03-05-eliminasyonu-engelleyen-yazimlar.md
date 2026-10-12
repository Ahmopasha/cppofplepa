---
cilt: "II — İleri"
kisim: "3 — Kopyalama Eliminasyonu"
baslik: "3.5 Eliminasyonu engelleyen yazımlar"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 3.5 Eliminasyonu engelleyen yazımlar

Üçü de iyi niyetle yazılır, üçü de zarar verir. Kuralları Cilt I, Kısım 13.12'de; burada
sebepleri.

**`return std::move(mx);`** — Dönüş ifadesi artık yerel nesnenin *ismi* değil, bir işlev
çağrısıdır. NRVO'nun ön koşulu ortadan kalkar, eliminasyon yapılamaz ve taşıyan kurucu
işlev çağrılır. Hiçbir şey yapmamak, taşımaktan ucuzdur.

**Geri dönüş türünü `const T` yapmak** — Taşıyan işlevin parametresi `T&&`'dir ve
`const T` ona bağlanamaz; `const T&` parametreli kopyalayan işlev seçilir. Taşıma
tamamen devre dışı kalır.

**Birden fazla yerel nesneden koşullu dönüş** — Derleyici hangi nesnenin dönüş yerinde
oluşturulacağını derleme zamanında bilemez:

```cpp
Myclass baz(bool b)
{
    Myclass a, c;
    return b ? a : c;      // NRVO uygulanamaz
}
```

İki ek durum, tuzak olmasa da bilinmelidir. **Değerle alınan parametreyi döndürmek**:
parametre yerel bir nesne olmadığı için NRVO uygulanmaz, ama örtülü taşıma çalışır.
**Bir veri elemanını döndürmek**: ne NRVO ne örtülü taşıma uygulanır; nesne hâlâ
sahibine aittir, dolayısıyla kopyalanır. Kaynağını gerçekten devretmek istiyorsanız
burada `std::move` yazmak doğrudur.
