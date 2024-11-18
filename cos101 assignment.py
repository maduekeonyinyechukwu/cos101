#program to calculate speed
def calculate_speed(distance, time):
    if time == 0
        return "time cannot be zero!"
    return distance / time

# user input
distance = float(input("Enter distance in meters: "))
time = float(input("Enter time in seconds: "))

# output
print (f"the speed is {calculate_speed(distance, time)} m/s.")


# program to calculate force
def calculate_force(mass, acceleration):
    return mass * acceleration

# user input
mass = float(input("Enter mass in kilograms: "))
acceleration = float(input("Enter acceleration in m/s^2): "))

# output
print (f"the force is {calculate_force(mass, acceleration)} N (Newton).")


# program to calculate kinetic energy
def calculate_kinetic_energy(mass, velocity):
   return 0.5 * mass * velocity ** 2

# user input
mass = float(input("Enter mass in kilograms: "))
velocity = float(input("Enter velocity in m/s: "))

#output
print(f"the kinetic energy is {calculate_kinetic_energy(mass, velocity)} J (Joule).")


# Gravitational force: F = G * (m1 * m2) / r^2
def gravitational_force(m1, m2, r):
    G = 6.67430e-11 #Gravitational constant
    return G * (m1 * m2) / r**2


# Coloumb's Law: F = k * |q1 * q2| / r^2
def electrostatic_force(q1, q2, r):
    k = 8.9875e9 # Couloumb's constant (N.m^2/C^2)
    return k * abs(q1 * q2) / r**2