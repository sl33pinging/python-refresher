# TODO: Test all functions of physics, finish physics problem and fix any issues

import unittest
import physics
import numpy as np


class Test_Physics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(1, 400), 3924)
        try:
            physics.calculate_buoyancy(-10, 4000)
            physics.calculate_buoyancy(10, -300)
        except Exception as e:
            self.assertEqual(
                "volume and fluid density cannot be less than or equal to zero", str(e)
            )

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(30, 40000), 0)
        self.assertEqual(physics.will_it_float(100, 10), 1)
        try:
            physics.will_it_float(40, 40000)
        except Exception as e:
            self.assertEqual("object is neutrally buoyant", str(e))
        try:
            physics.will_it_float(-10, 0)
        except Exception as e:
            self.assertEqual(
                "volume and mass cannot be less than or equal to zero", str(e)
            )

    def test_calculate_pressure(self):
        with self.assertRaises(Exception) as e:
            physics.calculate_pressure(-10)
            self.assertEqual("please input the depth as a positive value", str(e))
        # try:
        #     physics.calculate_pressure(-10)
        # except Exception as e:
        #     self.assertEqual("please input the depth as a positive value", str(e))
        self.assertEqual(physics.calculate_pressure(300), 2943000)

    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(500, 10), 50)
        self.assertEqual(physics.calculate_acceleration(3034, 20), 151.7)
        try:
            physics.calculate_acceleration(45, 0)
        except Exception as e:
            self.assertEqual(str(e), "please input a positive value for the mass")

    def test_calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(678, 3), 226)
        self.assertEqual(physics.calculate_angular_acceleration(300, 20), 15)
        try:
            physics.calculate_angular_acceleration(45, -1)
        except Exception as e:
            self.assertEqual(
                str(e), "please input a positive value for the moment of inertia"
            )

    def test_calculate_torque(self):
        self.assertEqual(physics.calculate_torque(34, 76, 10), 329.9005469338388)
        self.assertEqual(physics.calculate_torque(46, 84, 10), 457.4800718694057)
        try:
            physics.calculate_torque(34, 76, -1)
        except Exception as e:
            self.assertEqual(str(e), "please input a positive value for the radius")

    def test_calculate_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(459, 30), 413100)
        self.assertEqual(physics.calculate_moment_of_inertia(989, 77), 5863781)
        try:
            physics.calculate_moment_of_inertia(459, -5)
        except Exception as e:
            self.assertEqual(str(e), "please input a positive value for the radius")
        try:
            physics.calculate_moment_of_inertia(0, 77)
        except Exception as e:
            self.assertEqual(str(e), "please input a positive value for the mass")

    def test_how_to_test_numpy_arrays(self):
        np.testing.assert_array_equal(physics.numpy_array_equal(), [[5, 6], [6, 7]])


if __name__ == "__main__":
    unittest.main()
