import time
import pytesseract
import sys
from config import TESSERACT_PATH
from modules.capture import get_price_info
from modules.rule import should_trade
from modules.order import place_order
from modules.logger import log_order, log_signal, log_info ,log_error

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def main():
    log_info(" Start!!")
    already_ordered = False

    try:
        while True:
            price, vwap = get_price_info()
            log_info(f"Price: {price}, VWAP: {vwap}")

            action = should_trade(price, vwap)
            log_signal(signal=action, price=price, vwap=vwap)
            
            if action in ["buy", "sell"] and not already_ordered:
                place_order(action)
                log_order(order_type=action, price=price, vwap=vwap)
                already_ordered = True
                log_info(f" Price: {price}, VWAP: {vwap}")
                log_info(action)
            elif action in ["buy_close", "sell_close"]:
                log_order(order_type=action, price=price, vwap=vwap)
                log_info(action)
            elif action is None:
                log_info(" rule_out")
                log_error("rule_out")
                sys.exit(1)
            # シグナル捕捉間隔
            time.sleep(2)
    except Exception as e:
        log_error("exception", str(e))
        sys.exit(1)
    finally:
        log_info(" END...")

    sys.exit(0)

if __name__ == "__main__":
    main()
