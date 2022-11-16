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
        "Create a serial number that starts at a predefined value."
        self.start = self.next = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        "This will return the serial number. Then, everytime you call this will return the next sequential number"
        self.next += 1
        return self.next - 1

    def reset(self):
        "This will reset the serial number to the original number you started with."
        self.next = self.start
