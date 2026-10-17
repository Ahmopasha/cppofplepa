// Kod denetiminin genel bağlamı (araclar/kod_denetimi.py kullanır).
//
// Kitabın örnekleri bazı adları tanıtmadan kullanır: "Myclass bir sınıf olsun",
// "v bir vector olsun" gibi. Bir blok kendi dosyasındaki bağlamla da derlenmezse ve
// derleyici bu adlardan birini bulamadığını söylerse, yalnızca bulunamayan adların
// tanımları bloğun önüne eklenir.
//
// Biçim:
//   //@ Ad [: Bagimlilik ...]    tür ya da işlev; ad alanı düzeyine konur
//   //@@ ad [: Bagimlilik ...]   değişken; blok bir işlev gövdesindeyse gövdenin başına konur
// Tanımlar örneklerin beklediğinden fazlasını sunmamalıdır: bir ad buradaki tanımla
// derleniyorsa, kitaptaki örnek de o kadarını varsayıyor demektir.

//@ Myclass
struct Myclass {
    Myclass();
    Myclass(int);
    Myclass(int, int);
    void func();
};

//@ Kesir
struct Kesir {
    int pay, payda;
    Kesir(int p = 0, int q = 1);
};
Kesir operator+(const Kesir&, const Kesir&);
std::ostream& operator<<(std::ostream&, const Kesir&);

//@ Base
struct Base {
    virtual ~Base();
};

//@ Der : Base
struct Der : Base { };

//@ Sekil
struct Sekil {
    virtual ~Sekil();
    virtual void ciz() const;
};

//@ Daire : Sekil
struct Daire : Sekil {
    void ciz() const override;
    void yaricap_ayarla(double);
};

//@ listeden_al : Sekil
Sekil* listeden_al();

//@ Arac
struct Arac { };

//@@ v
std::vector<int> v{3, 1, 4, 1, 5};

//@@ v1
std::vector<int> v1{3, 1, 4};

//@@ v2
std::vector<int> v2{1, 5, 9};

//@@ s
std::string s{"merhaba dunya"};

//@@ x
int x = 10;

//@ Renk
enum class Renk { Kirmizi, Yesil, Mavi };

//@ g
void g();
