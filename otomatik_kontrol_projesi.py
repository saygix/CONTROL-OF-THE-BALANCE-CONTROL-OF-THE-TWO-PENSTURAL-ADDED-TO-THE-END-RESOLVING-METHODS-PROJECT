import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Sistem parametreleri
m1 = 1 # Birinci sarkacın kütlesi (kg)
m2 = 1  # İkinci sarkacın kütlesi (kg)
l1 = 1  # Birinci sarkacın uzunluğu (m)
l2 = 1  # İkinci sarkacın uzunluğu (m)
g = 9.81  # Yerçekimi ivemesi (m/s^2)

# PID denetleyici parametreleri
Kp = 100 # Oransal kazanç
Ki = 20  # İntegral kazanç
Kd = 10  # Türev kazancı
dt =0.1 # Örnekleme zamanı

# Başlangıç ​​koşulları
theta1 = np.pi/4 # Birinci sarkacın ilk açısı (rad)
theta2 = np.pi/4  # İkinci sarkacın ilk açısı (rad)
theta1_dot = 0  # Birinci sarkacın ilk açısal hızı (rad/s)
theta2_dot = 0  # İkinci sarkacın ilk açısal hızı (rad/s)

# Ayar noktası (istenen açı)
setpoint = np.array([0, 0])

# Değişkenleri başlat
theta1_history = [theta1]
theta2_history = [theta2]
u_history = []
error_history = [setpoint - np.array([theta1, theta2])]
integral_error = np.zeros(2)

# Kontrol fonksiyonu
def control(setpoint, theta1, theta2, theta1_dot, theta2_dot, integral_error):
    # Hatayı hesapla
    error = setpoint - np.array([theta1, theta2])
    integral_error += error * dt

    # Kontrol girişini hesapla
    u = Kp * error + Ki * integral_error + Kd * np.array([theta1_dot, theta2_dot])

    return u, integral_error

# Animasyon fonksiyonu
def animate(i):
    global theta1, theta2, theta1_dot, theta2_dot, theta1_history, theta2_history, u_history, error_history, integral_error

    # Kontrol fonksiyonunu çağır ve kontrol girişini al
    u, integral_error = control(setpoint, theta1, theta2, theta1_dot, theta2_dot, integral_error)

    # Kontrol girişini sisteme
    num1 = -g * (2 * m1 + m2) * np.sin(theta1) - m2 * g * np.sin(theta1 - 2 * theta2) - 2 * np.sin(theta1 - theta2) * m2 * (theta2_dot ** 2 * l2 + theta1_dot ** 2 * l1 * np.cos(theta1 - theta2))
    den1 = l1 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))
    num2 = 2 * np.sin(theta1 - theta2) * (theta1_dot ** 2 * l1 * (m1 + m2) + g * (m1 + m2) * np.cos(theta1) + theta2_dot ** 2 * l2 * m2 * np.cos(theta1 - theta2))
    den2 = l2 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))
    theta1_ddot = num1 / den1
    theta2_ddot = num2 / den2
    # Açısal hızları ve açıları güncelle
    theta1_dot += theta1_ddot * dt
    theta2_dot += theta2_ddot * dt
    theta1 += theta1_dot * dt
    theta2 += theta2_dot * dt
    # Açıları kaydet
    theta1_history.append(theta1)
    theta2_history.append(theta2)
    # Kontrol girişini kaydet
    u_history.append(u)
    # Hata kaydını güncelle
    error_history.append(setpoint - np.array([theta1, theta2]))
    # Sarkaçların x ve y koordinatlarını hesapla
    x1 = l1 * np.sin(theta1)
    y1 = -l1 * np.cos(theta1)
    x2 = x1 + l2 * np.sin(theta2)
    y2 = y1 - l2 * np.cos(theta2)
    # Grafikleri çiz
    plt.clf()
    plt.plot([0, x1, x2], [0, y1, y2], 'o-', lw=2)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.title(f'Time: {i*dt:.2f}s')

ani = FuncAnimation(plt.gcf(), animate, frames=range(200), interval=20)
ani.save('animation.gif', writer='pillow')
plt.show()

