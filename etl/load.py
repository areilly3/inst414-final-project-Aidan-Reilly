import logging

logger = logging.getLogger(__name__)


def load(metadata, ling):
    
    logger.info('Running load function')
    
    try:
        # Saves df's into CSV's for the final time, data is now clean and ready to analyze 
        metadata.to_csv('data/cleaned_metadata.csv')
        ling.to_csv('data/cleaned_ling.csv')
    
    except Exception as error:
        logger.error(f'Error in load. Error message: {error}')