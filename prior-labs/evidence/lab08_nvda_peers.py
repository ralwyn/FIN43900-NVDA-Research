"""Reproduce the September 3, 2026 NVIDIA peer P/E references.

Prices are USD per share at the September 3 close; EPS is the latest
annual reported diluted USD per share available by that date.
"""

TARGET_EPS = 4.90
PEERS = {
    "AMD": {"price": 456.16, "eps": 2.65},
    "AVGO": {"price": 357.16, "eps": 4.77},
}


def implied_value(price, peer_eps, target_eps=TARGET_EPS):
    if peer_eps <= 0 or target_eps <= 0:
        raise ValueError("P/E requires positive annual earnings")
    return price / peer_eps * target_eps


if __name__ == "__main__":
    for ticker, data in PEERS.items():
        multiple = data["price"] / data["eps"]
        value = implied_value(data["price"], data["eps"])
        print(f"{ticker}: P/E {multiple:.2f}x; NVDA implied ${value:.2f}")
    values = [implied_value(**{"price": d["price"], "peer_eps": d["eps"]}) for d in PEERS.values()]
    print(f"Range: ${min(values):.2f}–${max(values):.2f}")
    print(f"Remove AMD: ${implied_value(PEERS['AVGO']['price'], PEERS['AVGO']['eps']):.2f}")
    print(f"Remove AVGO: ${implied_value(PEERS['AMD']['price'], PEERS['AMD']['eps']):.2f}")
