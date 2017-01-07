print("from CNL import CNLHMI")
from CNL import CNLHMI

print("cnl = CNLHMI()")
cnl = CNLHMI()

raw_input("cnl.ToggleDown(2)")
cnl.ToggleDown(2)

raw_input("cnl.ToggleUp()")
cnl.ToggleUp()

raw_input("cnl.Select()")
cnl.Select()

raw_input("cnl.PowerOff()")
cnl.PowerOff()

print("...Test complete")

