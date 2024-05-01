import newspaper
import pandas as pd
from newspaper import Config

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'

config = Config()
config.browser_user_agent = USER_AGENT

base_url = 'https://www.merkur.de/wirtschaft/'
article_urls = set()

paper = newspaper.build(base_url, config=config, memoize_articles=False, language='de')

# Create an empty list to store data
data = []
relevant_keywords = ['aktie', 'investition', 'volkwirtschaft', 'bank', 'kredit', 'hauskauf', 'monat', 'zins', 
                     'monatliche', 'aspekte', 'laufzeit', 'immobilie', 'finanzierung', 'geldanlage', 'börse', 
                     'rendite', 'dividende', 'finanzmarkt', 'sparplan', 'versicherung', 'anlagestrategie', 
                     'kapitalanlage', 'kreditkarte', 'kreditzinsen', 'sparbuch', 'kreditvergleich', 
                     'kreditnehmer', 'kreditvergabe', 'kreditwürdigkeit', 'finanzamt', 'finanzberatung', 
                     'geldpolitik', 'steuererklärung', 'steuern', 'wirtschaftswachstum', 'inflation', 'deflation', 
                     'konjunktur', 'schulden', 'schuldner', 'aktienmarkt', 'anleihen', 'finanzkrise', 
                     'wirtschaftskrise', 'liquidität', 'bonität', 'wertpapiere', 'vermögenswerte', 
                     'risikomanagement', 'börsenmakler', 'börsenindex', 'investmentfonds', 'geldmarkt', 
                     'staatsanleihen', 'privatkredit', 'unternehmenskredit', 'hypothek', 'schuldenabbau', 
                     'einkommensteuer', 'erbschaftsteuer', 'grunderwerbsteuer', 'umsatzsteuer', 'vermögenssteuer', 'etf']

for article in paper.articles:
    article.download()
    article.parse()
    article.nlp()

    # Check if the article title contains any of the relevant keywords
    title_contains_keyword = any(keyword in article.title.lower() for keyword in relevant_keywords)

    # If the title contains at least one keyword, add it to the data list
    if title_contains_keyword:
        new_row = {'title': article.title}
        data.append(new_row)

# Create DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Remove duplicate titles
df.drop_duplicates(inplace=True)

# Save DataFrame to Excel file
df.to_excel('/Users/lenaschill/Desktop/merkur_article_data.xlsx', index=False)
