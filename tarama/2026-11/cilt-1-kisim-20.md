# Tarama — Cilt I Kısım 20 (Kasım 2026)

Kısım 20'deki normatif iddialar. "Sonuç" sütunu: **doğru**, **düzeltilmeli** (standarda
aykırı), **eksik** (doğru ama standardın söylediğinden dar ya da geniş), **gerçekleme**
(standardın söylemediği bir gerçekleme ayrıntısı standart gibi yazılmış), **biçim** (terim
tanıtımı, atıf). Kaynaklar C++20 (N4861) bölüm adlarıyla. 20.0 normatif iddia içermiyor;
20.3 ve 20.4'teki iddialar doğru.

**İşlem (2026-11):** "düzeltilmeli", "eksik", "gerçekleme" ve "biçim" sonuçlu bütün iddialar
düzeltildi; metinler AI hakem panelinden geçti (`~/ai-panel/calismalar/2026-11-18_c1-20-tarama`,
üç hakem, üç hakem turu; tur 3 kararı kabul; Claude hakemi xhigh). Panel ayrıca şunları
düzeltti: Rule of Zero cümlesinin kaynak yönetimini devretmeye bağlanması, `c_str()`
göstericisinde kesin (ömür sonu) ve olası (değiştiren işlevler, `std::getline`) geçersizleşmenin
ayrılması, SSO cümlesinin standardın belirlemediği şeyle sınırlanması, terim tanıtımı.

| # | Yer | İddia | Kaynak | Sonuç |
|---|---|---|---|---|
| 1 | 20.1 | `std::string` belleğini kendi yönetir, RAII uygular | — | doğru |
| 2 | 20.1 | `std::string` "Rule of Zero'ya uyar" | Kısım 13.9'a göre Rule of Zero'ya uyan, kaynağı `std::string` gibi bir sınıfa bırakan kullanıcı sınıfıdır; `std::string`'in kendisi belleği yönettiği için kopyalama, taşıma ve sonlandırma işlevlerini kendisi tanımlar | düzeltilmeli |
| 3 | 20.2 | Kurucular; `size()` ile `length()` aynı | [string.cons], [string.capacity]/1 | doğru |
| 4 | 20.2 | `[]` denetimsiz, "geçersiz indis tanımsız davranış"; `at` `std::out_of_range` gönderir | [string.access]/1–2: önkoşul `pos <= size()`; `s[s.size()]` geçerlidir ve boş karakteri verir (test). /5: `at` `pos >= size()` ise hata gönderir. "Geçersiz indis" sınırı söylenmiyor | eksik |
| 5 | 20.3 | Bulamazsa `std::string::npos`; `npos` `size_type`'ın en büyük değeri, işaretsiz | [basic.string]: `npos = -1` (`size_type`'a dönüşür); test | doğru |
| 6 | 20.3 | `int i = s.find(...)` yanlış, `npos` `int`'e sığmaz | [conv.integral]/3 (C++20: değer modüler dönüşür). Öğüt doğru | doğru |
| 7 | 20.4 | `substr` dışındakiler nesneyi değiştirir | [string.modifiers], [string.substr] | doğru |
| 8 | 20.5 | `c_str()` sonunda boş karakter bulunan `const char*` döndürür | [string.accessors]/1, [basic.string]/3 | doğru |
| 9 | 20.5 | "Nesne değiştirildiğinde veya hayatı bittiğinde gösterici geçersiz olur" | [string.require]/4: `const` olmayan üye işlevlerin çağrılması geçersiz kılabilir (`operator[]`, `at`, `data`, `front`, `back`, `begin`, `end` … hariç). `s[0] = 'x'` nesneyi değiştirir ama göstericiyi geçersiz kılmaz; kural "olur" değil "olabilir" | eksik |
| 10 | 20.5 | `std::stoi`, `std::stod`, `std::to_string` | [string.conversions] | doğru |
| 11 | 20.6 | SSO "gerçeklemelerin çoğu"; eşik "gerçeklemeye bağlıdır ve tipik olarak 15 civarındadır" | Standart SSO'dan hiç söz etmez. Kitapta "gerçeklemeye bağlı" standart seçeneği ve belgelenen davranıştır (Kısım 2.5); eşik böyle bir seçenek değil. "Tipik olarak 15" belirli gerçeklemelerin değeri | gerçekleme |
| 12 | 20.6 | "Bu, `std::string`'i … `const` referansla almanın yeterli olduğunu söyler" | Çıkarım SSO'dan gelmiyor: `const` referansla almak kopyalamayı zaten önler, SSO yalnızca kopyalamanın maliyetini etkiler. Atıf Cilt II 11 → 11.2 | eksik; biçim (atıf) |

Testler (Apple clang 21, `-std=c++20 -pedantic-errors`): bölümdeki kod örnekleri geçerli;
`npos == size_type(-1)`, `size_type` işaretsiz; `s[s.size()] == '\0'`, boş string'de
`e[0] == '\0'`; `s.at(3)` (3 karakterlik `s`) `std::out_of_range` gönderiyor; bulunmayan
aramada `int i = s.find(…)` −1 oluyor; `s.substr(1, 5)` kalan karakterleri veriyor.
