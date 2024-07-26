This project is a Python-based application that performs sentiment analysis on financial news articles related to specified stock tickers. The goal is to analyse the sentiment of these news articles to gain insights into market sentiment for various stocks, which can be valuable for investors and traders.

Key Features:
User Input for Tickers: Users can input any stock ticker symbols they are interested in. The application fetches the latest news articles for these tickers from a financial news website.

Web Scraping with BeautifulSoup: The project utilises the BeautifulSoup library for parsing HTML content. It scrapes news headlines and associated metadata (such as dates and times) from Finviz, a popular financial information website.

Sentiment Analysis with NLTK VADER: The project employs the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool from the NLTK library. VADER is specifically designed for sentiment analysis of social media texts and works well on financial news as well. It provides a compound score that indicates the overall sentiment of each news headline.

Data Handling and Visualization with Pandas and Matplotlib: The collected data, including ticker symbols, dates, times, and sentiment scores, are organised into a Pandas DataFrame for easy manipulation and analysis. The project uses Matplotlib to create bar charts, visually representing the average sentiment score for each ticker over time.

Robust Error Handling: The project includes error handling mechanisms to manage issues such as invalid ticker symbols, network errors, or parsing failures, ensuring a smooth user experience.
Frameworks and Libraries Used:

Pandas: For data manipulation and analysis, organising the scraped data into structured formats.

BeautifulSoup: For web scraping, extracting news headlines and metadata from HTML pages.

NLTK (Natural Language Toolkit): Specifically, the VADER sentiment analyser, used for calculating sentiment polarity scores from text data.

Matplotlib: For data visualisation, creating charts that help in understanding the sentiment trends for different stock tickers.

This project demonstrates how to combine web scraping, natural language processing, and data visualisation to extract meaningful insights from financial news data. 
