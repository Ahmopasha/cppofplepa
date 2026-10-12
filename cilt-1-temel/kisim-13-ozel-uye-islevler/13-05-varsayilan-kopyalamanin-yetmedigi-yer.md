---
cilt: "I — Temel"
kisim: "13 — Özel Üye İşlevler"
baslik: "13.5 Varsayılan kopyalamanın yetmediği yer"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 13.5 Varsayılan kopyalamanın yetmediği yer

Sınıfınız bir **kaynak** yönetiyorsa, yani veri elemanları arasında dinamik bellek
adresi, dosya tanıtıcısı, soket gibi bir şey varsa, üye üye kopyalama yanlış sonuç verir.

```cpp
class Yazi {
    char* p;
public:
    Yazi(const char* s) : p{ new char[std::strlen(s) + 1] } { std::strcpy(p, s); }
    ~Yazi() { delete[] p; }
};
```

Derleyicinin yazdığı kopyalayan kurucu işlev `p` göstericisini kopyalar. Sonuçta **iki
nesne aynı belleği gösterir.** İkisinin de sonlandırıcı işlevi çalışınca aynı bellek iki
kez serbest bırakılır ve program tanımsız davranışa girer.

Buna **sığ kopyalama** *(shallow copy)* denir. İstenen ise **derin kopyalamadır**
*(deep copy)*: kaynağın kendisinin de kopyalanması.

```cpp
Yazi(const Yazi& other) : p{ new char[std::strlen(other.p) + 1] }
{
    std::strcpy(p, other.p);
}
```
