---
cilt: "I — Temel"
kisim: "15 — Dinamik Ömürlü Nesneler"
baslik: "15.1 Dört ömür kategorisi"
kaynak: "ders notları"
son_kontrol: "2026-11 (C++20)"
---

## 15.1 Dört ömür kategorisi

Her nesnenin bir **ömür kategorisi** *(storage duration)* vardır: nesnenin bulunduğu
belleğin ne zaman ayrılıp ne zaman geri verileceğini bu belirler. Otomatik ve statik
ömürlü değişkenleri Kısım 3.2'de görmüştük. Dört kategori vardır.

| Kategori | Ne zaman hayata gelir | Ne zaman biter |
|---|---|---|
| Otomatik | Akış bildirime her geldiğinde | Kapsam bittiğinde |
| Statik | `main`'in ilk deyiminden önce (ertelenmesi gerçeklemeye bağlı); blok içindeyse akış bildirime ilk geldiğinde | Program sonunda |
| Dinamik | Programcı istediğinde | Programcı istediğinde |
| İş parçacığına özel (`thread_local`) | İş parçacığı başlarken (ertelenmesi gerçeklemeye bağlı); blok içindeyse her iş parçacığında akış bildirime ilk geldiğinde | İş parçacığı biterken |

Statik ömürlü nesnelerin iki aşamada ilk değer alması ve blok dışındakilerde ilk değer
vermenin ertelenebilmesi Cilt II, Kısım 17.5'tedir. İş parçacıklarını Kısım 27'de
göreceğiz.

Dinamik ömür, hayatın başlangıcı ve sonu **tamamen programcıya bırakılan** kategoridir.
Nesnenin ömrü bir kapsama bağlı kalamıyorsa ya da kaç nesneye ihtiyaç duyacağınız ancak
çalışma zamanında belli oluyorsa bu kategoriye ihtiyaç duyarsınız.
