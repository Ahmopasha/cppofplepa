---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.8 Sabitlerin yazımı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 2.8 Sabitlerin yazımı

C++11 ve sonrası, sabitlerin okunabilirliğini artıran birkaç yazım ekledi.

**İkilik sabitler.** `0b` veya `0B` ön ekiyle yazılır. Bit maskeleri ve donanım
kayıtlarında, onaltılık yazımdan daha açıktır.

```cpp
int a = 0b1010;          // 10
int maske = 0b0000'1111;
```

Sekizlik sabitler `0` ön ekiyle, onaltılık sabitler `0x` ile yazılır. Sekizlik yazım bir
tuzaktır: başına sıfır koyduğunuz bir sayı sessizce sekizlik okunur.

```cpp
int x = 010;             // 8, 10 değil
```

**Basamak ayırıcı.** Tek tırnak, sabitin okunabilirliği için araya konabilir ve değeri
etkilemez. Gruplama kuralı yoktur; nereye koyacağınıza siz karar verirsiniz.

```cpp
int   nufus  = 85'000'000;
long  bellek = 4'294'967'296;
int   maske  = 0b1111'0000'1111'0000;
double pi    = 3.141'592'653;
```

**Ham yazı sabitleri.** `R"(...)"` biçiminde yazılır; içindeki ters bölü ve tırnak
karakterleri kaçış dizisi olarak yorumlanmaz. Dosya yolları ve düzenli ifadeler için
kullanılır.

```cpp
const char* yol   = "C:\\Users\\ahmet\\veri.txt";       // kaçış dizileriyle
const char* yol2  = R"(C:\Users\ahmet\veri.txt)";      // ham

const char* desen = R"(\d{3}-\d{4})";
```

Yazının içinde `)"` dizisi geçiyorsa, araya bir ayırıcı konur:

```cpp
const char* s = R"AYIR(burada )" geçiyor)AYIR";
```

Ham yazı sabitleri satır sonlarını da olduğu gibi korur; çok satırlı metin gömmek için
elverişlidir.
