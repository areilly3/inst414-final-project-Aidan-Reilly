"""
Import packages from other directories to run code
"""
from etl import extract, transform, load
from analysis import model
import logging 

logger = logging.getLogger(__name__)

def main():
    
    # Set up logger
    logging.basicConfig(filename='final_project.log', encoding= 'utf-8', level=logging.INFO)
    
    try:
        logger.info('Starting pipeline')
        metadata, ling = extract.extract_data()
        metadata, ling = transform.transfrom(metadata, ling)
        transform.eda(metadata, ling)
        load.load(metadata, ling)
        model.logistic_regression_model()
        logger.info('Pipeline complete')
    
    except Exception as error:
        logger.error(f'Error in the pipeline. Error message: {error}')

if __name__ == "__main__":
    main()
    