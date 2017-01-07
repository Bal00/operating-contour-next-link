from CNLIO_Pi import ButtonOperator
from time import sleep

print("Testing CNLIO_Pi...")

print("BtnPowerMenu = ButtonOperator(14)")
BtnPowerMenu = ButtonOperator(14)

print("BtnTopUp = ButtonOperator(15)")
BtnTopUp = ButtonOperator(15)

print("BtnMiddleSelect = ButtonOperator(18)")
BtnMiddleSelect = ButtonOperator(18)

print("BtnBottomDown = ButtonOperator(23)")
BtnBottomDown = ButtonOperator(23)


raw_input("BtnPowerMenu.press(3)")
BtnPowerMenu.press(3)
sleep(5)

raw_input("BtnBottomDown.press()")
BtnBottomDown.press()

raw_input("BtnTopUp.press()")
BtnTopUp.press()

raw_input("BtnMiddleSelect.press()")
BtnMiddleSelect.press()

raw_input("BtnPowerMenu.press(3)")
BtnPowerMenu.press(3)

print("...Test complete")
