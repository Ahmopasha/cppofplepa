---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.1.2 Tür ve kategori bağımsız özelliklerdir"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

### 1.1.2 Tür ve kategori bağımsız özelliklerdir

C++ standardı her ifadeyi iki **bağımsız** özellikle tanımlar: bir türü vardır, bir de
değer kategorisi. Bu ikisinin karıştırılması, şablon kodu yazarken en çok hataya yol
açan yerlerden biridir.

**Bir ifadenin türü asla referans olamaz.** Değişkenin türü referans olabilir, ifadenin
türü olamaz.

```cpp
int x = 6;
int& rx = x;

rx = 66;    // buradaki "rx" ifadesinin türü "int&" DEĞİL, "int".
```

Kısıtlama göstericiler için geçerli değildir:

```cpp
int* px = &x;
*px = 99;   // "px" ifadesinin türü "int*".
```

**Değişkenlerin değer kategorisi yoktur, ifadelerin vardır.** Bir bildirim tek başına
ifade oluşturmaz:

```cpp
int x = 31;     // "x" burada ifade oluşturmuyor: kategori yok, tür "int".
int b;
b = x;          // "x" burada ifade: L-Value, tür "int".
b = +x;         // "+x" bir ifade: PR-Value, tür "int".

int&& rr = 10;  // "rr" burada ifade oluşturmuyor: tür "int&&".
+rr;            // "rr" burada ifade: L-Value, tür "int".
                // Referans niteliği düştü; ifadelerin türü referans olamaz.

int* p{};       // "p" burada ifade oluşturmuyor: tür "int*".
p;              // "p" burada ifade: L-Value, tür "int*".
                // İfadelerin türü referans olamaz ama gösterici olabilir.
```

`int&& rr` bildirimindeki `rr`'nin bir ifade olarak L-Value olması, ilk bakışta
çelişkili görünür. Çelişki değildir: `rr` bir isimdir, isimlerin bellekte yeri vardır,
dolayısıyla kimliği vardır. Bu, `T&&` parametreli işlevlerin gövdesinde
`std::move` çağırmak zorunda kalmanızın sebebidir.
