# -*- coding: utf-8 -*-
#ders 6: kütüphanelerin yüklenmesi
#kütüphaneler
import pandas as pd #veriler için
import numpy as np #hesaplamalar için
import matplotlib.pyplot as plt #grafikler için

#kod bölümü
#veri yükleme

veriler = pd.read_csv('veriler.csv') #çift tırnak " " da olabilir.bu komut bilgiyi yükleyecek.
print(veriler)
#veri ön işleme
boy = veriler[['boy']]
print(boy)

boyKilo = veriler[['boy','kilo']]
print(boyKilo)