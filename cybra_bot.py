import time
import requests
import hmac
import hashlib

print("====================================")
print(" CYBRA MOMENTUM BOT")
print("====================================")

API_KEY = input("BYBIT API KEY: ").strip()
SECRET = input("BYBIT SECRET KEY: ").strip()

BASE = "https://api.bybit.com"

# -------------------------
# PRICE
# -------------------------

def price():

    try:

        r = requests.get(
            BASE + "/v5/market/tickers",
            params={
                "category": "spot",
                "symbol": "BTCUSDT"
            },
            timeout=3
        )

        return float(
            r.json()["result"]["list"][0]["lastPrice"]
        )

    except:

        return None

# -------------------------
# SIGNAL
# -------------------------

buf = []

def signal(p):

    buf.append(p)

    if len(buf) > 20:
        buf.pop(0)

    avg = sum(buf) / len(buf)

    if p > avg * 1.001:
        return "Buy"

    if p < avg * 0.999:
        return "Sell"

    return "Hold"

# -------------------------
# SIGN
# -------------------------

def sign(payload):

    q = "&".join(
        [f"{k}={v}" for k,v in sorted(payload.items())]
    )

    return hmac.new(
        SECRET.encode(),
        q.encode(),
        hashlib.sha256
    ).hexdigest()

# -------------------------
# ORDER
# -------------------------

def order(side):

    ts = str(int(time.time() * 1000))

    payload = {
        "category": "spot",
        "symbol": "BTCUSDT",
        "side": side,
        "orderType": "Market",
        "qty": "0.001",
        "timestamp": ts
    }

    headers = {
        "X-BAPI-API-KEY": API_KEY,
        "X-BAPI-SIGN": sign(payload),
        "X-BAPI-TIMESTAMP": ts
    }

    try:

        r = requests.post(
            BASE + "/v5/order/create",
            data=payload,
            headers=headers,
            timeout=5
        )

        print("[ORDER]", r.json())

    except Exception as e:

        print("[ORDER ERROR]", e)

# -------------------------
# LOOP
# -------------------------

print("\n[CYBRA ACTIVE]\n")

while True:

    p = price()

    if not p:

        print("[WAIT PRICE]")

        time.sleep(2)

        continue

    sig = signal(p)

    print("[PRICE]", p, "[SIGNAL]", sig)

    if sig in ["Buy", "Sell"]:

        order(sig)

    time.sleep(2)
