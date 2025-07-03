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
    pyautogui.press("enter")

def place_buy_order():
    pyautogui.moveTo(*ORDER_BUY_POSITION)
    pyautogui.click()
    time.sleep(0.3)
    click_and_type(ORDER_BUY_BUTTON, ORDER_QUANTITY)

def place_sell_order():
    pyautogui.moveTo(*ORDER_SELL_POSITION)
    pyautogui.click()
    time.sleep(0.3)
    click_and_type(ORDER_SELL_BUTTON, ORDER_QUANTITY)
