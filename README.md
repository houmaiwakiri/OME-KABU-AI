# OME-KABU-AI

OME-KABU-AI（※AI ではない）は、証券会社の取引画面から OCR で現在値と VWAP（出来高加重平均価格）を読み取り、指定ルールに従って自動で売買を行う Python 製の株式自動売買システムです。

## 構成

OME-KABU-AI/  
├── main.py - メイン実行ファイル  
├── config.py - 環境依存設定（座標・ロット数・OCR パス）  
├── requirements.txt - 必要ライブラリ  
├── README.md - 本ファイル  
├── modules/  
│ ├── capture.py - 現在値・VWAP を画像キャプチャ＋ OCR で取得  
│ ├── order.py - pyautogui による注文処理  
│ ├── rule.py - 売買条件の判定ロジック  
│ └── logger.py - CSV 形式ログ出力  
├── debug/  
│ └── mouse_position.py - 座標取得ツール  
├── output/  
│ ├── orders_YYYYMMDD.csv - 注文ログ  
│ ├── signals_YYYYMMDD.csv - 売買シグナルログ  
│ ├── errors_YYYYMMDD.csv - エラーログ  
│ └── info_YYYYMMDD.csv - 情報ログ

## 機能

- 株式画面の特定領域をキャプチャし、OpenCV ＋ Tesseract OCR で価格情報を取得
- VWAP と現在値に基づいた売買シグナル判定（rule.py）
- 売買シグナルに応じて、pyautogui を使用して自動的に信用新規・返済注文
- 実行情報・注文履歴・シグナル・エラーを CSV に出力（output/）

## 使用ライブラリ

- numpy : OCR にかける前の形式変換
- Pillow(PIL) : OCR にかける前の画像加工
- pytesseract : 画像から文字を抽出（OCR）する
- opencv-python(cv2) : 画像・動画の読み込み、加工、解析、カメラ制御
- pyautogui : マウス操作での注文に使用

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
# 価格・VWAPキャプチャ領域
CAPTURE_REGION_PRICE = (x1, y1, width1, height1)
CAPTURE_REGION_VWAP  = (x2, y2, width2, height2)

# 注文画面の操作位置
ORDER_OPEN_POSITION = (x, y)
ORDER_CLOSE_POSITION = (x, y)
ORDER_BUY_BUTTON = (x, y)
ORDER_SELL_BUTTON = (x, y)

# 注文数量
ORDER_QUANTITY = "100"
```

## 実行方法

```
python main.py
```

- 価格と VWAP を 2 秒間隔で取得
- 条件に合致すれば、注文クリック＋履歴記録
- 異常時は rule_out を出力し終了

## デバッグ

- debug/mouse_position.py でカーソル座標取得可能

## 注意事項

- 利用は自己責任です。確実に儲けられる投資はありません。
- 本システムは証券会社の画面に依存して動作します。
- UI の変更や画面サイズによっては動作しない可能性があります。
- 実際の注文が発生するため、十分に検証してください。
