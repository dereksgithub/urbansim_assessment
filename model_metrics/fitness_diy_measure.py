# model fitness measure: model_metrics/fitness_diy_measure.py

import scipy.stats
from math import sqrt

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
