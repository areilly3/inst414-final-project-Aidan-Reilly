import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Functions will be called in main with metadata argument, but for now this works. Eventually take this line out 
metadata = pd.read_csv('data/metadata.csv')

def countplots():
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

def scatterplot():
    """
    Creates scatterplot for type of email and number of special characters it has in the url
    Args:
        none
    Returns:
        Scatter plot
    """
    
    sns.scatterplot(x='Type', y='number_of_special_char_in_url', data= metadata)
    plt.show()

def boxplot():
    """
    Creates boxplot for email type and number of special characters in the url
    Args:
        none
    Returns:
        Box plot
    """
    
    sns.boxplot(x='Type', y='number_of_special_char_in_url', data= metadata)
    plt.show()

def histogram():
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

# Function calls 
countplots()
boxplot()
histogram()