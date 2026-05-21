"""Просте моделювання каналу крену квадрокоптера Х-схеми."""

import math
import random


def pid_control(error, integral, derivative, kp, ki, kd):
    return kp * error + ki * integral + kd * derivative


def saturate(signal, lower_limit, upper_limit):
    return max(lower_limit, min(upper_limit, signal))


def simulate_roll_channel(duration=10.0, dt=0.01):
    # Параметри об'єкта
    J_x = 0.02  # момент інерції, кг·м^2
    K = 0.5     # коефіцієнт перетворення керуючого сигналу у момент

    # PID-параметри
    Kp = 12.0
    Ki = 5.0
    Kd = 1.0

    # Обмеження сигналу управління
    u_min = -10.0
    u_max = 10.0

    # Початкові умови
    phi = 0.0
    phi_dot = 0.0
    phi_ref = math.radians(5.0)

    noise_std = math.radians(0.2)
    integral = 0.0
    previous_error = phi_ref - phi

    history = []

    for step in range(int(duration / dt)):
        error = phi_ref - phi
        integral += error * dt
        derivative = (error - previous_error) / dt
        previous_error = error

        # Збурення моменту (наприклад, порив вітру)
        disturbance = 0.005 * math.sin(0.5 * step * dt)

        u_unsat = pid_control(error, integral, derivative, Kp, Ki, Kd)
        u = saturate(u_unsat, u_min, u_max)

        # Анти-віндап: якщо сигнал насичений, корекція інтегралу
        if u != u_unsat:
            integral -= error * dt

        # Вимірювання кута з шумом
        measurement_noise = random.gauss(0.0, noise_std)
        y = phi + measurement_noise

        torque = K * u
        phi_ddot = (torque + disturbance) / J_x
        phi_dot += phi_ddot * dt
        phi += phi_dot * dt

        history.append((step * dt, phi, phi_dot, u, disturbance, y, measurement_noise))

    return history


if __name__ == "__main__":
    data = simulate_roll_channel()
    final_time, final_phi, final_phi_dot, final_u, final_disturbance, final_y, final_noise = data[-1]
    print(f"Час: {final_time:.2f} с")
    print(f"Кут крену: {math.degrees(final_phi):.3f}°")
    print(f"Кутова швидкість: {math.degrees(final_phi_dot):.3f}°/с")
    print(f"Останній керуючий сигнал: {final_u:.3f}")
    print(f"Останнє збурення: {final_disturbance:.5f}")
    print(f"Останнє виміряне значення: {math.degrees(final_y):.3f}°")
    print(f"Останній шум вимірювань: {math.degrees(final_noise):.3f}°")
