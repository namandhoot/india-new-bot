
# India News Bot 🇮🇳

An automated bot that fetches breaking news from India and posts updates to Twitter and Facebook every 30 minutes. The bot curates news from reliable sources and formats them with appropriate hashtags and branding.

## Features 🌟

- Fetches latest breaking news from India using NewsAPI
- Posts updates every 30 minutes
- Cross-platform posting (Twitter & Facebook)
- Automatic hashtag generation
- Custom tweet formatting with branding
- Error handling and logging
- Trending news integration

## Prerequisites 📋

Before running this bot, you'll need:

- Python 3.7 or higher
- Twitter Developer Account
- Facebook Developer Account
- NewsAPI Account
- pip (Python package manager)

## Installation 🛠️

1. Clone the repository
```bash
git clone https://github.com/namandhoot/india-new-bot.git
cd india-new-bot
```

2. Install required dependencies
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your API credentials:
```env
# Twitter API Credentials
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_token_secret

# Facebook API Credentials
FACEBOOK_ACCESS_TOKEN=your_facebook_token
FACEBOOK_PAGE_ID=your_page_id

# News API Credentials
NEWS_API_KEY=your_news_api_key
```

## Configuration ⚙️

1. Twitter Setup:
   - Create a Twitter Developer account at developer.twitter.com
   - Create a new app and generate API keys and tokens
   - Enable Read and Write permissions for your app

2. Facebook Setup:
   - Create a Facebook Developer account
   - Create a new app
   - Generate a page access token
   - Get your Facebook page ID

3. NewsAPI Setup:
   - Register at newsapi.org
   - Get your API key

## Usage 🚀

To run the bot:
```bash
python bot.py
```

The bot will automatically:
- Fetch news every 30 minutes
- Format the news with appropriate hashtags
- Post to both Twitter and Facebook
- Log activities and any errors

## Project Structure 📁 
