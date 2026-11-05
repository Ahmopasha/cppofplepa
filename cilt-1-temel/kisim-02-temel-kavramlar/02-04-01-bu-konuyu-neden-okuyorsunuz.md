---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.4.1 Bu konuyu neden okuyorsunuz"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

### 2.4.1 Bu konuyu neden okuyorsunuz

Aşağıdaki dört satırın ikisi derlenir, ikisi derlenmez:

```cpp
int x = 10;

int& a = x;           // geçerli
int& b = 10;          // sentaks hatası
const int& c = 10;    // geçerli
int&& d = x;          // sentaks hatası
```

Aradaki farkı açıklayan şeye ifadenin **değer kategorisi** denir. Bu konuyu bilmeden
yazılan kodda, derleyicinin neden şikâyet ettiği anlaşılmaz. İşlev parametrelerini
doğru seçmek de buna bağlıdır.
