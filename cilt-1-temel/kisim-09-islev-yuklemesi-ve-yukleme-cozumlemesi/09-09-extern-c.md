---
cilt: "I — Temel"
kisim: "9 — İşlev Yüklemesi ve Yükleme Çözümlemesi"
baslik: "9.9 `extern \"C\"`"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 9.9 `extern "C"`

Standart, isimlerin bağlayıcıya nasıl aktarılacağını söylemez; bunun yerine dil
bağlantısını (Kısım 1.10) tanımlar. Gerçeklemeler, yüklenmiş işlevleri bağlayıcıda ayırt
edebilmek için C++ işlev isimlerini genellikle imzayla birlikte kodlar; buna *name
mangling* denir. C'de yükleme olmadığı için böyle bir kodlamaya gerek yoktur.

C ile yazılmış bir kütüphanenin işlevleri C++ tarafında C dil bağlantısıyla
bildirilmelidir (Kısım 1.10). Gerçeklemelerde bu, ismin C++ usulü kodlanmamasını, böylece
C tarafında derlenmiş işlevin ismiyle eşleşmesini sağlar. Bunun için bildirimin önüne
`extern "C"` yazılır; `extern "C" { … }` biçimiyle birden fazla işlev birlikte C dil
bağlantısıyla bildirilir:

<!-- kod: atla -->
```cpp
extern "C" void c_islevi(int);

extern "C" {
    void c_ac(int);
    void c_kapat();
}
```

Belli bir isimde C dil bağlantılı en fazla bir işlev olabilir; bu yüzden iki `extern "C"`
işlev birbirini yükleyemez. Aynı isimde C++ dil bağlantılı yüklemeler ise bildirilebilir:
`extern "C" void f(int);` ile `void f(double);` bir arada bulunabilir.
