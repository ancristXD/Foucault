import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constantes
g = 9.81  # Aceleração devido à gravidade (m/s^2)
L = 10.0  # Comprimento do pêndulo (metros)
theta0 = np.pi / 4  # Ângulo inicial (radianos)
omega0 = 0.0  # Velocidade angular inicial (radianos/segundo)
tmax = 10  # Tempo máximo da simulação (segundos)
dt = 0.05  # Passo de tempo (segundos)

# Função para calcular a aceleração angular
def angular_acceleration(theta):
    return -g / L * np.sin(theta)

# Método de Euler para resolver as equações diferenciais
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

# Função para atualizar a animação
def update(frame, line):
    line.set_data([0, L * np.sin(theta[frame])], [0, -L * np.cos(theta[frame])])
    return line,

# Simulação
theta, _ = euler_method(theta0, omega0, tmax, dt)

# Configuração da figura
fig, ax = plt.subplots()
ax.set_xlim(-L, L)
ax.set_ylim(-L, 0.5 * L)

line, = ax.plot([], [], lw=2)

# Criação da animação
ani = FuncAnimation(fig, update, frames=len(theta), fargs=(line,), interval=dt*1000, blit=True)

plt.title('Pêndulo de Foucault em Movimento')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
