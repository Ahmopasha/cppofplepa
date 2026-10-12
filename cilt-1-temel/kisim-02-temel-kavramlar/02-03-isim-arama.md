---
cilt: "I — Temel"
kisim: "2 — Temel Kavramlar"
baslik: "2.3 İsim arama"
kaynak: "ders notları"
son_kontrol: "2026-09 (C++23)"
---

## 2.3 İsim arama

Derleyici bir isim gördüğünde onu bir varlıkla eşleştirmek zorundadır. Bu işleme **isim
arama** *(name lookup)* denir.

Kuralın tek cümlelik hâli şudur: **arama, ismin bulunduğu ilk kapsamda durur.** Bulunan
ismin işe yarayıp yaramadığına bakılmaz; arama orada biter.

```cpp
void func(int);

int main()
{
    void func(double);   // yerel bildirim, dıştakini gölgeler

    func(12);            // func(double) çağrılır, func(int) değil
}
```

Bu davranış ilk bakışta hatalı görünür ama kasıtlıdır. İsim arama, işlev yükleme
çözümlemesinden **önce** ve ondan bağımsız yapılır. Sıra şudur:

1. **İsim arama** — ismin hangi kapsamda olduğu bulunur
2. **Yükleme çözümlemesi** — o kapsamdaki adaylar arasından uygun olan seçilir
3. **Erişim kontrolü** — seçilen adaya erişim hakkı var mı diye bakılır

Üçünün bu sırada ve birbirinden bağımsız işlemesi, C++'ta şaşırtıcı görünen birçok
durumun tek açıklamasıdır. Sınıflarda ve kalıtımda tekrar karşınıza çıkacak
(Kısım 12 ve 17).
