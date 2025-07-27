import os
from datetime import datetime

OUTPUT_DIR = "output"

def _get_log_filename(prefix: str) -> str:
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"{prefix}_{date_str}.csv"
    return os.path.join(OUTPUT_DIR, filename)

def _timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def _write_log(filepath: str, line: str):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(filepath, mode="a", encoding="utf-8") as f:
        f.write(line + "\n")

# 注文ログ
def log_order(order_type: str, price: float, vwap: float):
    filepath = _get_log_filename("orders")
    line = f"[{_timestamp()}] [{order_type}] price={price} vwap={vwap}"
    _write_log(filepath, line)

# シグナルログ
def log_signal(signal: str, price: float, vwap: float):
    filepath = _get_log_filename("signals")
    line = f"[{_timestamp()}] [{signal}] price={price} vwap={vwap}"

    _write_log(filepath, line)
# インフォログ
def log_info(message: str):
    filepath = _get_log_filename("info")
    line = f"[{_timestamp()}] [INFO] {message}"
    _write_log(filepath, line)

# エラーログ
def log_error(message: str, exception: Exception = None):
    filepath = _get_log_filename("errors")
    error_detail = f" exception={str(exception)}" if exception else ""
    line = f"[{_timestamp()}] [error] {message}{error_detail}"
    _write_log(filepath, line)
