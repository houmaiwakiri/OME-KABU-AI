# OME-KABU-AI

OME-KABU-AI(AIではない) は、VWAP（出来高加重平均価格）および現在値を OCR で取得し、一定の条件に基づいて自動的に買い／売り注文を行う、Python 製の株式自動売買システムです。

## 構成

OME-KABU-AI/  
　 main.py  
　 config.py  
　 requirements.txt  
　 modules/  
　　 order.py  
　　 capture.py  
　　 rule.py  
　 debug/  
　　 mouse_position.py

## 機能

- 株式の情報を領域指定でキャプチャ
- OpenCV と Tesseract OCR を使用
- 10 秒ごとの売買判断と自動注文（信用新規・信用返済）
- PyAutoGUI を使った注文操作
- 管理用 注文履歴 CSV 出力

## 使用ライブラリ

- pyautogui
- pytesseract
- opencv-python
- Pillow
- pandas（必要に応じて）

## セットアップ手順

1. Tesseract OCR をインストール

`config.py` にパスを指定する：

```
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

2. Python パッケージのインストール

```
pip install -r requirements.txt
```

3. 各種設定（config.py）

```
# 画面キャプチャ領域やクリック位置などを環境に合わせて調整
CAPTURE_REGION_PRICE = (x, y, width, height)
ORDER_BUY_BUTTON = (x, y)
```

## 実行方法

```
python main.py
```

1. main.py の内容：

条件に応じて buy / sell / close を判断

該当する注文操作を実行

## デバッグ

- debug/mouse_position.py でカーソル座標取得可能
