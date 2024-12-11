def amdahl_hesapla(paralel_oran, islemci_sayisi):
    
    hizlanma = 1 / ((1 - paralel_oran) + (paralel_oran / islemci_sayisi))
    return hizlanma

def amdahl_simulasyonu():
    print("Amdahl Yasasi Hizlanma Hesaplama Programi")
    print("-------------------------------------------------")
    
    # Kullanıcıdan giriş al
    paralel_oran = float(input("Paralellestirilebilir orani giriniz (0 ile 1 arasinda): "))
    if paralel_oran < 0 or paralel_oran > 1:
        print("Hatali giris! Oran 0 ile 1 arasinda olmalidir.")
        return
    
    max_islemci = int(input("Maksimum islemci sayisini giriniz: "))
    if max_islemci < 1:
        print("Hatali giris! Islemci sayisi 1 veya daha büyük olmalidir.")
        return
    
    print("\nHesaplama Sonuclari:")
    print("-------------------------------------------------")
    print(f"Paralellestirilebilir Oran: {paralel_oran:.2f}\n")
    
    # İşlemci sayısına göre hızlanmayı hesapla
    for islemci_sayisi in range(1, max_islemci + 1):
        hizlanma = amdahl_hesapla(paralel_oran, islemci_sayisi)
        print(f"Islemci Sayisi: {islemci_sayisi} -> Hizlanma: {hizlanma:.2f} kat")
    
    print("\nHesaplama Tamamlandi!")

if __name__ == "__main__":
    amdahl_simulasyonu()
