import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertNotEqual(hello.hello(), "Hklmi")

    def test_add(self):
        self.assertEqual(hello.add(4, 3), 7)
        self.assertEqual(hello.add(1234, 4567), 5801)
        self.assertEqual(hello.add(36, 47), 83)

    def test_sub(self):
        self.assertEqual(hello.sub(4, 3), 1)
        self.assertEqual(hello.sub(1234, 4567), -3333)
        self.assertEqual(hello.sub(4, 4), 0)

    def test_mul(self):
        self.assertEqual(hello.mul(4, 3), 12)
        self.assertEqual(hello.mul(1234, 4567), 5635678)
        self.assertEqual(hello.mul(23, 13), 299)

    def test_div(self):
        self.assertEqual(hello.div(4, 3), 4 / 3)
        self.assertEqual(hello.div(1234, 4567), 1234 / 4567)
        try:
            hello.div(1, 0)
        except ValueError as v:
            self.assertEqual("Can't divide by zero!", str(v))

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)
        self.assertEqual(hello.sin(2), 0.9092974268256817)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)


if __name__ == "__main__":
    unittest.main()
