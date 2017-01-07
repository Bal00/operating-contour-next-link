from gpiozero import DigitalOutputDevice
from time import sleep

class CNLButtons(object):
    """
    Represents a Contour Next Link operated by micro-relays wired in parallel
    with button switches.
    """

    def __init__(self):
        """Hard configuration:"""
        self.BtnPowerMenu = ButtonOperator(14)
        self.BtnTopUp = ButtonOperator(15)
        self.BtnMiddleSelect = ButtonOperator(18)
        self.BtnBottomDown = ButtonOperator(23)

class ButtonOperator(DigitalOutputDevice):
    """
    This class extends :class:`DigitalOutputDevice` with a :meth:`press` method and
    represents a button operator, typically a micro-relay operating a button
    switch.
    Connect the cathode of the micro-relay to a ground pin;
    connect the anode (via a limiting resistor?) to a GPIO pin.
    The following example will operate a button::
        from CNL import ButtonOperatorLED
        button = ButtonOperatorLED(14)
        button.press(3)
    :param int pin:
        The GPIO pin which the button operatorLED is attached to.
        See GPIOZero :ref:`pin_numbering` for valid pin numbers.
    """

    def __init__(self, pin=None):
        super(ButtonOperator, self).__init__(pin)

    def press(self, duration=0.2):
        """
        Perform a single synchronous button press
        :param float duration:
            Number of seconds pressed. Defaults to 0.2 seconds.
        """
        self.blink(duration, 0.3, 1, False)
