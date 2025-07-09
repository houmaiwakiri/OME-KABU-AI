import pyautogui
import time
from config import (
    ORDER_QUANTITY,
    ORDER_BUY_POSITION,
    ORDER_SELL_POSITION,
    ORDER_BUY_BUTTON,
    ORDER_SELL_BUTTON,
)

def click_and_type(position, text):
    pyautogui.moveTo(*position)
    pyautogui.click()
    pyautogui.typewrite(text)

def place_buy_order():
    # 信用新規買
    pyautogui.moveTo(*ORDER_BUY_POSITION)
    pyautogui.click()
    time.sleep(0.3)

    # 数量入力
    click_and_type(ORDER_BUY_BUTTON, ORDER_QUANTITY)
    time.sleep(0.2)

    # 注文確定
    pyautogui.moveTo(*ORDER_BUY_BUTTON)
    pyautogui.doubleClick()

def place_sell_order():
    # 信用返済売
    pyautogui.moveTo(*ORDER_SELL_POSITION)
    pyautogui.click()
    time.sleep(0.3)

    # 数量入力
    click_and_type(ORDER_SELL_BUTTON, ORDER_QUANTITY)
    time.sleep(0.2)

    # 注文確定
    pyautogui.moveTo(*ORDER_SELL_BUTTON)
    pyautogui.doubleClick()
