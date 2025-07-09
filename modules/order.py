import pyautogui
import time
from config import (
    ORDER_QUANTITY,
    ORDER_OPEN_POSITION,
    ORDER_CLOSE_POSITION,
    ORDER_BUY_BUTTON,
    ORDER_SELL_BUTTON,
)

# 現状、注文数量は100固定
def click_and_type(position, order_quantity):
    # pyautogui.typewrite(order_quantity)
    pyautogui.moveTo(*position)
    pyautogui.doubleClick()

def place_order(order_type):
    print("[INFO] "+ order_type + " ordered")
    if order_type == "buy":
        pyautogui.moveTo(*ORDER_OPEN_POSITION)  # 信用新規買い
        pyautogui.click()
        time.sleep(0.3)
        click_and_type(ORDER_BUY_BUTTON, ORDER_QUANTITY)

    elif order_type == "sell":
        pyautogui.moveTo(*ORDER_OPEN_POSITION)  # 信用新規売り
        pyautogui.click()
        time.sleep(0.3)
        click_and_type(ORDER_SELL_BUTTON, ORDER_QUANTITY)

    elif order_type == "close":
        pyautogui.moveTo(*ORDER_CLOSE_POSITION)  # 信用返済
        pyautogui.click()
        time.sleep(0.3)
        click_and_type(ORDER_SELL_BUTTON, ORDER_QUANTITY)
