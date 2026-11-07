---
cilt: "I — Temel"
kisim: "7 — Varsayılan Argümanlar"
baslik: "7.1 Ne işe yarar"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 7.1 Ne işe yarar

Bir parametreye varsayılan değer verirseniz, çağıran kod o argümanı yazmayabilir.

```cpp
void yazdir(const std::string& s, char ayirici = '\n');

yazdir("merhaba");          // ayirici '\n'
yazdir("merhaba", ' ');     // ayirici ' '
```

Aynı işi, işlevi iki kez yükleyerek (Kısım 9.1) de yapabilirdiniz. Varsayılan argüman, tek
bir tanımla aynı sonucu verir.
