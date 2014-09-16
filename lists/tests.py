from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):
    """docstring for SmokeTest
    Stupid Test to fail
    """

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)