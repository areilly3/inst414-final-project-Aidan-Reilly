import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import StratifiedKFold as KFold_strat
from sklearn.linear_model import LogisticRegression as lr
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import os
import logging

logger = logging.getLogger(__name__)

def logistic_regression_model():
    """
    Runs a logistic regression model to classify emails as phishing or safe
    Args:   
        none
    Returns:
        Saves report into directory data/report 
    """
    
    logger.info('Running logistic_regression_model function')
    
    try:
        metadata = pd.read_csv('data/cleaned_metadata.csv')
        
        # Splits training and testing data
        metadata_train, metadata_test = train_test_split(metadata, test_size= 0.3, shuffle= True, stratify= metadata['Type'])
        
        features = ['entropy_of_url' ,'entropy_of_domain' ,'url_length' ,'yes_no_total', 'number_of_special_char_in_url', 'average_subdomain_length', 'number_of_digits_in_domain']
        
        # Scaling training features due to wide disparity between the features 
        scaler = StandardScaler()
        features_train = metadata_train[features]
        features_train_scaled = scaler.fit_transform(features_train)
        y_train = metadata_train['Type']
        
        # Create paramater grid
        param_grid = {'C': [0.1, 1, 10]}
        lr_model = lr()
        
        gs_cv = GridSearchCV(estimator= lr_model, param_grid= param_grid, cv= 5)
        gs_cv.fit(features_train_scaled, y_train)
        
        # Scaling test features
        metadata_features_test = metadata_test[features]
        metadata_features_test_scaled = scaler.transform(metadata_features_test)
        
        # Creates pred_lr (prediction) column 
        pred_lr = gs_cv.predict(metadata_features_test_scaled)
        metadata_test['pred_lr'] = pred_lr
        
        y_test = metadata_test['Type']
        
        return metadata_features_test_scaled, y_test, pred_lr, gs_cv
    
    except Exception as error:
        logger.error(f'Error in the model. Error message: {error}')