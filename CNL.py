from CNLIO_Pi import CNLButtons
from datetime import datetime
from time import sleep
from math import (floor, trunc)

class CNLHMI(CNLButtons):
    """
    This class extends :class:`CNL` with menu functions and management of power on/off
    and built-in time-outs (doze and power off).
    """

    def __init__(self):
        """Constants:"""
        self.DozeTime = 60
        self.OffTime = 180

        self.LastAction = datetime.min

        super(CNLHMI, self).__init__()

        self.WaitForTimeOut()
    
    """Supporting Methods for UI:"""
    def IdleTime(self):
        """Returns time since last noted action in seconds (float)"""
        return (datetime.now()-self.LastAction).total_seconds()
    
    def PowerIsOn(self):
        """Returns true if idle time is less than Off Time (boolean)"""
        return self.IdleTime() < self.OffTime

    def IsDozing(self):
        """Returns true if idle time is greater than doze time (boolean)"""
        return self.IdleTime() >= self.DozeTime

    def MakeAwake(self):
        if self.PowerIsOn():
            if self.IsDozing():
                self.Wake()
        else:
            self.PowerOn()

    def NoteAction(self, time=None):
        if time == None:
            time = datetime.today()
        self.LastAction = time

    """Basic Operations:"""
    def PowerOnOff(self):
        self.BtnPowerMenu.press(3)

    def Menu(self):
        self.MakeAwake()
        self.NoteAction()
        self.BtnPowerMenu.press()

    def TopUp(self):
        self.MakeAwake()
        self.NoteAction()
        self.BtnTopUp.press()

    def MiddleSelect(self):
        self.MakeAwake()
        self.NoteAction()
        self.BtnMiddleSelect.press()

    def BottomDown(self):
        self.MakeAwake()
        self.NoteAction()
        self.BtnBottomDown.press()

    """UI Level Operations:"""
    def ToggleUp(self, count=1):
        counter = 0
        while counter < count:
            self.TopUp()
            counter += 1
            
    def ToggleDown(self, count=1):
        counter = 0
        while counter < count:
            self.BottomDown()
            counter += 1

    def SelectTop(self):
        self.TopUp()

    def SelectMiddle(self):
        self.MiddleSelect()

    def SelectBottom(self):
        self.BottomDown()

    def Select(self):
        self.MiddleSelect()

    def Back(self):
        self.Menu()

    def PowerOn(self):
        if not self.PowerIsOn():
            self.PowerOnOff()
            sleep(5)
            self.NoteAction()

    def PowerOff(self):
        if self.PowerIsOn():
            self.PowerOnOff()
            self.NoteAction(datetime.min)

    def Wake(self):
        self.Menu()

    def WaitForTimeOut(self):
        print("Waiting for CNL power timeout ({:.0f} minutes)...".format(self.OffTime/60))
        sleep(self.OffTime)
        print("...ready.")

class CNL24(CNLHMI):
    """
    This class extends :class:`CNL` with a :meth:`remoteBolus` method.
    """

    def __init__(self):
        """Constants:"""
        self.pulse = 0.025
        self.bolusDeliveryRate = 0.025

        super(CNL24, self).__init__()
    
    def remoteBolus(self, amount=0):
        """
        Perform a remote bolus
        :param float amount:
            Amount of insulin to deliver in Units. Defaults to 0 Units.
            Rounded down to lower 0.025 Units.
        """

        """Check validity:"""
        if amount == 0:
            print("Bolus amount is zero, cancelling.")
            return(None)

        try:
            """Calculate bolus:"""
            clicks = floor(amount/self.pulse)
            bolusAmount = clicks * self.pulse
        
            """Calculate delivery time:"""
            deliveryDuration = bolusAmount/self.bolusDeliveryRate

            """Deliver bolus:"""
            print("Sending remote bolus of {:.3f} Units...".format(bolusAmount))

            """Select bolus"""
            self.SelectMiddle()
            """Select manual:"""
            self.SelectMiddle()
            """Wait for connection:"""
            sleep(5)
            """Toggle up:"""  """{:d} clicks".format(trunc(clicks)))"""
            self.ToggleUp(clicks)
            """Select amount:"""
            self.SelectMiddle()
            """Confirm:"""
            self.SelectMiddle()
            """Wait for send:"""
            sleep(3)
            """Acknowledge notification:"""
            self.SelectMiddle()
            """Wait for delivery:""" """({:d} seconds)".format(trunc(deliveryDuration)))"""
            sleep(deliveryDuration)       
            """Power off"""
            self.PowerOff()

            print("...sent")

            return bolusAmount

        except:
            print("...Error in sending bolus!")
            raise
