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
