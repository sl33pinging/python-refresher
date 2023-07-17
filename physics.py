# TODO: also add a note in docstring that tells if there is an error that is going to be raised
# TODO: also check the shape of the Thruster magnitudes
# TODO: need to check like all shapes of the ndarrays

import numpy as np

_g = 9.81  # gravity
_density_water = 1000


def calculate_buoyancy(v, density_fluid):
    """return the buoyancy force in Newtons using volume and fluid density"""
    if v <= 0 or density_fluid <= 0:
        raise Exception("volume and fluid density cannot be less than or equal to zero")

    buoyancy_force = v * density_fluid * _g

    return buoyancy_force


def will_it_float(v, mass):
    """return whether or not the object is going to float using volume and mass"""
    if v <= 0 or mass <= 0:
        raise Exception("volume and mass cannot be less than or equal to zero")
    if mass / v != _density_water:
        return mass / v < _density_water
    else:
        raise Exception("object is neutrally buoyant")


def calculate_pressure(h):
    """calculates the pressure in Pascals at a given depth in water"""
    # h is the depth
    if h < 0:
        raise Exception("please input the depth as a positive value")
    hydrostatic_pressure = _density_water * _g * h
    return hydrostatic_pressure


def calculate_acceleration(F, m):
    """calculates the acceleration of an object given the force applied to it and its mass"""
    if m <= 0:
        raise Exception("please input a positive value for the mass")
    linear_acceleration = F / m
    return linear_acceleration


def calculate_angular_acceleration(tau, I):
    """calculates the angular acceleration of an object given the torque applied to it and its moment of inertia"""
    if I <= 0:
        raise Exception("please input a positive value for the moment of inertia")
    angular_acceleration = tau / I
    return angular_acceleration


def calculate_torque(F_magnitude, F_direction, r):
    """calculates the torque applied to an object given the force applied to it and the distance from the axis of rotation to the point where the force is applied"""
    if r <= 0:
        raise Exception("please input a positive value for the radius")
    torque = F_magnitude * r * np.sin(np.radians(F_direction))
    return torque


def calculate_moment_of_inertia(m, r):
    """calculates the moment of inertia of an object given its mass and the distance from the axis of rotation to the center of mass of the object"""
    if r <= 0:
        raise Exception("please input a positive value for the radius")
    if m <= 0:
        raise Exception("please input a positive value for the mass")
    moment_of_inertia = m * r**2
    return moment_of_inertia


def calculate_auv_acceleration(
    F_magnitude, F_angle=0, mass=100, volume=0.1, thruster_distance=0.5
):
    """return the acceleration of the AUV in meters per second squared"""
    auv_acceleration = F_magnitude / mass
    return auv_acceleration


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    """return the angular acceleration of the AUV in radians per second squared"""
    auv_angular_acceleration = (
        F_magnitude * thruster_distance * np.sin(np.radians(F_angle))
    ) / inertia
    return auv_angular_acceleration


def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    """calculates the acceleration of the AUV in the 2D plane"""
    sin_alpha = np.sin(alpha)
    cos_alpha = np.cos(alpha)
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    thruster_xy_forces_ratios = np.array(
        [
            [cos_alpha, cos_alpha, -cos_alpha, -cos_alpha],
            [sin_alpha, -sin_alpha, -sin_alpha, sin_alpha],
        ]
    )
    print(thruster_xy_forces_ratios)
    thrusters_magnitudes = np.array([[T[0]], [T[1]], [T[2]], [T[3]]])
    print(thrusters_magnitudes)
    forces_prime = np.dot(thruster_xy_forces_ratios, thrusters_magnitudes)
    print(forces_prime)
    rotational_matrix = np.array([[cos_theta, -sin_theta], [sin_theta, cos_theta]])
    forces = np.dot(rotational_matrix, forces_prime)
    auv2_acceleration = np.divide(forces, mass)
    print(auv2_acceleration)


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    """calculates the angular acceleration of the AUV"""
    sin_alpha = np.sin(alpha)
    cos_alpha = np.cos(alpha)
    radius = np.sqrt(L**2 + l**2)
    change_to_perpendicular = sin_alpha * L + cos_alpha * l
    thrusters_magnitudes = np.array([[T[0]], [T[1]], [T[2]], [T[3]]])
    thrusters_tau = thrusters_magnitudes * radius * change_to_perpendicular
    total_tau = (
        thrusters_tau[0] - thrusters_tau[1] + thrusters_tau[2] + thrusters_tau[3]
    )
    print(total_tau)
    auv2_angular_acceleration = total_tau / inertia
    print(auv2_angular_acceleration)


testarray = np.array([1, 3, 1, 2])
print(calculate_auv2_acceleration(testarray, 70, 40))
calculate_auv2_angular_acceleration(testarray, 0.5, 1.5, 1.8)


def numpy_array_equal():
    return np.array([[5, 6], [6, 7]])
