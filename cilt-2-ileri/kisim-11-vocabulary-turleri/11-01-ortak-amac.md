---
cilt: "II — İleri"
kisim: "11 — Vocabulary Türleri"
baslik: "11.1 Ortak amaç"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 11.1 Ortak amaç

Bu bölümdeki türlerin ortak yanı, **arayüzlerde ortak bir kelime dağarcığı**
oluşturmalarıdır. İngilizcede *vocabulary types* denmesinin sebebi budur.

Her proje kendi "isteğe bağlı değer" veya "şu türlerden biri" sınıfını yazarsa, iki
kütüphane bir araya geldiğinde birbirine dönüştürme kodu gerekir. Standart kütüphanenin
bu türleri sunması, arayüzlerin ortak bir dilde konuşmasını sağlar.

İki gruba ayrılırlar. **Görünüm türleri** (`string_view`, `span`) sahiplenmeden gösterir.
**Sarmalayıcı türler** (`optional`, `variant`, `any`) değeri içlerinde tutar.
