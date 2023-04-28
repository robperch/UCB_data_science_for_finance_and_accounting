## MODULE WITH ML PARAMETERS FOR THE PROJECT





"----------------------------------------------------------------------------------------------------------------------"
############################################# Imports ##################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--- Standard library imports ---"
from functools import partial

"--- Third party imports ---"
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)
from sklearn.ensemble import (

    RandomForestClassifier,
    GradientBoostingClassifier,

)
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

"--- Local application imports ---"






"----------------------------------------------------------------------------------------------------------------------"
############### Scikit-Learn parameters ################################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--------------- Data transformation ---------------"

test_split_size = 0.2
random_state_split = 123



"--------------- Column Transformer pipeline ---------------"

## Categorical pipeline
categorical_ppl = Pipeline(
    [
        ('hotencode', OneHotEncoder())
    ]
)

## Numerical pipeline
numerical_ppl = Pipeline(
    [
        ('std_scaler', StandardScaler())
    ]
)



"--------------- Prediction ML models ---------------"

predict_models_dict = {

    'random_forest': {
        'alias': 'rf',
        'model': RandomForestClassifier(
            max_features='sqrt',
            n_jobs=-1,
            random_state=1111
        ),
        'param_grid': {
            'n_estimators': [50, 75],
#            'min_samples_leaf': [2],
            'max_depth': [100],
            'criterion': ['gini']
        },
        'class_thresh': 0.4,
    },

    'decision_tree': {
        'alias': 'dt',
        'model': DecisionTreeClassifier(
            random_state=2222
        ),
        'param_grid': {
            'max_depth': [100, 150],
            'min_samples_leaf': [2, 3]
#            'min_samples_leaf': [1]
        },
        'class_thresh': 0.35,
    },

#    'gradient_boosting': {
#        'alias': 'xgb',
#        'model': GradientBoostingClassifier(
#            random_state=3333,
#        ),
#        'param_grid': {
#            'max_depth': [100],
#            'learning_rate': [0.1],
#            'n_estimators': [100],
#        },
#        'class_thresh': 0.4,
#    },

    'logistic_regression': {
        'alias': 'lr',
        'model': LogisticRegression(
            random_state=3333,
            max_iter=1000,
        ),
        'param_grid': {
            'class_weight': [None, 'Balanced'],
            'penalty': [None, 'l1', 'l2', 'elasticnet'],
        },
        'class_thresh': 0.4,
    },

}

predict_model_eval_metric = 'accuracy'

positive_label = True



"--------------- Model evaluation metrics ---------------"

model_eval_metrics = {

    'accuracy_score':
        {
            'alias': 'acc',
            'params': 'label/predict',
            'method': partial(metrics.accuracy_score),
        },

    'balanced_accuracy_score':
        {
            'alias': 'bacc',
            'params': 'label/predict',
            'method': partial(metrics.balanced_accuracy_score),
        },

    'average_precision_score':
        {
            'alias': 'avgprec',
            'params': 'label/proba',
            'method': partial(metrics.average_precision_score),
        },

    'brier_score_loss':
        {
            'alias': 'brier',
            'params': 'label/proba',
            'method': partial(metrics.brier_score_loss),
        },

    'f1_score':
        {
            'alias': 'f1',
            'params': 'label/predict',
            'method': partial(metrics.f1_score),
        },

    'precision_score':
        {
            'alias': 'prec',
            'params': 'label/predict',
            'method': partial(metrics.precision_score),
        },

    'recall_score':
        {
            'alias': 'recall',
            'params': 'label/predict',
            'method': partial(metrics.recall_score),
        },

}





"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
############################################# END OF FILE ##############################################################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
