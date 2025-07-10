import time
import pytesseract
import cv2
from config import TESSERACT_PATH
from modules.capture import get_price_info
from modules.rule import should_trade
from modules.order import place_order
from modules.logger import log_order, log_signal, log_error

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def main():
    print("[INFO]Start!!")
    already_ordered = False #trueの場合、注文発注しない

    try:
        while True:
            price, vwap = get_price_info()
            print(f"[INFO] Price: {price}, VWAP: {vwap}")

            action = should_trade(price, vwap)
            log_signal(signal=action, price=price, vwap=vwap)
            
            if action in ["buy", "sell"] and not already_ordered:
                place_order(action)
                log_order(order_type=action, price=price, vwap=vwap)
                already_ordered = True
                print("[INFO] "+ action)
            if action in ["buy_close","sell_close"]:
                # 返済注文処理追加予定
                # action = close
                # place_order(action)
                # already_ordered = False
                log_order(order_type=action, price=price, vwap=vwap)
                print("[INFO] "+ action)
            elif action is None:
                print("[ERROR] rule_out")
                log_error("rule_out", "rule_out")

            time.sleep(2)
    finally:
        print("[INFO] END...")

if __name__ == "__main__":
    main()
