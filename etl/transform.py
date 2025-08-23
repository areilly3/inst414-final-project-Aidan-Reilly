import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
import re
import logging

logger = logging.getLogger(__name__)

# Add logger
def transfrom(metadata, ling):
    """
    Clean data so that it is tidy and can be worked with
    Args:
        dataframes
    Returns:
        cleaned dataframes
    """
    
    logger.info('Running transform function')
    
    try:
        # Checks for missing data
        missing_metadata = metadata.isnull().sum()
        missing_ling = ling.isnull().sum()
        
        # Ling is missing 62 values in the subject column. This data will be kept unchanged because it could reveal insight into when emails don't have a subject line.
        
        # Creates column that combines url_length and domain_length
        metadata_totals_column_names = ['url_length', 'domain_length']
        metadata['totals'] = metadata[metadata_totals_column_names].sum(axis=1)
        
        # Creates two new columns that count the length of subject and body 
        ling['subject_len'] = ling['subject'].str.len()
        ling['body_len'] = ling['body'].str.len()
        
        meteadata_yes_no_column_names = ['having_repeated_digits_in_url', 'having_special_characters_in_domain', 'having_digits_in_domain', 'having_repeated_digits_in_domain', 'having_dot_in_subdomain', 'having_hyphen_in_subdomain', 'having_special_characters_in_subdomain', 'having_digits_in_subdomain', 'having_repeated_digits_in_subdomain', 'having_path', 'having_query', 'having_fragment', 'having_anchor']
        metadata['yes_no_total'] = metadata[meteadata_yes_no_column_names].sum(axis=1)
        
        return metadata, ling
        
    except Exception as error:
        logger.error(f'Error in transform. Error message: {error}')
        

def eda(metadata, ling):
    """
    Exploring data with graphs to understand it better
    Args:
        dataframes
    Returns:
        produces several charts
    """    
    
    logger.info('Running eda function')
    
    try:
        # Lots of different simple visualizations to help with exploring data, commented out to speed up the program
        
        metadata = pd.read_csv('data/cleaned_metadata.csv')
        cleaned_raw_data = pd.read_csv('data/cleaned_ling.csv')
        
        # # Boxplot that shows relationship between type of email and the url length
        sns.boxplot(x= 'Type', y= 'url_length', data= metadata)
        plt.show()
        
        # # Scatterplot that show relationship between type of email and the number of qualities that email has 
        sns.boxplot(x= 'Type', y= 'yes_no_total', data= metadata)
        plt.show()

        # Boxplot to show total length of url and domain lengths combined of different types of emails
        totals_graph = sns.boxplot(x= 'Type', y= 'totals', data= metadata)
        totals_graph.set_ylabel('Total lengths of URLs and domains')
        plt.show()
    
    except Exception as error:
        logger.error(f'Error in eda. Error message: {error}')
    