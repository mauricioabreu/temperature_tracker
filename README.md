# Temperature Tracker

Simple temperature tracker

Requirements:

* Python 3.6+

## What is this?

This is a simple temperature tracker object. The structure is composed by the following API:

`insert`: records a new temperature.

`get_max`: returns the highest temperature we have seen so far.

`get_min`: returns the lowest temperature we have seen so far.

`get_mean`: returns the mean of all temperatures we have seen so far.

## Examples

To use the TemperatureTracker, you need to spawn a new Python shell or write
the following lines into a file:

```python
from tracker import TemperatureTracker

temperature_tracker = TemperatureTracker()

# Registering temperatures
temperature_tracker.insert(22)
temperature_tracker.insert(23)
temperature_tracker.insert(21)

# Checking what is the maximum temperature we have collected so far
temperature_tracker.get_max()

# Checking what is the minimum temperature we have collected so far
temperature_tracker.get_min()

# Checking what is the mean temperature we have collected so far
temperature_tracker.get_mean()
```


You can read the code and tests to better understand how it works.
