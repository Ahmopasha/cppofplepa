---
cilt: "II — İleri"
kisim: "3 — Kopyalama Eliminasyonu"
baslik: "3.5 Eliminasyonu engelleyen yazımlar"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 3.5 Eliminasyonu engelleyen yazımlar

Üçü de iyi niyetle yazılır, üçü de zarar verir; biri eliminasyonu değil taşımayı engeller.
Kuralları Cilt I, Kısım 13.12'de; burada sebepleri.

**`return std::move(mx);`** — Dönüş ifadesi artık yerel nesnenin *ismi* değil, bir işlev
çağrısıdır. NRVO'nun ön koşulu ortadan kalkar, eliminasyon yapılamaz ve taşıyan kurucu
işlev çağrılır. Hiçbir şey yapmamak, taşımaktan ucuzdur.

**Geri dönüş türünü `const T` yapmak** — Eliminasyonu engellemez: `Myclass m = foo();`
yine zorunlu eliminasyondur, `foo` içindeki `return mx;` de NRVO'ya uygundur. Engellediği
şey taşımadır: `const T` bir değer `T&&` parametresine bağlanamaz. `m = foo();` gibi bir
atamada taşıyan atama yerine `const T&` parametreli kopyalayan atama seçilir (Kısım 2.7).

**Birden fazla yerel nesneden koşullu dönüş** — `return b ? a : c;` deyiminin operandı bir
nesnenin adı değil, bir koşul ifadesidir. Bu yüzden NRVO uygulanamaz. Örtülü taşıma da
aynı nedenle uygulanmaz; ifade bir L-Value olduğu için dönüş nesnesi kopyalanarak kurulur.

```cpp
Myclass baz(bool b)
{
    Myclass a, c;
    return b ? a : c;      // NRVO yok, kopyalanır
}
```

Aynı mantığı `if (b) return a; return c;` biçiminde yazarsanız her `return` bir ad
döndürür: standart iki dönüş için de NRVO'ya izin verir, yapılmazsa örtülü taşıma çalışır.

İki ek durum, tuzak olmasa da bilinmelidir. **Değerle alınan parametreyi döndürmek**:
parametre de otomatik ömürlüdür, ama standart parametreleri NRVO'dan açıkça dışlar;
örtülü taşıma ise çalışır.
**Bir veri elemanını döndürmek**: ne NRVO ne örtülü taşıma uygulanır; nesne hâlâ
sahibine aittir, dolayısıyla kopyalanır. Kaynağını gerçekten devretmek istiyorsanız
burada `std::move` yazmak doğrudur.
