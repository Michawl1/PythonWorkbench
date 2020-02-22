"""
@author Michael Thompson (mjt106@case.edu)
@about This is a script used to automate farming in BTD6
"""

import pyautogui as auto
import time
import params as params
import sys


def select_map_mode():
    '''
    Selects dark castle easy mode
    '''
    time.sleep(1)
    auto.click(params.step1[0], params.step1[1])
    time.sleep(2)
    auto.click(params.step2[0], params.step2[1])
    time.sleep(2)
    auto.click(params.step3[0], params.step3[1])
    time.sleep(2)
    auto.click(params.step4[0], params.step4[1])
    time.sleep(2)
    auto.click(params.step5[0], params.step5[1])
    time.sleep(6)


def place_obyn():
    """
    Places obyn on dark castle
    """
    auto.moveTo(params.step6[0], params.step6[1])
    time.sleep(1)
    auto.dragTo(params.step7[0], params.step7[1], duration=1, button='right')
    time.sleep(1)
    auto.click(params.step7[0], params.step7[1])
    time.sleep(1)


def place_super():
    """
    Places a super monkey on dark castle

    @pre The game must have enough money to purchase a super
    """
    auto.moveTo(params.step8[0], params.step8[1], duration=1)
    for i in range(0, 25):
        auto.scroll(params.scroll1)

    auto.moveTo(params.step9[0], params.step9[1])
    time.sleep(1)
    auto.dragTo(params.step10[0], params.step10[1], duration=1, button='right')
    time.sleep(1)
    auto.click(params.step10[0], params.step10[1])
    time.sleep(1)


def upgrade_path1():
    """
    Upgrades path 1 on the right

    @pre The game must have enough money to purchase the upgrade
    """
    auto.click(params.step10[0], params.step10[1])
    time.sleep(1)
    auto.click(params.path1[0], params.path1[1])
    time.sleep(1)
    auto.click(params.step10[0], params.step10[1])
    time.sleep(1)


def upgrade_path3():
    """
    Upgrades path 3 on the right

    @pre The game must have enough money to purchase the upgrade
    """
    auto.click(params.step10[0], params.step10[1])
    time.sleep(1)
    auto.click(params.path3[0], params.path3[1])
    time.sleep(1)
    auto.click(params.step10[0], params.step10[1])
    time.sleep(1)


def collect_insta():
    """
    Collects insta monkeys from both the 3 and 2 reward config
    """
    auto.click(params.collectStep1[0], params.collectStep1[1])
    time.sleep(2)

    auto.click(params.insta1[0], params.insta1[1])
    time.sleep(1)
    auto.click(params.anyclick[0], params.anyclick[1])
    time.sleep(1)

    auto.click(params.insta3[0], params.insta3[1])
    time.sleep(1)
    auto.click(params.anyclick[0], params.anyclick[1])
    time.sleep(1)

    auto.click(params.insta5[0], params.insta5[1])
    time.sleep(1)
    auto.click(params.anyclick[0], params.anyclick[1])
    time.sleep(1)

    auto.click(params.insta2[0], params.insta2[1])
    time.sleep(1)
    auto.click(params.anyclick[0], params.anyclick[1])
    time.sleep(1)

    auto.click(params.insta4[0], params.insta4[1])
    time.sleep(1)
    auto.click(params.anyclick[0], params.anyclick[1])
    time.sleep(1)

    auto.click(params.backtohome[0], params.backtohome[1])
    time.sleep(1)
    auto.click(params.backtohome[0], params.backtohome[1])
    time.sleep(3)


def go_home():
    """
    Takes the user home after a victory in a game
    """
    auto.click(params.endstep1[0], params.endstep1[1])
    time.sleep(4)


def pointer_output():
    """
    Outputs cursor position
    """
    while True:
        time.sleep(0.05)
        print(auto.position())


if __name__ == "__main__":
    total = 50
    winning_requirement = 70
    time_modifier = 1.15

    start = 0
    end = 0

    while (True):
        start = time.time()
        time.sleep(2)
        select_map_mode()
        place_obyn()

        auto.press(keys='space')
        time.sleep(0.5)
        auto.press(keys='space')

        time.sleep(100 * time_modifier)

        place_super()

        time.sleep(64 * time_modifier)

        upgrade_path3()

        time.sleep(35 * time_modifier)

        upgrade_path3()

        time.sleep(40 * time_modifier)

        upgrade_path1()

        time.sleep(40 * time_modifier)

        upgrade_path1()

        time.sleep(40 * time_modifier)

        go_home()
        total += params.winning_amount

        if total >= winning_requirement:
            collect_insta()
            total -= winning_requirement

        end = time.time()
        print("Runtime: {}".format(end - start))
