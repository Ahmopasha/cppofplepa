---
cilt: "II — İleri"
kisim: "1 — Değer Kategorileri ve Referans Semantiği"
baslik: "1.2.2 Referans çökmesi"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

### 1.2.2 Referans çökmesi

Kendi elinizle referansa referans yazamazsınız; `int& &` sentaks hatasıdır. Ama tür
çıkarımı, `typedef` ve `decltype` yoluyla dolaylı olarak ortaya çıkabilir. Bu durumda
diller **referans çökmesi** *(reference collapsing)* kuralını uygular:

| Ortaya çıkan | Çöker |
|---|---|
| `T&  &` | `T&` |
| `T&  &&` | `T&` |
| `T&& &` | `T&` |
| `T&& &&` | `T&&` |

Tek cümlelik kuralı şudur: **ikisinden biri sol taraf referansıysa sonuç sol taraf
referansıdır.** Yalnızca ikisi de sağ taraf referansıysa sonuç sağ taraf referansı olur.

Forwarding reference'ın çalışma biçimi tamamen bu kurala dayanır.
