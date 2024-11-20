import numpy as np
import matplotlib.pyplot as plt


g = 9.81  
L = 10.0  
theta0 = np.pi / 4  
omega0 = 0.0  
tmax = 10  
dt = 0.01  


def angular_acceleration(theta):
    return -g / L * np.sin(theta)


def euler_method(theta0, omega0, tmax, dt):
    num_steps = int(tmax / dt)
    theta = np.zeros(num_steps)
    omega = np.zeros(num_steps)
    time = np.zeros(num_steps)
    theta[0] = theta0
    omega[0] = omega0

    for i in range(1, num_steps):
        alpha = angular_acceleration(theta[i - 1])
        omega[i] = omega[i - 1] + alpha * dt
        theta[i] = theta[i - 1] + omega[i] * dt
        time[i] = time[i - 1] + dt

    return theta, time

# Simulação
theta, time = euler_method(theta0, omega0, tmax, dt)

# Plotagem
plt.plot(time, theta)
plt.title('Pêndulo de Foucault')
plt.xlabel('Tempo (s)')
plt.ylabel('Ângulo (radianos)')
plt.grid(True)
plt.show()
