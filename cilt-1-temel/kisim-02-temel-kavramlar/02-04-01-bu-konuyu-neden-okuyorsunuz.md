---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.4.1 Bu konuyu neden okuyorsunuz"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

### 2.4.1 Bu konuyu neden okuyorsunuz

Aşağıdaki dört satırın ikisi derlenir, ikisi derlenmez:

```cpp
int x = 10;

int& a = x;           // derlenir
int& b = 10;          // DERLENMEZ
const int& c = 10;    // derlenir
int&& d = x;          // DERLENMEZ
```

Aradaki farkı açıklayan şeye ifadenin **değer kategorisi** denir. Bu konuyu bilmeden
yazılan kodda, derleyicinin neden şikâyet ettiği anlaşılmaz. İşlev parametrelerini
doğru seçmek de buna bağlıdır.
