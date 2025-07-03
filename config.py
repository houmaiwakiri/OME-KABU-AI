from datetime import time

# Tesseract OCR のパス
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 認識対象領域の座標設定（左上から横X, 左上から縦Y, 幅, 高さ）
CAPTURE_REGION = (940, 490, 450, 25)

# 注文エリアの位置（スピード注文）
ORDER_BUY_POSITION = (1380, 330)      # 買い「信用新規」
ORDER_SELL_POSITION = (1380, 270)     # 売り「信用返済」

ORDER_BUY_BUTTON = (1330, 490)        # 「買い」注文ボタン
ORDER_SELL_BUTTON = (1180, 490)       # 「売り」注文ボタン

# 注文ロット
ORDER_QUANTITY = "100"

# 最初の取引可能時間（9:03）
START_TIME = time(9, 3)
