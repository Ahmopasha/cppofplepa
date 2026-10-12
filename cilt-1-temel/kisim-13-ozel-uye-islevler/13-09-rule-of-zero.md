---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.9 Rule of Zero"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
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

> **Rule of Zero:** Kaynak yönetimini `std::string`, `std::vector`, `unique_ptr`,
> `shared_ptr` gibi bunun için yazılmış sınıflara bırakın; özel üye işlevlerin hiçbirini
> yazmayın.

Pratikte yazdığınız sınıfların ezici çoğunluğu bu kurala uyar. Big-Five'a ihtiyaç
duyduğunuz yer, o kaynak yöneten sınıfların kendisini yazdığınız yerdir.
