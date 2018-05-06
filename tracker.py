import unittest


class InvalidTemperature(Exception):
    """Raise when an invalid temperature is
    added to the tracker."""
    pass


class TemperatureTracker(object):

    def __init__(self):
        self.temperatures = []
        self.max_temperature = None
        self.min_temperature = None

    def insert(self, temperature: int) -> None:
        """Insert a new temperature on the tracker.
        It is added in the end the collection, keeping
        the order from the most recent to the oldest temperature."""
        # Check temperature value
        self.validate_temperature(temperature)
        # Record the temperature
        self.temperatures.append(temperature)
        # Set maximum temperature
        self.set_max(temperature)
        # Set minimum temperature
        self.set_min(temperature)

    def set_max(self, temperature):
        if not self.max_temperature or temperature > self.max_temperature:
            self.max_temperature = temperature
        return self.max_temperature

    def set_min(self, temperature):
        if not self.min_temperature or temperature < self.min_temperature:
            self.min_temperature = temperature
        return self.min_temperature

    def validate_temperature(self, temperature: int) -> None:
        """Check if the temperature is a valid value."""
        if (temperature < 0 or temperature > 100) or not isinstance(temperature, int):
            raise InvalidTemperature(
                'Temperature must be an integer between 0 and 100')

    def get_max(self):
        """Return the maximum temperature tracked."""
        return self.max_temperature

    def get_min(self):
        """Return the minimum temperature tracked."""
        return self.min_temperature

    def get_mean(self) -> float:
        """Return the mean temperature tracked."""
        return sum(self.temperatures) / len(self.temperatures)

    def __getitem__(self, index: int) -> int:
        """Return the element in the given index.
        This function overrides the list indexing protocol.
        Example:
            >>> temperature_tracker = TemperatureTracker()
            >>> temperature_tracker.insert(15)
            >>> temperature_tracker[0]
            >>> 15
        """
        return self.temperatures[index]


class TestTemperatureTracker(unittest.TestCase):

    def test_insert(self):
        temperature_tracker = TemperatureTracker()
        temperature_tracker.insert(22)
        self.assertEqual(temperature_tracker[-1], 22)
        temperature_tracker.insert(21)
        self.assertEqual(temperature_tracker[-1], 21)

    def test_insert_with_invalid_temperature(self):
        temperature_tracker = TemperatureTracker()
        # Insert a value that is too low...
        with self.assertRaises(InvalidTemperature):
            temperature_tracker.insert(-3)

        # Insert a value that is too high...
        with self.assertRaises(InvalidTemperature):
            temperature_tracker.insert(101)

        # Insert a non-integer value...
        with self.assertRaises(InvalidTemperature):
            temperature_tracker.insert(3.0)

    def test_get_max(self):
        temperature_tracker = TemperatureTracker()
        temperature_tracker.insert(10)
        temperature_tracker.insert(15)
        temperature_tracker.insert(12)
        self.assertEqual(temperature_tracker.get_max(), 15)

    def test_get_min(self):
        temperature_tracker = TemperatureTracker()
        temperature_tracker.insert(12)
        temperature_tracker.insert(8)
        temperature_tracker.insert(10)
        self.assertEqual(temperature_tracker.get_min(), 8)

    def test_get_mean(self):
        temperature_tracker = TemperatureTracker()
        temperature_tracker.insert(3)
        temperature_tracker.insert(4)
        temperature_tracker.insert(5)
        self.assertEqual(temperature_tracker.get_mean(), 4.0)


if __name__ == '__main__':
    unittest.main()
