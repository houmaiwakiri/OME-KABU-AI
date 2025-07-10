# OME-KABU-AI

OME-KABU-AI は、VWAP（出来高加重平均価格）および現在値を OCR で取得し、一定の条件に基づいて自動的に買い／売り注文を行う、Python 製の株式自動売買システムです。

## 構成

OME-KABU-AI/  
　 main.py  
　 config.py  
　 requirements.txt  
　 modules/  
　　 order.py  
　　 capture.py  
　　 rule.py
(その他のモジュール)
debug/
(デバッグ用スクリプトやツール)

## 機能

- 画面上の価格情報を領域指定でキャプチャ
- OpenCV と Tesseract OCR による VWAP と現在値の文字認識
- 10 秒ごとの売買判断と自動注文（信用新規・信用返済）
- PyAutoGUI を使ったスピード注文操作

## 使用ライブラリ

- pyautogui
- pytesseract
- opencv-python
- Pillow
- pandas（必要に応じて）

## セットアップ手順

1. Tesseract OCR をインストール  
    Windows の場合は以下にインストールされるのが一般的です：
   C:\Program Files\Tesseract-OCR\tesseract.exe

python
コピーする
編集する

`config.py` に以下のようにパスを指定してください：

```python
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
Pythonパッケージのインストール

bash
コピーする
編集する
pip install -r requirements.txt
各種設定（config.py）

python
コピーする
編集する
# 画面キャプチャ領域やクリック位置などを環境に合わせて調整
CAPTURE_REGION_PRICE = (x, y, width, height)
ORDER_BUY_BUTTON = (x, y)

実行方法
bash
コピーする
編集する
python main.py
main.py の内容：

現在値とVWAPを取得

条件に応じて buy / sell / close を判断

該当する注文操作を実行

デバッグ
debug/mouse_position.pyでカーソル座標取得可能
```
