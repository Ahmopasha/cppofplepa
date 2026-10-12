---
tur: "kısım geçişi"
cilt: "II — İleri"
onceki: "Kısım 10 — `std::format`"
sonraki: "Kısım 11 — Vocabulary Türleri"
yer: "Kısım 11 başlığının hemen altı, varsa kısım girişinden önce"
kaynak: "derleyen"
son_kontrol: "2026-10 (C++23)"
---

`std::format`, biçimlendirmedeki hataları tür sistemine yakalatıyordu. Bu bölümdeki türler
aynı ilkeyi işlev arayüzlerine uygular: "değer olmayabilir", "şu türlerden biri" ya da
"sahiplenmeden bakılan bir dizi" gibi niyetleri, `-1` veya `nullptr` gibi özel değerlere
başvurmadan türün kendisiyle ifade ederler.
