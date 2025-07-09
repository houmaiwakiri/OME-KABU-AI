from datetime import time

# Tesseract OCR のパス
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 認識対象領域の座標設定（左上から横X, 左上から縦Y, 幅, 高さ）
CAPTURE_REGION_PRICE = (525, 175, 50, 25)
CAPTURE_REGION_VWAP = (1150, 290, 220, 20)

# 注文エリアの位置（スピード注文）
ORDER_OPEN_POSITION = (1630, 330)      # 信用新規選択
ORDER_CLOSE_POSITION = (1730, 330)     # 信用返済選択

ORDER_BUY_BUTTON = (1530, 540)        # 「買い」注文ボタン
ORDER_SELL_BUTTON = (1785, 540)       # 「売り」注文ボタン

# 注文ロット
ORDER_QUANTITY = "100"
