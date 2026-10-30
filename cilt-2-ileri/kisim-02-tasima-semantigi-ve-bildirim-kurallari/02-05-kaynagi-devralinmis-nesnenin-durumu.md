---
cilt: "II — İleri"
kisim: "2 — Taşıma Semantiği ve Bildirim Kuralları"
baslik: "2.5 Kaynağı devralınmış nesnenin durumu"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 2.5 Kaynağı devralınmış nesnenin durumu

Standart kütüphane türleri için verilen garanti, aksi belirtilmedikçe, **geçerli ama
belirtilmemiş bir durumdur.** Bazı türlerde durum belirtilmiştir; örneğin başka bir
nesneye taşınmış `std::unique_ptr` boştur.

Geçerli ama belirtilmemiş durumun pratik karşılığı üç maddedir. Nesnenin sonlandırıcı
işlevi güvenle çalışır. Tür atamayı destekliyorsa nesneye yeni bir değer atayabilirsiniz.
Ön koşulu olmayan işlemler (bir `vector` için `size()`, `empty()`, `clear()`) çağrılabilir
ve türü için belirtildiği gibi davranır; ön koşulu nesnenin değerine bağlı işlemlerden
(`front()`, `pop_back()`) önce ise bu koşul denetlenmelidir.

```cpp
std::string s(10000, 'A');
auto t = std::move(s);

s.size();          // tanımlı ama değeri garanti edilmiyor
s = "yeni";        // geçerli
std::cout << s;    // artık okunabilir
```

Aynı durum, elemanları taşıyarak kaydıran algoritmaların geride bıraktığı elemanlar için
de geçerlidir; örneğin `std::remove` sonrasında aralığın sonundakiler (Cilt I Kısım 23.7).

Kendi sınıfınızı yazarken aynı garantiyi vermeniz beklenir. "Kaynağı bırak" adımını
atlamak yalnızca çift serbest bırakma sorunu değil, bu sözleşmenin de ihlalidir.

Üçüncü parti kütüphaneler bu garantiyi vermek zorunda değildir.
