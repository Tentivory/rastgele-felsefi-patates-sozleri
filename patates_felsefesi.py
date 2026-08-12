#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Felsefi Patates Sözleri Üreteci
=======================================
Bu yazılım, insanlığın en büyük felsefi sorunlarını çözmek için
binlerce yıllık patates bilgeliğini modern bilgisayar bilimiyle
birleştirerek geliştirilmiştir.

Uyarı: Bu programı çalıştırmadan önce lütfen derin bir nefes alın
ve hayatınızın anlamını sorgulamaya hazır olun.
"""

import random
import time
import sys

# Bilimsel olarak onaylanmış (aslında onaylanmamış) patates bilgeliği veritabanı
PATATES_SOZLERI = [
    "Varoluşun anlamı, toprağın altında sessizce büyüyen bir patatesin sabrında gizlidir.",
    "Eğer hayat seni kızartıyorsa, unutma: en lezzetli patatesler en çok ateşi görenlerdir.",
    "Ben düşündükçe varım... ama patates olduğum için aslında sadece nişasta ve suyun birleşimiyim.",
    "Gerçek özgürlük, soyulmayı kabul edip yine de lezzetli kalabilmektir.",
    "Zaman bir yanılsamadır. Patates ise ebedi bir gerçektir.",
    "Hiçbir şey bilmediğini bilmek, Sokrates'in en büyük bilgeliğidir. Ben ise sadece bir patatesim ve bunu biliyorum.",
    "Aşk, iki patatesin aynı tencerede haşlanmasıdır. Ayrılık ise birinin kızartılmasıdır.",
    "Evren genişliyor. Ben ise küçülüyorum. Bu bir paradoks değil, sadece diyet yapıyorum.",
    "Ölüm korkulacak bir şey değildir. Asıl korkulacak şey, çiğ çiğ yenmektir.",
    "Mutluluk, bir tabak sıcak patates püresinin dumanında saklıdır.",
    "Felsefe yapmak, patatesi soyup içindeki boşluğu görmektir.",
    "Ben bir patatesim, dolayısıyla düşünüyorum. Düşünüyorum, dolayısıyla varım. Varım, dolayısıyla kızartılabilirim.",
    "Hayat kısa, patates uzun. Onun için acele etme, yavaş yavaş piş.",
    "Gerçek bilgelik, toprağın altından gelendir. Kitapların üstünden değil.",
    "Eğer bir gün kendini kaybedersen, unutma: her patates bir gün filizlenir.",
]

def yavas_yaz(metin, gecikme=0.04):
    """Dramatik etki için metni yavaş yavaş yazdır."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def ana_menu():
    print("\n" + "="*60)
    print("  🥔  RASTGELE FELSEFİ PATATES SÖZLERİ ÜRETECİ  🥔")
    print("="*60)
    print("\nEvrenin en derin sırları, bir patatesin gözünde saklıdır.")
    print("Hazır mısın? (Evet demen gerekmiyor, zaten hazır olduğunu biliyoruz)\n")

def uret():
    soz = random.choice(PATATES_SOZLERI)
    print("\n" + "-"*60)
    yavas_yaz(f"🥔 Bilgelik: {soz}")
    print("-"*60 + "\n")

def main():
    ana_menu()
    while True:
        try:
            girdi = input("Yeni bir patates bilgeliği almak için Enter'a bas (çıkmak için 'q'): ").strip().lower()
            if girdi == 'q':
                yavas_yaz("\nPatates seni unutmayacak... Sen de onu unutma. Güle güle.")
                break
            uret()
        except KeyboardInterrupt:
            print("\n\nProgram zorla kapatıldı. Patatesler üzüldü.")
            break

if __name__ == "__main__":
    main()
