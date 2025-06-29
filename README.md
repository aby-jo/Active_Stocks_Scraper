# 📈 Active Stocks Scraper

This project automates the scraping of stock market data every 30 minutes during NYSE hours and sends a daily summary email after market close.

## 🔧 How It Works

### 🕑 1. Scraper Workflow (`stock-scraper`)
- **Runs every 30 minutes** from 9:30 AM to 4:00 PM EST (13:00–21:30 UTC)
- Scrapes stock data using `main.py`
- Saves output `.csv` files to the repository’s `data-store` branch using GitHub Actions

### 📬 2. Email Workflow (`send-stock-email`)
- **Runs at 4:30 PM EST** (22:00 UTC)
- Checks out the `data-store` branch
- Retrieves `send_and_clean.py` from the `main` branch
- Sends the collected `.csv` files as email attachments
- Cleans up the `data-store` branch by deleting `.csv` files

## 📂 Branch Structure

- `main`: Source code and workflow definitions
- `data-store`: Stores temporary `.csv` files collected during market hours

## ⚙️ GitHub Actions Configuration

Two workflows are defined in `.github/workflows/`:
- `scraper.yml`: Periodic scraping and CSV upload
- `send_email.yml`: Email dispatch and cleanup after close

## 🔐 Secrets Configuration

The following secrets must be configured in the repository:
- `PP`: Password or app password for SMTP email
- `SMAIL`: Sender email address
- `RMAIL`: Recipient email address

## 🛠️ Technologies Used

- Python 3.12
- Selenium
- GitHub Actions
- Gmail SMTP

## 📬 Example Output

Scraped files will be named like:
`stock_data_29-06-25_04-45-42_AM.csv`

And emailed as daily attachments after the market closes.

## 💡 Notes

- All automation is handled via GitHub Actions (no server needed)
- The `GITHUB_TOKEN` is used to authenticate pushes to `data-store`
- Be sure to keep email secrets secure

## 📜 License

MIT License