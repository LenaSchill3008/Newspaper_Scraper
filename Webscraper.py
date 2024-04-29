import newspaper
import pandas as pd
from newspaper import Config
from collections import Counter

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'

config = Config()
config.browser_user_agent = USER_AGENT

base_url = 'https://www.tagesschau.de/wirtschaft'
article_urls = set()

paper = newspaper.build(base_url, config=config, memoize_articles=False, language='de')

# Create an empty list to store data
data = []

for article in paper.articles:
    article.download()
    article.parse()
    article.nlp()

    # Define the data for the new row as a dictionary
    new_row = {'title': article.title, 'keywords': ', '.join(article.keywords)}

    # Append the new row to the list
    data.append(new_row)

# Create DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Save DataFrame to Excel file
df.to_excel('/Users/lenaschill/Desktop/darticle_data.xlsx', index=False)
