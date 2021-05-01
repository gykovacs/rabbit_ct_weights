import pandas as pd

from sklearn.model_selection import RepeatedKFold
from sklearn.metrics import r2_score
from maweight.mltoolkit.automl import R2_score, RMSE_score
from maweight.mltoolkit.optimization import SimulatedAnnealing, UniformIntegerParameter, ParameterSpace, BinaryVectorParameter
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import RepeatedKFold

from maweight.mltoolkit.automl import *

random_state= 11

def model_selection(features, 
            target, 
            objectives=[KNNR_Objective, 
                        LinearRegression_Objective, 
                        LassoRegression_Objective,
                        RidgeRegression_Objective,
                        PLSRegression_Objective],
            dataset=None,
            type=None):
    all_results= []

    for o in objectives:
        print("Objective {}:".format(o.__name__))
        results={}
        ms= ModelSelection(o, 
                            features.values, 
                            target.values, 
                            verbosity=0, 
                            score_functions=[NegR2_score()], 
                            preprocessor=StandardScaler(), 
                            optimizer=SimulatedAnnealing(verbosity=0,
                                                            random_state=random_state),
                            random_state=random_state)
        results['model_selection_score']= ms.select()['score']
        results['features']= list(features.columns[ms.get_best_model()["features"]])
        results['parameters']= ms.get_best_model()['model'].regressor.get_params()
        results['model']= o.__name__

        best = ms.get_best_model()
        used_features=[features.columns[i] for i, x in enumerate(best["features"]) if x]
        
        print("Number of used features: {}\nUsed features: {} \nScore: {}".format(len(used_features), used_features, best["score"]))
        for i in [1]:
            tmp= ms.evaluate(n_estimators=i, score_functions=[R2_score(), RMSE_score()], validator= RepeatedKFold(n_splits=10, n_repeats=20, random_state=21))
            results['r2_' + str(i)]= tmp['scores'][0]
            results['rmse_' + str(i)]= tmp['scores'][1]
            results['y_test_' + str(i)]= tmp['y_test']
            results['y_pred_' + str(i)]= tmp['y_pred']
            results['y_indices_' + str(i)]= str(tmp['y_indices'])
            print(i, results['r2_' + str(i)])
        results['dataset']= dataset
        results['type']= type
        
        all_results.append(results)
    
    return pd.DataFrame(all_results)
