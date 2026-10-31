---
cilt: "I — Temel"
kisim: "15 — Dinamik Ömürlü Nesneler"
baslik: "15.1 Dört ömür kategorisi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++20)"
---

## 15.1 Dört ömür kategorisi

| Kategori | Ne zaman hayata gelir | Ne zaman biter |
|---|---|---|
| Otomatik | Bildirim noktasında | Kapsam bittiğinde |
| Statik | Program başında veya ilk kullanımda | Program sonunda |
| Dinamik | Programcı istediğinde | Programcı istediğinde |
| İş parçacığına özel | İş parçacığı başlarken | İş parçacığı biterken |

Dinamik ömür, hayatın başlangıcı ve sonu **tamamen programcıya bırakılan** kategoridir.
Nesnenin ne kadar yaşayacağı derleme zamanında belli değilse bu kategoriye ihtiyaç
duyarsınız.
