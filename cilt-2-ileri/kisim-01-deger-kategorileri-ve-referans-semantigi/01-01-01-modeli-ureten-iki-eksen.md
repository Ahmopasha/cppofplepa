---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.1.1 Modeli üreten iki eksen"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

### 1.1.1 Modeli üreten iki eksen

Cilt I'de üç kategori operasyonel olarak sıralanmıştı. Bu üçlü keyfi değildir; iki
ikili sorunun kesişiminden doğar:

- İfadenin bir **kimliği** var mı? Bellekte bir yere karşılık geliyor mu, yani `&`
  operatörünün operandı olabiliyor mu? Bir isimle temsil edilmesi şart değildir.
- İfadenin **kaynakları devralınabilir** mi?

|  | Kimliği var | Kimliği yok |
|---|---|---|
| **Kaynağı devralınabilir** | X-Value | PR-Value |
| **Kaynağı devralınamaz** | L-Value | *(tanımsız)* |

Dördüncü göze karşılık gelen bir kategori yoktur. Kimliği de olmayan, kaynağı da
devralınamayan bir ifade dilde tanımlanmamıştır.

Cilt I'de "R-Value" diye tek kalemde geçen şey aslında bu tablonun **üst satırıdır**:

- **R-Value** = PR-Value ∪ X-Value — kaynağı devralınabilenler
- **GL-Value** = L-Value ∪ X-Value — kimliği olanlar

Bunlara **bileşik** kategoriler denir; ilk üçü ise **birincil** kategorilerdir. Bir
ifade her an birincil kategorilerden tam olarak birine aittir.

X-Value her iki bileşiğe de dahildir. Modelin gerilim noktası orasıdır ve taşıma
semantiğinin tamamı o gözün üzerine kurulur.

Cilt I'deki "geçici olan" tarifi, PR-Value'nun kaba karşılığıydı. Kesin tarif
tablodaki gibidir.
