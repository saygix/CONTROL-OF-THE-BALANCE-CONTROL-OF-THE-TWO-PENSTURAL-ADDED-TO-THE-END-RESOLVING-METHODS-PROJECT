# Çift Sarkaç PID Denetleyici Animasyonu

Bu proje, iki bağlantılı sarkacın kontrolünü simüle eden bir Python programını içerir. PID (Proportional-Integral-Derivative) denetleyici kullanılarak sarkaçların hareketi kontrol edilir.

## Sistem Tanımı

Sistem, iki sarkaçtan oluşur, her biri bir çubuk ve bir kütle ile birbirine bağlanır. İlk sarkaç dikey olarak asılırken, ikinci sarkaç, ilk sarkaçtan asılı olan çubuğa bağlanır ve yere dikey değil, yatay bir açıyla yerleştirilir. Bu sistem, açısal hızları, kütleleri, çubuk uzunlukları ve yerçekimi ivmesi gibi parametreleri kullanarak modellenir. PID denetleyicisi, sistemi hedef açılara getirmek için kullanılır.

## Gereksinimler

- Python 3.x
- NumPy
- Matplotlib

Gerekli kütüphaneleri yüklemek için terminal veya komut istemcisine şu komutu yazabilirsiniz:
```bash
pip install numpy
pip install matplotlib
```

## Kullanım

1. 'pendulum_simulation.py' dosyasını çalıştırın.
2. Simülasyon penceresi açılacaktır ve sarkaçlar belirtilen PID kontrol parametreleri ile hareket edecektir.

## Parametreler
Proje içinde, sarkaçların fiziksel özellikleri ve PID denetleyici parametreleri aşağıdaki gibi ayarlanmıştır:
```python
# Sistem parametreleri
m1 = 1  # Birinci sarkacın kütlesi (kg)
m2 = 1  # İkinci sarkacın kütlesi (kg)
l1 = 1  # Birinci sarkacın uzunluğu (m)
l2 = 1  # İkinci sarkacın uzunluğu (m)
g = 9.81  # Yerçekimi ivemesi (m/s^2)

# PID denetleyici parametreleri
Kp = 100  # Oransal kazanç
Ki = 20   # İntegral kazanç
Kd = 10   # Türev kazancı
dt = 0.1  # Örnekleme zamanı
```

Bu parametreleri ihtiyaca göre değiştirebilir ve simülasyonun davranışını gözlemleyebilirsiniz.

## Animasyon

Simülasyon sırasında sarkaçların hareketi animasyon olarak gösterilir ve animation.gif adlı bir dosyaya kaydedilir.

![](https://github.com/saygix/CONTROL-OF-THE-BALANCE-CONTROL-OF-THE-TWO-PENSTURAL-ADDED-TO-THE-END-RESOLVING-METHODS-PROJECT/assets/139467552/f43c703e-71f5-412d-97fb-a377bd674e45)




