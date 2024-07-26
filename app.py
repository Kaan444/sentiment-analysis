from urllib.request import urlopen, Request, HTTPError
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
import urllib
from datetime import datetime, timedelta


def get_tickers_from_user():
    tickers = input("Enter the ticker symbols separated by commas: ").strip().split(',')
    return [ticker.strip().upper() for ticker in tickers]

# parses the date from strings
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%b-%d-%y').date()
    except ValueError:
        try:
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return None  


def fetch_news(tickers):
    finviz_url = 'https://finviz.com/quote.ashx?t='
    news_tables = {}
    
    for ticker in tickers:
        url = finviz_url + ticker
        req = Request(url=url, headers={'User-Agent': 'my-app'})
        
        try:
            response = urlopen(req)
            html = BeautifulSoup(response, features='html.parser')
            news_table = html.find(id="news-table")
            
            if news_table:
                news_tables[ticker] = news_table
            else:
                print(f"No news table found for ticker: {ticker}")
                
        except HTTPError as e:
            print(f"HTTPError for ticker {ticker}: {e}")
        except urllib.error.URLError as e:
            print(f"URLError for ticker {ticker}: {e}")
        except Exception as e:
            print(f"General exception for ticker {ticker}: {e}")
    
    return news_tables

# Parses the news data from HTML
def parse_news_data(news_tables):
    parsed_data = []
    
    for ticker, news_table in news_tables.items():
        for row in news_table.findAll('tr'):
            title = row.a.text
            date_data = row.td.text.strip().split(' ')
            
            if len(date_data) == 1:
                date_str = datetime.today().strftime('%Y-%m-%d')
                time = date_data[0].strip()
            else:
                date_str = date_data[0].strip()
                time = date_data[1].strip()
                
                if date_str == "Today":
                    date_str = datetime.today().strftime('%Y-%m-%d')
                elif date_str == "Yesterday":
                    date_str = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
            
            date = parse_date(date_str)
            if date:
                parsed_data.append({
                    'ticker': ticker,
                    'date': date,
                    'time': time,
                    'title': title.strip()
                })
    
    return parsed_data


def main():
    tickers = get_tickers_from_user()
    news_tables = fetch_news(tickers)
    parsed_data = parse_news_data(news_tables)
    
    if not parsed_data:
        print("No valid news data retrieved. Exiting.")
        return
    
    df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])
    
    vader = SentimentIntensityAnalyzer()
    df['compound'] = df['title'].apply(lambda title: vader.polarity_scores(title)['compound'])
    
    plt.figure(figsize=(10,8))
    mean_df = df.groupby(['ticker', 'date'])['compound'].mean().unstack()
    mean_df.plot(kind='bar')
    plt.show()

if __name__ == "__main__":
    main()
