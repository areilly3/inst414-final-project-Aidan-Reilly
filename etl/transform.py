import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
import re

# Add logger
def transfrom(metadata, ling):
    """
    Clean data so that it is tidy and can be worked with
    Args:
        dataframes
    Returns:
        cleaned dataframes
    """

    # Checks for missing data
    missing_metadata = metadata.isnull().sum()
    missing_ling = ling.isnull().sum()
    
    # Ling is missing 62 subjects. This data will be kept unchanged because it could reveal insight into when emails don't have a subject line.
    
    # Creates column that combines url_length and domain_length
    metadata_totals_column_names = ['url_length', 'domain_length']
    metadata['totals'] = metadata[metadata_totals_column_names].sum(axis=1)
    
    # Creates two new columns that count the length of subject and body 
    ling['subject_len'] = ling['subject'].str.len()
    ling['body_len'] = ling['body'].str.len()
    
    meteadata_yes_no_column_names = ['having_repeated_digits_in_url', 'having_special_characters_in_domain', 'having_digits_in_domain', 'having_repeated_digits_in_domain', 'having_dot_in_subdomain', 'having_hyphen_in_subdomain', 'having_special_characters_in_subdomain', 'having_digits_in_subdomain', 'having_repeated_digits_in_subdomain', 'having_path', 'having_query', 'having_fragment', 'having_anchor']
    metadata['yes_no_total'] = metadata[meteadata_yes_no_column_names].sum(axis=1)
    
    return metadata, ling
    

def eda(metadata, ling):
    """
    Exploring data with graphs to understand it better
    Args:
        none
    Returns:
        none
    """     
    # Lots of different simple visualizations to help with exploring data, commented out to speed up the program
    
    # metadata = pd.read_csv('data/metadata.csv')
    # # cleaned_raw_data = pd.read_csv('data/cleaned_raw_data.csv')
    
    # print(metadata.head())
    
    # # Boxplot that shows relationship between type of email and the url length
    # sns.boxplot(x= 'Type', y= 'url_length', data= metadata)
    # plt.show()
    
    # # Scatterplot that show relationship between type of email and the number of special characters in url 
    # sns.scatterplot(x= 'Type', y= 'number_of_special_char_in_url', data= metadata)
    # plt.show()

    # Boxplot to show total lengths of different types of emails
    # sns.boxplot(x= 'Type', y= 'totals', data= metadata)
    # plt.show()
    
    # # Boxplot to show subject lengths of different types of emails
    # sns.boxplot(x= 'label', y= 'subject_len', data= ling)
    # plt.show()
    
    # sns.boxplot(x= 'Type', y= 'yes_no_total', data= metadata)
    # plt.show()

# Have not got this working yet. Function to find the most popular words in phishing and safe emails.   
# def popular_words(dataframe, text_cols):
#     """
#     Finds the five most popular words in a type of email. Excludes common words listed in the 'stopwords' set
#     Args:
#         dataframe: df that will be used
#         text_cols: Columns in df to analyze. 'subject' and 'body'
#     Returns:
#         The five most popular words in the email type
#     """
    
#     stopwords = {
#     "the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as",
#     "with","his","they","i","at","be","this","have","from","or","one","had","by","word","but",
#     "not","what","all","were","we","when","your","can","said","there","use","each","which",
#     "she","do","how","their","if","will"}
    
#     dataframe = dataframe.copy() 
#     dataframe["full_text"] = dataframe[text_cols].agg(" ".join, axis=1)
#     all_text = " ".join(dataframe["full_text"]).lower()
#     words = re.findall(r"\b[a-z]+\b", all_text)
#     filtered_words = [word for word in words if word not in stopwords]

#     return Counter(filtered_words).most_common(5)

    