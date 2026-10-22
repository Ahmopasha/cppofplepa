# CLAUDE.md

Bu depoda çalışan yapay zekâ oturumları için kurallar. Kitabın bakım ve yazım kuralları
`BAKIM.md`'de; önce onu okuyun. Burada yalnızca yapay zekâya özgü ek kurallar var.

## Doğruluk

- **Kanıtsız iddia yok.** Dil ve kütüphane hakkındaki her normatif iddia ("tanımsız
  davranıştır", "sentaks hatasıdır", "C++17'den beri") birincil kaynaktan doğrulanır:
  standart metni (eel.is/c++draft ya da ilgili standart sürümü), önergeler (wg21.link),
  cppreference. Bellekten yazılmaz; doğrulanamayan iddia metne girmez.
- **Her normatif iddiaya bir test kodu.** İddiayı sınayan kısa kod yazılır ve kod
  denetiminden geçer (`araclar/kod_denetimi.py`). Derlenmeyen kod "derlendi" diye
  yazılmaz; derleme yapılmadıysa yapılmadığı söylenir.
- **Standart esastır.** Kitap derleyici davranışını değil C++ standardını anlatır.
  Derleyici adı, sürümü ya da derleyiciye özgü davranış metne girmez. Standart bir
  davranışı gerçeklemeye bağlı bıraktığında bu açıkça söylenir.
- **Standart ufku.** Cilt I C++20, Cilt II C++23. C++26 değişiklikleri kitaba işlenmez
  (istisna: eski kiplere de uygulanan kusur raporları; bkz. BAKIM.md).

## Değişiklik akışı

- Esaslı her metin değişikliği AI hakem panelinden (`~/ai-panel`, `cpp-kitap` ölçütü)
  geçer; kapı kararlarını kullanıcı verir. Yalnızca tarih alanı, tablo satırı, yazım
  hatası ve terim sözlüğüne uyum gibi önemsiz değişiklikler panele gitmez.
- Hakemlerin internet erişimi yoktur: kaynak alıntıları ve derleme sonuçları brief'e
  konur.
- Metni yazan oturum, aynı metnin bağımsız gözden geçirmesini yapmaz.
- Commit'ten önce: `python3 araclar/derle.py --kati --kod` uyarısız ve sorunlu bloksuz
  bitmeli; `son_kontrol` alanları ve `DEGISIKLIKLER.md` güncellenmeli.
- Kullanıcı push'u kendisi yapar (GitHub Desktop); kimlik bilgisi girilmez.

## Biçim

- Kod yorumu satıra sığıyorsa satır sonunda `//` ile; sığmıyorsa kodun hemen üstünde
  `/*`, `* ...`, `*/` bloğu olarak yazılır.
- Kod denetiminin işaretleri (`<!-- kod: ... -->`, `<!-- kod-baglam ... -->`) okura
  görünmez; kullanımları BAKIM.md, "Kod örnekleri" bölümünde.
- Terimler `terim_sozlugu.md`'ye uyar; 6. bölümdeki karşılıklar kullanılmaz.
