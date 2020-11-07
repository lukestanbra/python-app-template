from unittest import TestCase
from package.hello_world import hello_world
import pytest

class TestDefault(TestCase):
    @pytest.fixture(autouse=True)
    def capfd(self, capfd):
        self.capfd = capfd

    def test_default(self):
        self.assertTrue(True)

    def test_hello_world(self):
        hello_world()
        captured = self.capfd.readouterr()
        self.assertEqual(
            "Hello, world!\n",
            captured.out
        )
