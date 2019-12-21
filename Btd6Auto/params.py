import pyautogui

width, height = pyautogui.size()
winning_amount = 12

# select dark castle easy
step1 = (width / 2.3814), (height / 1.2)
step2 = (width / 1.3545), (height / 1.1339)
step3 = (width / 4.3389), (height / 1.8824)
step4 = (width / 3.3464), (height / 2.7961)
step5 = (width / 3.4133), (height / 1.8182)

# place obyn
step6 = (width / 1.1327), (height / 4.3637)  # drag to below
step7 = (width / 2.4976), (height / 2.4407)

# scroll to super monkey
step8 = (width / 1.0847), (height / 2.7170)
scroll1 = -1000
step9 = (width / 1.1278), (height / 3.0638)  # drag to below
step10 = (width / 2.2069), (height / 2.5175)

path1 = (width / 5.1717), (height / 2.0571)
path3 = (width / 5.1717), (height / 1.2255)

"""
place at 1140, 590
get after end of 10 start 11
upgrade 001 end of 21 start 22
upgrade 002 end of 25 start 26
upgrade 102 end of 30 start 31
upgrade 202 end of 36 start 37
"""

endstep1 = (width / 2.5347), (height / 1.1901)

collectStep1 = (width / 2), (height / 1.5439)

insta1 = (width / 2.9091), (height / 2.014)
insta2 = (width / 2.4976), (height / 2.014)
insta3 = (width / 2), (height / 2.014)
insta4 = (width / 1.6842), (height / 2.014)
insta5 = (width / 1.5103), (height / 2.014)
# you can click anywhere after getting an insta
anyclick = (width / 5.12), (height / 2.88)
# one last anyclick at the end to get off insta screen
backtohome = (width / 25.6), (height / 14.4)
