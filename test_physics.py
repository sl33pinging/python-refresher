import unittest
import physics


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


if __name__ == "__main__":
    unittest.main()
