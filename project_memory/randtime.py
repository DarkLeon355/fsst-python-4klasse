import random
import time

class RandomTimeGenerator:
    def __init__(self, start, end, time_format='%Y-%m-%d'):
        """
        Initialize the RandomTimeGenerator with a start date, end date, and date format.
        """
        self.start = start
        self.end = end
        self.time_format = time_format

    def str_time_prop(self, prop):
        """
        Get a date at a proportion of a range of two formatted dates.

        prop specifies how a proportion of the interval to be taken after start.
        The returned date will be in the specified format.
        """
        stime = time.mktime(time.strptime(self.start, self.time_format))
        etime = time.mktime(time.strptime(self.end, self.time_format))

        ptime = stime + prop * (etime - stime)

        return time.strftime(self.time_format, time.localtime(ptime))

    def random_date(self):
        """
        Generate a random date between the start and end dates.
        """
        return self.str_time_prop(random.random())


# Example usage
generator = RandomTimeGenerator("2020-01-01", "2025-01-01")
print(generator.random_date())