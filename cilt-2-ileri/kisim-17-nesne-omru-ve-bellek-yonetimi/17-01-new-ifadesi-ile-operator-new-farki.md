---
cilt: "II — İleri"
kisim: "17 — Nesne Ömrü ve Bellek Yönetimi"
baslik: "17.1 `new` ifadesi ile `operator new` farkı"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 17.1 `new` ifadesi ile `operator new` farkı

Cilt I Kısım 15.2'de `new` ifadesinin iki iş yaptığı söylenmişti: bellek ayırmak ve
nesneyi hayata getirmek. Bu iki işin **ayrı ayrı** özelleştirilebilir olması, bölümün
konusudur.

| Yazım | Ne yapar |
|---|---|
| `new T` | *new ifadesi* — bellek ayırır **ve** kurucu işlevi çağırır |
| `operator new` | Yalnızca ham bellek ayırır; kurucu işlev çağırmaz |

`operator new`, imzası `void* operator new(std::size_t)` olan sıradan bir işlevdir.
`new` ifadesi arka planda onu çağırır. `malloc` ile farkı yoktur; C++ tarafından
değiştirilebilir olması dışında.

Aynı şekilde `delete` ifadesi önce sonlandırıcı işlevi çağırır, sonra
`void operator delete(void*)` işlevini çağırır.
