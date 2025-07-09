import pyautogui
import time

print("マウスカーソルの位置を確認したい場所に移動してください。")
print("Ctrl+C で終了します。\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"現在の位置: ({x}, {y})", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n終了しました。")