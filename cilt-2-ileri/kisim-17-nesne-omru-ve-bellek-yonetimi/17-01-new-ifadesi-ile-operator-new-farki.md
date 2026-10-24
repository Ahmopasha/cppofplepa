---
cilt: "II — İleri"
kisim: "17 — Nesne Ömrü ve Bellek Yönetimi"
baslik: "17.1 `new` ifadesi ile `operator new` farkı"
kaynak: "ders notları"
son_kontrol: "2026-10 (C++23)"
---

## 17.1 `new` ifadesi ile `operator new` farkı

Cilt I Kısım 15.2'de `new` ifadesinin iki iş yaptığı söylenmişti: bellek ayırmak ve
nesneyi hayata getirmek. Bu iki işin **ayrı ayrı** özelleştirilebilir olması, bölümün
konusudur.

| Yazım | Ne yapar |
|---|---|
| `new T` | *new ifadesi* — bellek ayırır **ve** kurucu işlevi çağırır |
| `operator new` | Yalnızca ham bellek ayırır; kurucu işlev çağırmaz |

`operator new`, imzası `void* operator new(std::size_t)` olan sıradan bir işlevdir.
`new` ifadesi arka planda onu çağırır. `malloc`'a benzer, ama ondan başlıca üç farkı
vardır: ayırma başarısız olursa, kurulu bir *new handler* varsa onu çağırıp yeniden dener;
new handler yoksa boş gösterici döndürmez, `std::bad_alloc` gönderir (bkz. Kısım 17.4);
program da kendi tanımıyla onun yerini alabilir.

Aynı şekilde `delete` ifadesi önce sonlandırıcı işlevi çağırır, sonra bir
`operator delete` işlevini çağırır: `void operator delete(void*)` ya da boyutu da alan
`void operator delete(void*, std::size_t)`. Global boyutlu biçim C++14'ten itibaren
vardır. Global işlevlerde, tür tamsa tek nesne silinirken boyutlu biçim seçilir; dizi
silmede (`operator delete[]` biçimleri arasında) bu, elemanlar trivial olmayan
sonlandırıcı işlevli bir sınıf türündense geçerlidir. Diğer durumlarda (ör. bir `int`
dizisinin `delete[]` ile silinmesi) hangisinin seçileceği belirtilmemiştir. Sınıf
düzeyindeki biçimler için bkz. Kısım 17.2.
