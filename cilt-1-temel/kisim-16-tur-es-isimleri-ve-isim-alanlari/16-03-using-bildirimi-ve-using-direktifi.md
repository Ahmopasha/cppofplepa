---
cilt: "I — Temel"
kisim: "16 — Tür Eş İsimleri ve İsim Alanları"
baslik: "16.3 `using` bildirimi ve `using` direktifi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 16.3 `using` bildirimi ve `using` direktifi

İki ayrı araçtır ve karıştırılmaları yaygındır.

**`using` bildirimi** tek bir ismi mevcut kapsama taşır:

```cpp
using std::cout;
cout << "merhaba";      // artık nitelemeye gerek yok
```

**`using` direktifi** isim alanındaki bütün isimleri görünür kılar:

```cpp
using namespace std;
```

> **`using namespace` direktifini başlık dosyasında asla kullanmayın.** O başlığı dahil
> eden her dosya, isteyip istemediğine bakılmaksızın bütün isimleri kapsamına almış olur.
> Bu, isim alanlarının varlık sebebini ortadan kaldırır ve çözülmesi zor çakışmalara yol
> açar.

Kaynak dosyalarda ve işlev gövdelerinde kullanımı kabul edilebilir, ama `using` bildirimi
neredeyse her zaman daha iyidir: neyi getirdiğiniz koddan okunur.
