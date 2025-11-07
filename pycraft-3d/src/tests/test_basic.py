import unittest
from pycraft.engine import GameEngine

class TestGameEngine(unittest.TestCase):
    def setUp(self):
        self.engine = GameEngine()

    def test_initialization(self):
        self.assertIsNotNone(self.engine)
        self.assertEqual(self.engine.state, "running")

    def test_update_frame(self):
        initial_frame_count = self.engine.frame_count
        self.engine.update()
        self.assertEqual(self.engine.frame_count, initial_frame_count + 1)

if __name__ == '__main__':
    unittest.main()