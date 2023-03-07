# -*- coding: utf-8 -*-
#ders 6: kütüphanelerin yüklenmesi
#kütüphaneler
import pandas as pd #veriler için
import numpy as np #hesaplamalar için
import matplotlib.pyplot as plt #grafikler için

#kod bölümü
#veri yükleme

veriler = pd.read_csv('eksikveriler.csv') #çift tırnak " " da olabilir.bu komut bilgiyi yükleyecek.
print(veriler)
#veri ön işleme
boy = veriler[['boy']]
print(boy)

boyKilo = veriler[['boy','kilo']]
print(boyKilo)

#eksik veriler
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan, strategy= 'mean')
Yas = veriler.iloc[:,1:4].values
print(Yas)
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)

ulke = veriler.iloc[:,0:1].values #bütün satırlar için.
print(ulke)

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)
ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)

