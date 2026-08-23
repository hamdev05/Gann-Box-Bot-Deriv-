# OANDA version — setup notes

This is the OANDA version of the bot (`oanda_client.py`, `backtest.py`,
`live_bot.py`, `scheduled_run.py`). It gives exact price-based TP/SL via real
limit orders, which is more precise than the Deriv version — but **OANDA does
not currently accept residents of Nigeria** (confirmed against OANDA's own
published country list as of August 2026), which is why this project's main
README focuses on Deriv instead. If you're eligible for OANDA, this version
is the better one to use.

## 1. Set up your free OANDA demo account

1. Go to https://www.oanda.com and sign up for a **practice (demo) account**
   — free, no card required.
2. Go to **"Manage API Access"** in account settings, generate a **Personal
   Access Token** → this is `OANDA_API_KEY`.
3. Your `OANDA_ACCOUNT_ID` is on your dashboard, formatted like
   `101-011-12345678-001`.

## 2. Install

```bash
pip install -r requirements.txt
cp .env.example .env
# fill in OANDA_API_KEY and OANDA_ACCOUNT_ID
```

Keep `OANDA_ENVIRONMENT=practice` until you've watched it run cleanly for a
good stretch of time.

## 3. Backtest

```bash
python backtest.py EUR_USD 2000
```

## 4. Run it

**PC / persistent server:**
```bash
python live_bot.py
```

**Phone-only via GitHub Actions:** upload the project to a public GitHub
repo (including `.github/workflows/gann-bot.yml`), add `OANDA_API_KEY` and
`OANDA_ACCOUNT_ID` as repository secrets (Settings → Secrets and variables →
Actions), and it'll run every 5 minutes automatically via `scheduled_run.py`.

See the main `README.md` for the fuller phone-only walkthrough — the steps
are identical, just swap the Deriv secrets/workflow file for the OANDA ones.
