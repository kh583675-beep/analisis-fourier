import numpy as np
import matplotlib.pyplot as plt

# Parámetros
N = 128
t = np.linspace(0, 1, N, endpoint=False)

# 1. Señales PURAS (para las gráficas)
pulso = np.zeros(N)
pulso[N//2-10:N//2+10] = 1  # Pulso rectangular

escalon = np.zeros(N)
escalon[N//2:] = 1  # Escalón

senoide = np.sin(2*np.pi*5*t)  # SENOIDE PURA DE 5 Hz

# Función para graficar
def graficar(x, titulo):
    X = np.fft.fft(x)
    mag = np.abs(X)/N
    fase = np.angle(X)
    
    plt.figure()
    plt.subplot(3,1,1)
    plt.plot(t, x)
    plt.title(f'{titulo} - Tiempo')
    plt.grid(True)
    
    plt.subplot(3,1,2)
    plt.stem(np.arange(N), mag, basefmt=" ")
    plt.title('Magnitud FFT')
    plt.xlim(0, 100)
    
    plt.subplot(3,1,3)
    plt.stem(np.arange(N), fase, basefmt=" ")
    plt.title('Fase FFT')
    plt.xlim(0, 100)
    
    plt.tight_layout()
    plt.show()

# Graficar las 3
graficar(pulso, "Pulso Rectangular")
graficar(escalon, "Escalon")
graficar(senoide, "Senoidal 5 Hz")

# 2. Prueba de linealidad (aparte, no afecta la gráfica de arriba)
print("Prueba linealidad:")
combinada = 2*pulso + 0.5*senoide
X_comb = np.fft.fft(combinada)
X_sum = 2*np.fft.fft(pulso) + 0.5*np.fft.fft(senoide)
error = np.max(np.abs(X_comb - X_sum))
print(f"Error max = {error} -> Linealidad OK: {error < 1e-10}")
