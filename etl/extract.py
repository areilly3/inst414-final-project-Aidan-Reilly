import pandas as pd
import logging

logger = logging.getLogger(__name__)

# Add logger
def extract_data():
    """
    Extracts data from where it lives and saves it into CSV's
    Args:
        none
    Returns:
        Saves two CSV's to '/data' 
    """
    
    logger.info('Running extract_data function')
    
    try:
        # Pull data in from dropbox
        metadata = pd.read_csv('https://www.dropbox.com/scl/fi/gsyka7j3nfx7n1dp2p5vt/Dataset.csv?rlkey=k1vx2li5rfvos869yv401tp1e&st=txjidhnc&dl=1', sep= ',')
        ling = pd.read_csv('https://www.dropbox.com/scl/fi/7mj8wzhbee0utrtbm5d0g/Ling.csv?rlkey=po6or9qp6a4skclh092f31fl0&st=wxl2mlqu&dl=1')

        # Saves df's to CSV's in /data
        metadata.to_csv('data/metadata.csv')
        ling.to_csv('data/ling.csv')

        return (metadata, ling)
    
    except Exception as error:
        logger.error(f'Error in extract. Error message: {error}')