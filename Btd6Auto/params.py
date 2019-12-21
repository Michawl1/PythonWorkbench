import pyautogui

width, height = pyautogui.size()
widthRatio = width / 100
heightRatio = height / 100
winning_amount = 12

# select dark castle easy
step1 = 1075, 1200
step2 = 1890, 1270
step3 = 590, 765
step4 = 765, 515
step5 = 750, 790

# place obyn
step6 = 2260, 330  # drag to below
step7 = 1025, 590

# press space #

# scroll to super monkey
step8 = 2360, 530
scroll1 = -1000
step9 = 2270, 470  # drag to below
step10 = 1160, 570

path1 = 495, 700
path3 = 495, 1175

"""
place at 1140, 590
get after end of 10 start 11
upgrade 001 end of 21 start 22
upgrade 002 end of 25 start 26
upgrade 102 end of 30 start 31
upgrade 202 end of 36 start 37
"""

endstep1 = 1010, 1210

collectStep1 = 1280, 930

insta1 = 880, 715
insta2 = 1025, 715
insta3 = 1280, 715
insta4 = 1520, 715
insta5 = 1695, 715
# you can click anywhere after getting an insta
anyclick = 500, 500
# one last anyclick at the end to get off insta screen
backtohome = 100, 100
