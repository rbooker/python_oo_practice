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
   		 """Initializes the starting value of the serial number, startnum, with a default value of 0.
   		 Also initializes the attribute serialnum to the value of startnum""" 
   		 self.startnum = start
   		 self.serialnum = self.startnum

    def generate(self):
    	"""Increments the serial number by one, and returns its pre-incrementation value"""
    	self.serialnum += 1
    	return self.serialnum - 1

    def reset(self):
    	"""Resets the value of the serial number to its initial value"""
    	self.serialnum = self.startnum
