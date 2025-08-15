def load(metadata, ling):
    
    # Saves df's into CSV's for the final time, data is now clean and ready to analyze 
    metadata.to_csv('data/cleaned_metadata.csv')
    ling.to_csv('data/cleaned_ling.csv')