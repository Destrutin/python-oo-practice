"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        self.start = start
        self.changing_number = start

    def __repr__(self):
        return f'<SerialGenerator start={self.start} changing_number={self.changing_number}>'

    def generate(self):
        new_number = self.changing_number
        self.changing_number += 1
        return new_number
    
    def reset(self):
        self.changing_number = self.start
        