# model fitness measure: model_metrics/fitness_diy_measure.py

import scipy.stats
from math import sqrt
import numpy as np

class FitnessDIYMeasure():
    """
    
    ----
    functions: 
    
    """
    def __init__(self, observed, estimated):
        
        # Initialize any necessary variables or attributes here
        self.observed = observed
        self.estimated = estimated

    # R squared:
    def calc_rsquared(self):
        """
        Calculate the r^2 from a series of observed and estimated target values
        inputs:
        Observed: Series of actual observed values
        estimated: Series of predicted values
        """
            
        r, p = scipy.stats.pearsonr(self.observed, self.estimated)
        R2 = r **2  
        return R2

    # Mean Squared Error:
    def calc_mse(self):
        """
        Calculate Mean Squared Error between a series of observed and estimated values
        
        inputs:
        Observed: Series of actual observed values
        estimated: Series of predicted values
        """
            
        res = (self.observed -self.estimated)**2
        MSE = round(res.mean(), 3)
            
        return MSE

    # Root Mean Square Error:
    def calc_rmse(self):
        """
        Calculate Root Mean Square Error between a series of observed and estimated values
        
        inputs:
        Observed: Series of actual observed values
        estimated: Series of predicted values
        """
            
        res = (self.observed -self.estimated)**2
        RMSE = round(sqrt(res.mean()), 3)
            
        return RMSE
    
   # Root Mean Square Error:
    def calc_mae(self):
        """
        Calculate Root Mean Square Error between a series of observed and estimated values
        
        inputs:
        Observed: Series of actual observed values
        estimated: Series of predicted values
        """
            
        res = abs(self.observed -self.estimated)
        mae = round(res.mean(), 3)
            
        return mae
    
    def calc_msle(self):
        """
        Calculate Mean Squared Logarithmic Error between a series of observed and estimated values.
        
        inputs:
        Observed: Series of actual observed values
        estimated: Series of predicted values
        
        Note: Both observed and estimated values must be positive and non-zero.
        """
        
        # Adding 1 to both observed and estimated values to avoid log(0) 
        # since log(0) is undefined
        log_observed = np.log(self.observed + 1)
        log_estimated = np.log(self.estimated + 1)
        
        # Compute the squared log differences
        squared_log_errors = (log_observed - log_estimated) ** 2
        
        # Compute the mean of these squared log differences
        msle = np.mean(squared_log_errors)
        
        return msle

    def calc_mape(self):
        """
        Calculate Mean Absolute Percentage Error between a series of observed and estimated values.
        
        inputs:
        Observed: Series of actual observed values
        estimated: Series of predicted values
        
        Note: Both observed and estimated values must be positive and non-zero.
        """
        
        # Compute the absolute percentage error
        absolute_percentage_errors = np.abs((self.observed - self.estimated) / self.observed)
        
        # Compute the mean of these absolute percentage errors
        mape = np.mean(absolute_percentage_errors)
        
        return mape
  
        

