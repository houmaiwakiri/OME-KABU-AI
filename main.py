import time
import pytesseract
import cv2
from config import TESSERACT_PATH
from modules.recognizer import get_price_info
from modules.rule_engine import should_trade
from modules.order import place_buy_order, place_sell_order

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def main():
    print("Starting bot...")
    already_ordered = False

    try:
        while True:
            price, vwap = get_price_info()
            print(f"Price: {price}, VWAP: {vwap}")

            action = should_trade(price, vwap)

            if action == "buy" and not already_ordered:
                place_buy_order()
                already_ordered = True
                print("BUY ORDER SENT")
            elif action == "sell" and not already_ordered:
                place_sell_order()
                already_ordered = True
                print("SELL ORDER SENT")

            time.sleep(10)
    finally:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
