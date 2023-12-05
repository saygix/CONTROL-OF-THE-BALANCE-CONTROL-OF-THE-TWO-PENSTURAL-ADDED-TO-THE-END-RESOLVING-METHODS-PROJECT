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
