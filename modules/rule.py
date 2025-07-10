def should_trade(price, vwap):
    if price is None or vwap is None:
        return None

    if price > vwap:
        return "buy"
    elif price < vwap:
        return "sell"
    else:
        return None
