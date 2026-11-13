---
cilt: "I — Temel"
kisim: "16 — Tür Eş İsimleri ve İsim Alanları"
baslik: "16.3 `using` bildirimi ve `using` direktifi"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 16.3 `using` bildirimi ve `using` direktifi

İki ayrı araçtır ve karıştırılmaları yaygındır.

**`using` bildirimi** *(using declaration)* adını açıkça yazdığınız ismi mevcut kapsama
taşır (C++17'den itibaren virgülle birden fazla isim yazılabilir):

```cpp
using std::cout;
cout << "merhaba";      // artık nitelemeye gerek yok
```

**`using` direktifi** *(using directive)* isim alanındaki bütün isimleri görünür kılar:

```cpp
using namespace std;
```

> **Başlık dosyasında isim alanı kapsamında (global ya da bir isim alanı içinde) `using
> namespace` direktifini asla kullanmayın.** O başlığı dahil eden her dosya (direktif
> bir isim alanı içindeyse, o isim alanını kullanan her kod), isteyip istemediğine
> bakılmaksızın bütün isimleri kapsamına almış olur. Bu, isim alanlarının varlık
> sebebini ortadan kaldırır ve çözülmesi zor çakışmalara yol açar.

Kaynak dosyalarda ve işlev gövdelerinde kullanımı kabul edilebilir, ama `using` bildirimi
neredeyse her zaman daha iyidir: neyi getirdiğiniz koddan okunur.
