import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
import logging
from collections import Counter
from wordcloud import WordCloud

logger = logging.getLogger(__name__)

def countplots(metadata):
    """
    Creates countplots for email type and whether or not an email has special characters or digits in subdomain
    Args:
        none
    Returns:
        Count plot
    """
    
    sns.countplot(x='Type', hue='having_special_characters_in_domain', data= metadata)
    plt.show()
    
    sns.countplot(x='Type', hue= 'having_digits_in_subdomain', data= metadata)
    plt.show()
    
def boxplot(metadata):
    """
    Creates boxplot for email type and number of special characters in the url
    Args:
        none
    Returns:
        Box plot
    """
    
    sns.boxplot(x='Type', y='number_of_special_char_in_url', data= metadata)
    plt.show()

def histogram(metadata):
    """
    Creates histogram for entropy of url and entropy of domain
    Args:
        none
    Returns:
        Two histograms
    """
    
    sns.histplot(data=metadata, x='entropy_of_url', hue='Type')
    plt.show()
    
    sns.histplot(data=metadata, x='entropy_of_domain', hue='Type')
    plt.show()
    
def popular_words(dataframe, text_cols):
    """
    Finds the five most popular words in a type of email. Excludes common words listed in the 'stopwords' set
    Args:
        dataframe: df that will be used
        text_cols: Columns in df to analyze. 'subject' and 'body'
    Returns:
        The five most popular words in the email type
    """
    
    logger.info('Running popular_words function')
    
    try:
        
        # These are common words that are filtered out
        stopwords = {
        "the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as",
        "with","his","they","i","at","be","this","have","from","or","one","had","by","word","but",
        "not","what","all","were","we","when","your","can","said","there","use","each","which",
        "she","do","how","their","if","will", "s", "an", "e", "de", "t", "our", "out", "my", "get",
        "no", "more", "should", "people"}
        
        # Joins the 'subject' and 'body' strings into one string
        dataframe = dataframe.copy() 
        dataframe["full_text"] = dataframe[text_cols].astype(str).agg(" ".join, axis=1)
        all_text = " ".join(dataframe["full_text"]).lower()
        
        # Finds all words in all_text, filters out common words to make list
        words = re.findall(r"\b[a-z]+\b", all_text)
        filtered_words = [word for word in words if word not in stopwords]

        popular_words = Counter(filtered_words)

        # Creates a wordcloud with popular_words, max word count of 10
        wc = WordCloud(width=800, height=400,
                    background_color="white",
                    max_words = 10,
                    colormap="viridis").generate_from_frequencies(popular_words)
        
        # Plots wordcloud
        plt.figure(figsize=(8, 4))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.show()
    
    except Exception as error:
        logger.error(f'Error in visualizations. Error message: {error}')
    

