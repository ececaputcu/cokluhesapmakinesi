# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    def print_hi(name):
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    from abc import ABC, abstractmethod
    import math

    class Makine(ABC):

        @abstractmethod  # metodu soyut metod ol.işaretlemek için
        def hesapla(self):  # hesapla temel soyut sınıf ABCden miras
            pass

    class Hafiza:

        def __init__(self):
            self.toplam = 0

        def ekle(self, deger):
            self.toplam += deger

        def cikar(self, deger):
            self.toplam -= deger

        def sifirla(self):
            self.toplam = 0

        def get_toplam(self):
            return self.toplam

    class Toplama(Makine):

        def __init__(self, *sayilar):
            self.sayilar = sayilar

        def hesapla(self):
            hesap = sum(self.sayilar)
            print("Toplama işlemi sonucu:", hesap)
            return hesap

    class Cikarma(Makine):

        def __init__(self, *sayilar):
            self.sayilar = sayilar

        def hesapla(self):
            hesap = self.sayilar[0] - sum(self.sayilar[1:])
            print("Çıkarma işlemi sonucu:", hesap)
            return hesap

    class Bolme(Makine):

        def __init__(self, *sayilar):
            self.sayilar = sayilar

        def hesapla(self):
            if 0 in self.sayilar[1:]:
                print("Sıfıra bölme hatası")
                return None
            else:
                hesap = self.sayilar[0] / math.prod(self.sayilar[1:])
                print("Bölme işlemi sonucu:", hesap)
                return hesap

    class Carpma(Makine):

        def __init__(self, *sayilar):
            self.sayilar = sayilar

        def hesapla(self):
            hesap = math.prod(self.sayilar)
            print("Çarpma işlemi sonucu:", hesap)
            return hesap

    class Karekok(Makine):

        def __init__(self, sayi):
            self.sayi = sayi

        def hesapla(self):
            if self.sayi < 0:
                print("geçersiz giriş, negatif sayıların karekökü alınmaz.")
                return None
            else:
                hesap = math.sqrt(self.sayi)
                print("Karekök alma işlemi sonucu:", hesap)
                return hesap

    class KokAlma(Makine):

        def __init__(self, sayi, kok):
            self.sayi = sayi
            self.kok = kok

        def hesapla(self):
            if self.sayi < 0 or self.kok <= 0:
                print("geçersiz giriş, negatif sayıların veya sıfırın kökü alınmaz.")
                return None
            else:
                hesap = self.sayi ** (1 / self.kok)
                print(f"{self.kok}. kök alma işlemi sonucu:", hesap)
                return hesap

    class YuzdeHesaplama(Makine):

        def __init__(self, sayi, yuzde):
            self.sayi = sayi
            self.yuzde = yuzde

        def hesapla(self):
            hesap = (self.sayi * self.yuzde) / 100
            print(f"{self.sayi} sayısının {self.yuzde}% yüzdesi:", hesap)
            return hesap

    hafiza = Hafiza()

    while True:  # kullanıcı çıkış yapana kadar çalışması için
        print("---------------------------------")
        print("Yapmak istediğin işlemi seçin:")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Bölme")
        print("4. Çarpma")
        print("5. Karekök alma")
        print("6. Kök alma")
        print("7. Yüzde alma")
        print("8. Grand Total")
        print("9. Hesap makinesini sıfırla")
        print("10. Çıkış")

        secim = input("Seçiminizi yapın (1,2,3,4,5,6,7,8,9,10): ")

        if secim == '10':
            print("Çıkılıyor...")
            break

        if secim == '8':
            print("Grand Total:", hafiza.get_toplam())
            continue

        if secim == '9':
            hafiza.sifirla()
            print("Hesap Makinesi Sıfırlandı...")
            continue

        sayilar = [float(x) for x in input("Sayıları aralarında boşluk bırakarak girin: ").split()]

        if secim == '1':
            hesap = Toplama(*sayilar)
        elif secim == '2':
            hesap = Cikarma(*sayilar)
        elif secim == '3':
            hesap = Bolme(*sayilar)
        elif secim == '4':
            hesap = Carpma(*sayilar)
        elif secim == '5':
            hesap = Karekok(sayilar[0])
        elif secim == '6':
            kok = int(input("Kaçıncı kökünü almak istediğinizi girin: "))
            hesap = KokAlma(sayilar[0], kok)
        elif secim == '7':
            yuzde = float(input("Yüzde hesaplamak istediğiniz değeri girin: "))
            hesap = YuzdeHesaplama(sayilar[0], yuzde)
        else:
            print("Geçersiz seçenek")
            continue  # hata mesajıyla döngü tekrar başlayacak

        sonuc = hesap.hesapla()
        if sonuc is not None:
            hafiza.ekle(sonuc)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
