from etl import extract, transform, load
from analysis import model, evaluate
import logging 
from vis import visualizations

logger = logging.getLogger(__name__)

# Set up logger
logging.basicConfig(filename='final_project.log', encoding= 'utf-8', level=logging.INFO)

def main():
    
    try:
        logger.info('Starting pipeline')
        metadata, ling = extract.extract_data()
        metadata, ling = transform.transfrom(metadata, ling)
        load.load(metadata, ling)
        transform.eda(metadata, ling)
        metadata_features_test_scaled, y_test, pred_lr, gs_cv = model.logistic_regression_model()
        evaluate.evaluate( metadata_features_test_scaled, y_test, pred_lr, gs_cv)
        visualizations.popular_words(ling[ling['label'] == 0], ['subject', 'body'])
        visualizations.popular_words(ling[ling['label'] == 1], ['subject', 'body'])
        logger.info('Pipeline complete')
    
    except Exception as error:
        logger.error(f'Error in the pipeline. Error message: {error}')

if __name__ == "__main__":
    main()
    