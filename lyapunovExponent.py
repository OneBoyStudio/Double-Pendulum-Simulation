import numpy as np
from scipy.integrate import odeint
import math
import csv

def double_pendulum(y, t, l1, l2, m1, m2, g):
    theta1, omega1, theta2, omega2 = y

    thetaDiff = theta1 - theta2
    sinThetaDiff = math.sin(thetaDiff)
    cosThetaDiff = math.cos(thetaDiff)

    bottom = (m1 + m2) - m2 * cosThetaDiff**2

    dydt = [
        omega1,
        (-sinThetaDiff * m2 * (omega2**2 * l2 + (l1 * omega1**2 * cosThetaDiff)) + 
        g * (m2 * math.sin(theta2) * cosThetaDiff - (math.sin(theta1) * (m1 + m2)))) / (l1 * bottom),
        omega2,
        (sinThetaDiff * (omega1**2 * l1 * (m1 + m2) + (l2 * omega2**2 * m2 * cosThetaDiff)) - 
        g * (m1 + m2) * (math.sin(theta2) - (cosThetaDiff * math.sin(theta1)))) / (l2 * bottom)
    ]

    return dydt

def lyapunov_exponents(y0, params, perturbation=1e-9, num_steps=100):
    t = np.linspace(0, 100, num_steps)
    
    # Initial perturbation
    perturbed_y0 = y0 + perturbation * np.random.randn(len(y0))
    
    # Integrate the unperturbed and perturbed trajectories
    unperturbed_solution = odeint(double_pendulum, y0, t, args=params)
    perturbed_solution = odeint(double_pendulum, perturbed_y0, t, args=params)
    
    # Calculate the differences between the trajectories
    differences = np.abs(unperturbed_solution - perturbed_solution)
    
    # Calculate the Lyapunov exponents
    exponents = np.zeros(len(y0))
    for i in range(len(y0)):
        exponents[i] = np.mean(np.log(differences[1:, i] / differences[:-1, i]))
    
    return exponents

def runForAllVals (L1, L2, M1, M2):

    # Parameters
    l1, l2 = L1, L2  # pendulum arm lengths
    m1, m2 = M1, M2  # mass of pendulum point masses
    g = 9.81  # acceleration constant (due to gravity)

    # Initial conditions [theta1, omega1, theta2, omega2]
    initial_conditions = [0, 0, 0, 0]

    lyapunov_exp = [0, 0, 0, 0]

    for i in range(60):

        exponent_calculated = lyapunov_exponents([initial_conditions[0] + (i * (np.pi/60)),
        initial_conditions[1],
        initial_conditions[2] + (i * (np.pi/60)),
        initial_conditions[3]],
        (l1, l2, m1, m2, g),)

        lyapunov_exp[0] += exponent_calculated[0]
        lyapunov_exp[1] += exponent_calculated[1]
        lyapunov_exp[2] += exponent_calculated[2]
        lyapunov_exp[3] += exponent_calculated[3]

    lyapunov_exp[0] = lyapunov_exp[0] / 60
    lyapunov_exp[1] = lyapunov_exp[1] / 60
    lyapunov_exp[2] = lyapunov_exp[2] / 60
    lyapunov_exp[3] = lyapunov_exp[3] / 60

    print("Lyapunov exponents:", lyapunov_exp)

    return lyapunov_exp

lyapunov_exp_graph = []

for i in range(50):

    lyapunov_exp_graph.append(runForAllVals(1 + i, 1 + i, 1 + i, 1 + i))

with open('litValue2.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(lyapunov_exp_graph)