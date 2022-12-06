import unittest
from api_v1.services import movements


class Test_Movements(unittest.TestCase):
    def setUp(self):
        self.expected = [5, 1, "E"]

    def test_movements_output(self):
        top = [3, 3]
        position = [3, 3, "E"]
        instructions = "MMRMMRMRRM"
        output = movements(top, position, instructions)
        self.assertListEqual(output, self.expected)


if __name__ == "__main__":
    unittest.main()
