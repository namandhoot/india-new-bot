import requests
import tweepy
import schedule
import time
<<<<<<< HEAD
from datetime import datetime, timedelta
=======
from datetime import datetime
>>>>>>> eec9f4d (Initial commit of the news Twitter bot project)
import feedparser
import google.generativeai as genai

# News API Configuration (using RSS)
NEWS_API_URL = "https://www.thehindu.com/news/national/feeder/default.rss"  # The Hindu RSS feed

# Twitter API Configuration
<<<<<<< HEAD
TWITTER_API_KEY = "YOUR_TWITTER_API_KEY"
TWITTER_API_SECRET = "YOUR_TWITTER_API_SECRET"
TWITTER_ACCESS_TOKEN = "YOUR_TWITTER_ACCESS_TOKEN"
TWITTER_ACCESS_TOKEN_SECRET = "YOUR_TWITTER_ACCESS_TOKEN_SECRET"

# Gemini API Configuration
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

class TwitterBot:
    def __init__(self, api):
        self.api = api
        self.last_tweet_time = None
        self.tweet_counter = 0
        self.reset_time = datetime.now() + timedelta(hours=24)

    def check_limits(self):
        try:
            limits = self.api.rate_limit_status()
            remaining = limits['resources']['statuses']['/statuses/update']['remaining']
            print(f"Remaining tweets allowed: {remaining}")
            return remaining > 0
        except Exception as e:
            print(f"Error checking limits: {e}")
            return False

    def post_tweet(self, tweet_text):
        # Check if we've waited long enough since last tweet
        if self.last_tweet_time:
            elapsed = datetime.now() - self.last_tweet_time
            if elapsed.total_seconds() < 300:  # Wait at least 5 minutes between tweets
                wait_time = 300 - elapsed.total_seconds()
                print(f"Waiting {int(wait_time)} seconds before next tweet...")
                time.sleep(wait_time)

        # Check daily limit
        if datetime.now() > self.reset_time:
            self.tweet_counter = 0
            self.reset_time = datetime.now() + timedelta(hours=24)

        if self.tweet_counter >= 45:  # Keep safe margin below 50
            print("Daily tweet limit reached. Waiting until reset...")
            time.sleep(3600)  # Wait an hour
            return

        try:
            if self.check_limits():
                print(f"Attempting to post tweet: {tweet_text[:50]}...")
                self.api.update_status(tweet_text)
                self.last_tweet_time = datetime.now()
                self.tweet_counter += 1
                print(f"Tweet posted successfully at {self.last_tweet_time}")
                print(f"Tweets posted today: {self.tweet_counter}")
                return True
            else:
                print("Rate limit in effect, waiting...")
                time.sleep(900)  # Wait 15 minutes
                return False
        except tweepy.RateLimitError:
            print("Rate limit exceeded. Waiting 15 minutes...")
            time.sleep(900)
            return False
        except tweepy.TweepError as e:
            if 'duplicate' in str(e).lower():
                print("Duplicate tweet detected, skipping...")
                return False
            print(f"Twitter error: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

=======
TWITTER_API_KEY = "ZGnX2cMRVo00wB3YRhufX3ZX0"
TWITTER_API_SECRET = "Wuvt6vll0yK7MHqeVuoelJgg3CHfZ0eA5Fowi0ey1LTpwqFaA9"
TWITTER_ACCESS_TOKEN = "1886632487146975232-NTPPsoLgsf7Jg0kNhl8CTY68NNWC5U"
TWITTER_ACCESS_TOKEN_SECRET = "5TeYi1fYoZIx4PjA8oT4xvMIZc0EyEETJIOyAZAjvgdIe"

# Gemini API Configuration
GEMINI_API_KEY = "AIzaSyAd208wmxt5GJpNA670ZuZuHHgLKBahtRU"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

>>>>>>> eec9f4d (Initial commit of the news Twitter bot project)
def summarize_news(title, url):
    try:
        prompt = f"""Summarize this news article comprehensively in 100-200 words:
        Title: {title}
        URL: {url}
        
        Rules:
        1. Include all important details and context
        2. Use clear, journalistic writing style
        3. Cover who, what, when, where, why aspects
        4. Maintain a neutral tone
        5. Don't mention any source
        6. Don't add any hashtags
        7. Make it engaging and informative
        8. Minimum 100 words, maximum 200 words"""
        
        response = model.generate_content(prompt)
        summary = response.text.strip()
        
        # Ensure the summary isn't too long for Twitter
        if len(summary) > 240:
            # Try to find a sentence break near 240 characters
            last_period = summary[:240].rfind('.')
            if last_period > 0:
                summary = summary[:last_period + 1]
            else:
                summary = summary[:237] + "..."
        
        # Add Gatiman News at the end
        tweet = f"{summary}\n\n- Gatiman News 📰"
        return tweet
    except Exception as e:
        print(f"Error in summarization: {str(e)}")
        # Fallback to original title if summarization fails
        tweet = f"{title[:200]}...\n\n- Gatiman News 📰"
        return tweet

def get_top_news():
    print("Fetching news...")
    try:
        print("Making request to The Hindu RSS feed...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(NEWS_API_URL, headers=headers)
        print(f"Response status code: {response.status_code}")
        print(f"Response content length: {len(response.content)}")
        
        if response.status_code == 200:
            feed = feedparser.parse(response.content)
            print(f"Number of entries: {len(feed.entries) if hasattr(feed, 'entries') else 0}")
            
            if hasattr(feed, 'entries') and feed.entries:
                articles = feed.entries[:2]
                tweets = []
                
                for article in articles:
                    title = article.get("title", "")
                    url = article.get("link", "")
                    
                    if title and url:
                        tweet = summarize_news(title, url)
                        if tweet:
                            tweets.append(tweet)
                            print(f"Prepared tweet: {tweet[:50]}...")
                
                return tweets
            else:
                print("Feed parsed but no entries found")
                print(f"Feed keys available: {feed.keys() if hasattr(feed, 'keys') else 'No keys'}")
        
        print("Failed to fetch the feed")
        print(f"Response content: {response.text[:500]}...")  # Print first 500 chars of response
        return None
    except Exception as e:
        print(f"Error fetching news: {str(e)}")
        print(f"Error type: {type(e)}")
        return None

<<<<<<< HEAD
def main():
    # Your existing authentication code
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    bot = TwitterBot(api)
    
    print("Starting Gatiman News Bot...")
    while True:
        try:
            print("Fetching news...")
            tweet_text = get_top_news()  # Your existing news fetching function
            
            if tweet_text:
                if bot.post_tweet(tweet_text):
                    # Successfully posted, wait for next hour
                    print("Waiting for next scheduled post...")
                    time.sleep(3600)  # Wait 1 hour
                else:
                    # Failed to post, wait shorter time
                    print("Waiting before retry...")
                    time.sleep(300)  # Wait 5 minutes
            else:
                print("No news to post, waiting...")
                time.sleep(300)
                
        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(300)

if __name__ == "__main__":
    main() 
=======
def post_tweet(tweet_text):
    print(f"Attempting to post tweet: {tweet_text[:50]}...")
    try:
        # Initialize Twitter API v2 with additional parameters
        client = tweepy.Client(
            consumer_key=TWITTER_API_KEY,
            consumer_secret=TWITTER_API_SECRET,
            access_token=TWITTER_ACCESS_TOKEN,
            access_token_secret=TWITTER_ACCESS_TOKEN_SECRET,
            wait_on_rate_limit=True
        )
        
        # Post tweet
        print("Sending tweet to Twitter...")
        response = client.create_tweet(
            text=tweet_text,
        )
        print(f"Tweet posted successfully at {datetime.now()}")
        print(f"Response from Twitter: {response}")
        return True
    except tweepy.errors.TweepyException as e:
        print(f"Twitter API Error: {str(e)}")
        if "403" in str(e):
            print("Please check Twitter app permissions in the developer portal")
        elif "429" in str(e):  # Rate limit exceeded
            print("Rate limit exceeded. Sleeping for a while...")
              # Sleep for 15 minutes
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        print(f"Error type: {type(e)}")
        return False

def job():
    news_tweets = get_top_news()
    if news_tweets:
        for tweet in news_tweets:
            post_tweet(tweet)
            time.sleep(60)  # Wait 1 minute between tweets

def main():
    print("Starting Gatiman News Bot...")
    # Schedule the job to run every 30 minutes
    schedule.every(30).minutes.do(job)
    
    # Run the first tweet immediately
    job()
    
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    main() 
>>>>>>> eec9f4d (Initial commit of the news Twitter bot project)
