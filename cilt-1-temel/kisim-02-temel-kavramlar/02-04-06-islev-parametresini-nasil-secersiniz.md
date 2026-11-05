---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.4.6 İşlev parametresini nasıl seçersiniz"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

### 2.4.6 İşlev parametresini nasıl seçersiniz

Yukarıdaki tablonun doğrudan sonucu, günlük olarak vereceğiniz bir karardır.

**Okumak için alıyorsanız `const T&` kullanın.** Her şeyi bağlar, kopyalama maliyeti
yoktur, çağıran koda kısıtlama getirmez.

```cpp
void yazdir(const std::string& s);   // hem değişkenle hem geçici yazıyla çağrılabilir
```

**Değiştirmek için alıyorsanız `T&` kullanın.** Çağıran kod bir değişken vermek
zorunda kalır, ki zaten istenen budur.

```cpp
void buyut(std::string& s);
```

**Kaynağını devralacaksanız `T&&` kullanın.** Bu, "bu nesneyi bana bırak, artık senin
değil" demenin dildeki karşılığıdır.

Kopyalanması pahalı bir sınıf türünü değerle geçmek, argüman bir L-Value ise kopyalama
maliyeti getirir. Yerleşik türlerde (`int`, `double`, gösterici) salt okunacak bir
parametreyi değerle geçmek doğru tercihtir; `const` referans kullanmanın genellikle bir
kazancı yoktur.
