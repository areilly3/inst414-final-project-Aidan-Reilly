import pandas as pd

def extract():
    """
    Extracts data from where it lives and puts it into dataframes
    Args:
        none
    Returns:
        Dataframes
    """
    
    metadata = pd.read_csv('https://www.dropbox.com/scl/fi/gsyka7j3nfx7n1dp2p5vt/Dataset.csv?rlkey=k1vx2li5rfvos869yv401tp1e&st=txjidhnc&dl=1', sep= ',')
    
    # Having trouble with this dataset
    # raw_data = pd.read_csv('https://www.dropbox.com/scl/fi/3f5c9g4y8jxspulxlpurb/TREC_06.csv?rlkey=kja3sh1yjb23bkl8owfsd1jhr&st=7md0peq7&dl=1', sep= ',')
    
    metadata.to_csv('data/metadata.csv')
    # raw_data.to_csv('data/raw_data.csv')
    

extract()