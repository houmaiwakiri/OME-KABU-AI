import pyautogui
import pytesseract
import cv2
import numpy as np
from PIL import Image
import re
from config import CAPTURE_REGION_PRICE, CAPTURE_REGION_VWAP

def capture_image(region):
    return pyautogui.screenshot(region=region)

def preprocess_for_ocr(pil_img):
    img = np.array(pil_img)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
    return Image.fromarray(binary), binary

def extract_vwap(text):
    vwap = None
    # カンマ削除
    text = text.replace(",", "")
    for line in text.splitlines():
        line = line.strip()
        if "VWAP" in line.upper():
            found = re.findall(r"\d{1,6}\.\d{1,10}", line)
            if found:
                vwap = float(found[0])
    return vwap

def extract_price(text):
    found = re.findall(r"\d{1,3}(?:,\d{3})*(?:\.\d+)?", text)
    if found:
        # カンマ除去数値変換
        cleaned = found[0].replace(",", "")
        #小数点除去
        return int(float(cleaned))
    return None


def capture_and_extract(region, extractor_fn, label="", lang="eng"):
    img = capture_image(region)
    processed_pil, _ = preprocess_for_ocr(img)

    # デバッグ用：画像表示
    # processed_pil.show(title=f"{label} OCR Image")

    # OCR実行
    text = pytesseract.image_to_string(processed_pil, lang=lang, config="--psm 7")

    # デバッグ用：抽出文字列表示
    # print(f"[DEBUG] {label}:{text}\n")
    
    return extractor_fn(text)

def get_price_info():
    price = capture_and_extract(CAPTURE_REGION_PRICE, extract_price, label="PRICE", lang="eng")
    vwap = capture_and_extract(CAPTURE_REGION_VWAP, extract_vwap, label="VWAP", lang="eng")
    return price, vwap
