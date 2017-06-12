import unittest
from temp_converter import convert_celsius_to_farenheit

class TempConverterTest(unittest.TestCase):
	#given temp in test case get correct farenheit

	def test_celsius_converted_fareheit(self):
		"""
		F = C * 9/5 + 32
		"""
		actual = convert_celsius_to_farenheit(10)
		expected = 50

		self.assertEqual(actual, expected, msg='Celsius Should Convert to Correct Farenheit')

if __name__ == '__main__':
	unittest.main()
