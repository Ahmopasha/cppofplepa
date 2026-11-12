---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.9 Rule of Zero"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 13.9 Rule of Zero

Big-Five'ın doğru okunuşu "beşini de yaz" değil, **"hiçbirini yazmak zorunda kalmayacak
şekilde tasarla"**dır.

Kaynağı doğrudan tutmak yerine, kaynağı zaten doğru yöneten bir sınıfa devredin:

```cpp
class Yazi {
    std::string s;        // kaynağı std::string yönetiyor
};
```

Bu sınıf için altı işlevin hiçbirini yazmanıza gerek yoktur. Derleyicinin yazdığı hepsi
doğru çalışır, çünkü `std::string`'in kendi işlevleri doğru çalışır.

> **Rule of Zero:** Kaynak yönetimini `std::string`, `std::vector`, `std::unique_ptr`,
> `std::shared_ptr` (Kısım 25) gibi bunun için yazılmış sınıflara bırakın; kopyalama ve
> taşıma işlevlerini ve sonlandırıcı işlevi yazmayın (türemiş sınıf nesneleri taban
> sınıf göstericisiyle siliniyorsa sanal sonlandırıcı için Kısım 17.7).

Pratikte yazdığınız sınıfların ezici çoğunluğu bu kurala uyar. Big-Five'a ihtiyaç
duyduğunuz yer, o kaynak yöneten sınıfların kendisini yazdığınız yerdir.
