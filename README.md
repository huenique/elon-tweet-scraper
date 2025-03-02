# elon-tweet-scraper

## **✅ Features**

- Fetches **latest tweet** from **Elon Musk**.
- **Outputs JSON to console** if no file is specified.
- **Saves JSON to file** if `--output <path>` is used.
- **Uses `.env` for credentials** (no hardcoded secrets).
- **Validates required environment variables**.

## **🚀 Setup Guide**

### **1️⃣ Install Poetry**

This project uses [Poetry](https://python-poetry.org/) for dependency management. To install Poetry, use the official installer:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Once installed, verify it with:

```bash
poetry --version
```

### **2️⃣ Set Up the Virtual Environment**

```bash
poetry install
```

This will install all required dependencies inside a virtual environment.

### **4️⃣ Create and Configure the `.env` File**

Copy `.env.example` -> `.env` or create one file in the project root and add the following:

```bash
TWITTER_USERNAME=your_twitter_username
TWITTER_EMAIL=your_email@example.com
TWITTER_PASSWORD=your_twitter_password
TWITTER_COOKIES_FILE=cookies.json
```

Make sure to replace the placeholders with your actual credentials.

## **🛠 Usage**

### **1️⃣ Run the Script with Console Output (Default)**

```bash
poetry run python elon_tweet_scraper
```

**Example Output (formatted JSON)**:

```json
{
    "id": "1896158775498957299",
    "created_at": "Sun Mar 02 11:20:55 +0000 2025",
    "text": "Thank you!",
    "lang": "en",
    "favorite_count": 32109,
    "retweet_count": 3730,
    "reply_count": 2808,
    "view_count": "1919866",
    "user": "<User id=\"44196397\">",
    "full_text": "Thank you!",
    ...
}
```

### **2️⃣ Save Tweet to a JSON File**

```bash
poetry run python elon_tweet_scraper.py --output elon_tweet.json
```

**Output**:

```bash
✅ Tweet saved to: elon_tweet.json
```
