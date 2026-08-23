"""
Configuration for the Gann Box bot.
Fill in credentials via a .env file (see .env.example) - never hardcode them here.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# --- Deriv credentials ---
DERIV_API_TOKEN = os.getenv("DERIV_API_TOKEN", "")
# 1089 is Deriv's public demo app_id, fine for initial testing. Register your
# own free app_id at api.deriv.com for anything beyond quick testing.
DERIV_APP_ID = os.getenv("DERIV_APP_ID", "1089")
DERIV_CURRENCY = os.getenv("DERIV_CURRENCY", "USD")

# OANDA-style pair names -> Deriv's forex symbol names
DERIV_SYMBOLS = {
    "EUR_USD": "frxEURUSD",
    "GBP_USD": "frxGBPUSD",
    "USD_JPY": "frxUSDJPY",
    "AUD_USD": "frxAUDUSD",
}

GRANULARITY_SECONDS = 900  # 15 minutes

# Multiplier for Deriv Multipliers contracts. Available values depend on your
# account/region/symbol - check in the Deriv Trader UI (Multipliers tab) what's
# offered for your forex pairs before assuming this value works.
MULTIPLIER = int(os.getenv("DERIV_MULTIPLIER") or "40")

# Minimum stake Deriv allows per contract (varies by symbol/currency - verify
# in-app; this is a conservative placeholder).
MIN_STAKE = 1.0

# --- OANDA credentials (used only if you're running the OANDA version instead) ---
OANDA_API_KEY = os.getenv("OANDA_API_KEY", "")
OANDA_ACCOUNT_ID = os.getenv("OANDA_ACCOUNT_ID", "")

# Practice (demo) vs live. ALWAYS start with "practice".
OANDA_ENVIRONMENT = os.getenv("OANDA_ENVIRONMENT", "practice")  # "practice" or "live"

OANDA_URLS = {
    "practice": "https://api-fxpractice.oanda.com",
    "live": "https://api-fxtrade.oanda.com",
}
OANDA_BASE_URL = OANDA_URLS[OANDA_ENVIRONMENT]

# --- Instruments to trade ---
# OANDA instrument names use underscores, e.g. EUR_USD
INSTRUMENTS = [
    "EUR_USD",
    "GBP_USD",
    "USD_JPY",
    "AUD_USD",
]

# --- Strategy settings ---
TIMEFRAME = "M15"          # 15 minute candles
RISK_PERCENT = 1.0         # % of account balance risked per trade
MAX_OPEN_TRADES_PER_PAIR = 1  # don't stack multiple pending/open trades on the same pair at once
PENDING_ORDER_TIMEOUT_CANDLES = 1  # cancel unfilled limit order after this many candles

# --- Live loop ---
POLL_SECONDS = 15  # how often the live bot checks for a new closed candle
