import pickle
import os

import numpy  as np
import pandas as pd

class HealthInsurance:
    
    def __init__( self ):
        self.home_path = os.path.abspath('')
        self.annual_premium_scaler            = pickle.load( open( os.path.join(self.home_path, 'features/annual_premium_scaler.pkl'), 'rb' ) )
        self.age_scaler                       = pickle.load( open( os.path.join(self.home_path, 'features/age_scaler.pkl'), 'rb' ) )
        self.vintage_scaler                   = pickle.load( open( os.path.join(self.home_path, 'features/vintage_scaler.pkl'), 'rb' ) )
        self.target_encode_gender_scaler      = pickle.load( open( os.path.join(self.home_path, 'features/target_encode_gender_scaler.pkl'), 'rb' ) )
        self.target_encode_region_code_scaler = pickle.load( open( os.path.join(self.home_path, 'features/target_encode_region_code_scaler.pkl'), 'rb' ) )
        self.freq_policy_sales_channel_scaler = pickle.load( open( os.path.join(self.home_path, 'features/freq_policy_sales_channel_scaler.pkl'), 'rb' ) )
        
        
    def data_cleaning( self, df2 ):
        ## 2.1. Renaming Columns
        # to lower case
        cols_new = df2.columns.str.lower()

        # rename columns
        df2.columns = cols_new
        df2.columns
        
        return df2
    
    
    def feature_engineering( self, df3 ):
        # vehicle age
        df3['vehicle_age'] = df3['vehicle_age'].apply( lambda x: 'over_2_years'      if x == '> 2 Years' else
                                                                 'between_1_2_years' if x == '1-2 Year' else 
                                                                 'below_1_year' )
        # vehicle damage
        df3['vehicle_damage'] = df3['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)
        
        return df3
    
    
    def data_preparation( self, df6 ):
        # annual_premium
        df6['annual_premium'] = self.annual_premium_scaler.fit_transform( df6[['annual_premium']].values )

        # age
        df6['age'] = self.age_scaler.fit_transform( df6[['age']].values )

        # vintage
        df6['vintage'] = self.vintage_scaler.fit_transform( df6[['vintage']].values )
        
        # gender 
        df6['gender'] = df6['gender'].map( self.target_encode_gender_scaler )

        # region code
        df6['region_code'] = df6['region_code'].map( self.target_encode_region_code_scaler )

        # vehicle_age
        df6 = pd.get_dummies( df6, prefix='vehicle_age', columns=['vehicle_age'] )

        if 'vehicle_age_below_1_year' not in df6.columns:
            df6['vehicle_age_below_1_year'] = 0
        if 'vehicle_age_between_1_2_years' not in df6.columns:
            df6['vehicle_age_between_1_2_years'] = 0
        if 'vehicle_age_over_2_years' not in df6.columns:
            df6['vehicle_age_over_2_years'] = 0

        # policy_sales_channel
        df6['policy_sales_channel'] = df6['policy_sales_channel'].map( self.freq_policy_sales_channel_scaler )
        
        # feature selection
        cols_selected = ['annual_premium', 'vintage', 'age', 'region_code', 
                        'vehicle_damage', 'previously_insured', 'policy_sales_channel', 
                        'vehicle_age_below_1_year', 'vehicle_age_between_1_2_years', 'vehicle_age_over_2_years']
        
        return df6[ cols_selected ]
    
    
    def get_predict( self, model, original_data, test_data ):
        # model prediction
        pred = model.predict_proba( test_data )

        # join prediction into original data
        original_data['score'] = pred[:, 1].tolist()
        
        return original_data.to_json( orient='records', date_format='iso' )