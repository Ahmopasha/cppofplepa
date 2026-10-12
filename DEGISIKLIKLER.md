# Değişiklik kaydı

## Yayımlanmamış

### Yapı

- Kitap, her alt başlık ayrı bir dosya olacak biçimde bölündü (`cilt-1-temel/`,
  `cilt-2-ileri/`). Ciltler ve PDF artık `araclar/derle.py` ile bu dosyalardan derleniyor.
  Bölme kayıpsızdır: geçişsiz derleme, bu sayfada sayılan değişiklikler dışında
  Sürüm 1.0'ın metnini harfi harfine verir.
- Kısımlar arasına ve iki cilt arasına geçiş paragrafları eklendi (`gecisler/`). Cilt I
  artık "Cilt I'den Cilt II'ye" başlıklı kısa bir kapanışla bitiyor; Cilt II'nin ön
  metnine, bölümlerinin Cilt I'deki karşılıklarını gösteren bir tablo eklendi.
- Cilt II'de, bölüm dosyaları birleştirilirken kalmış üç fazla yatay çizgi kaldırıldı
  (1.1 ile 1.2 arası, Kısım 2 ve Kısım 6 sonu).

### Düzeltmeler

- Cilt I 6.6: `constexpr` kısıtlarının gevşemesi ile `consteval` ve `constinit` için
  verilen atıf Cilt II Kısım 16'yı gösteriyordu; doğrusu Kısım 18.
- Cilt I 15.5: `operator new` / `operator delete` yüklemesi, `placement new` ve
  `std::set_new_handler` için verilen atıf Cilt II Kısım 16'yı gösteriyordu; doğrusu
  Kısım 17.
- Cilt II 8.7: Kısım 14'te bulunmayan bir "pipeline operator" deyimine yapılan atıf
  kaldırıldı.
- Cilt II ön metni: "karşılığını bilindiği varsayar" → "karşılığının bilindiğini
  varsayar".

## Sürüm 1.0 — Eylül 2026

İlk yayım.
