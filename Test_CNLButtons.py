print("from CNLIO_Pi import CNLButtons")
from CNLIO_Pi import CNLButtons
from time import sleep

print("cnl = CNLButtons()")
cnl = CNLButtons()

raw_input("cnl.BtnPowerMenu.press(3)")
cnl.BtnPowerMenu.press(3)
sleep(5)

raw_input("cnl.BtnBottomDown.press()")
cnl.BtnBottomDown.press()

raw_input("cnl.BtnTopUp.press()")
cnl.BtnTopUp.press()

raw_input("cnl.BtnMiddleSelect.press()")
cnl.BtnMiddleSelect.press()

raw_input("cnl.BtnPowerMenu.press(3)")
cnl.BtnPowerMenu.press(3)

print("...Test complete")

