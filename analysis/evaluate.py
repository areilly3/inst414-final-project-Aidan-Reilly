# Move/calculate performance metrics here
# Think about what other metrics would be helpful to see from this model
import os
from sklearn.metrics import classification_report
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def evaluate(metadata_features_test_scaled, y_test, pred_lr, gs_cv):
    """
    Gets evaluation metrics for the model
    Args:
        metadata_features_test_scaled, y_test, pred_lr, gs_cv
    Returns: 
        prints put model accuracy
        Creates 'classification report.csv in data/report
    """
    
    logger.info('Running evaluate function.')
    
    try:
    
        print(f'\nTest Set Performance:')
        print(f'Accuracy: {gs_cv.score(metadata_features_test_scaled, y_test):.4f}')
        
        # Creates classification report and saves it into new dir in data/ 
        os.makedirs('data/report', exist_ok= True)
        report = classification_report(y_test, pred_lr, output_dict= True)
        report_df = pd.DataFrame(report).transpose()
        report_df.to_csv('data/report/classification report.csv')
    
    except Exception as error:
        logger.error(f'Error in evaluate. Error message: {error}')