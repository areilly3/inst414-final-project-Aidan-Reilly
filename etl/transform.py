import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def transfrom():
    """
    Clean data so that it is tidy and can be worked with
    Args:
        dataframes
    Returns:
        cleaned dataframes
    """
    metadata = pd.read_csv('data/metadata.csv')
    # raw_data = pd.read_csv('data/raw_data.csv')

    # Drop rows with missing data, save new df to /data
    # cleaned_raw_data = raw_data.dropna()
    # cleaned_raw_data.to_csv('data/cleaned_raw_data.csv')

def eda():
    """
    Exploring data with graphs to understand it better
    Args:
        none
    Returns:
        none
    """
    
    metadata = pd.read_csv('data/metadata.csv')
    # cleaned_raw_data = pd.read_csv('data/cleaned_raw_data.csv')
    
    print(metadata.head())
    
    # Boxplot that shows relationship between type of email and the url length
    sns.boxplot(x= 'Type', y= 'url_length', data= metadata)
    plt.show()
    
    # Scatterplot that show relationship between type of email and the number of special characters in url 
    sns.scatterplot(x= 'Type', y= 'number_of_special_char_in_url', data= metadata)
    plt.show()
    
eda()