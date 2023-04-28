## MODULE WITH GENERAL PARAMETERS FOR THE PROJECT





"----------------------------------------------------------------------------------------------------------------------"
############################################# Imports ##################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--- Standard library imports ---"


"--- Third party imports ---"


"--- Local application imports ---"





"----------------------------------------------------------------------------------------------------------------------"
############### Data schema ############################################################################################
"----------------------------------------------------------------------------------------------------------------------"


## Data schema to handle data
proy_base_data_schema = {

  "index": {
    "relevant": False,
    "clean_col_name": "index",
    "data_type": "int",
    "value_map": {},
    "feature_type": "numeric",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "FID": {
    "relevant": True,
    "clean_col_name": "FID",
    "data_type": "int",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "id_feature": True,
  },
  "ADDRESBR": {
    "relevant": False,
    "clean_col_name": "ADDRESBR",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "BRNUM": {
    "relevant": True,
    "clean_col_name": "BRNUM",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": True,
    "imputation_strategy": "most_frequent"
  },
  "BRSERTYP": {
    "relevant": True,
    "clean_col_name": "BRSERTYP",
    "data_type": "int",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": True,
    "imputation_strategy": "most_frequent"
  },
  "CBSABR": {
    "relevant": True,
    "clean_col_name": "CBSABR",
    "data_type": "int",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": True,
    "imputation_strategy": "most_frequent"
  },
  "CBSANAMB": {
    "relevant": False,
    "clean_col_name": "CBSANAMB",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "CITYBR": {
    "relevant": False,
    "clean_col_name": "CITYBR",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "CNTRYNAB": {
    "relevant": False,
    "clean_col_name": "CNTRYNAB",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "CNTYNAMB": {
    "relevant": False,
    "clean_col_name": "CNTYNAMB",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "DEPSUMBR": {
    "relevant": True,
    "clean_col_name": "DEPSUMBR",
    "data_type": "int",
    "value_map": {},
    "feature_type": "numeric",
    "model_relevant": True,
    "imputation_strategy": "most_frequent"
  },
  "GEOCODE_CE": {
    "relevant": False,
    "clean_col_name": "GEOCODE_CE",
    "data_type": "int",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "GEOCODE__1": {
    "relevant": False,
    "clean_col_name": "GEOCODE__1",
    "data_type": "int",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "NAMEBR": {
    "relevant": False,
    "clean_col_name": "NAMEBR",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "STALPBR": {
    "relevant": False,
    "clean_col_name": "STALPBR",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "STCNTYBR": {
    "relevant": False,
    "clean_col_name": "STCNTYBR",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "STNAMEBR": {
    "relevant": False,
    "clean_col_name": "STNAMEBR",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "UNINUMBR": {
    "relevant": True,
    "clean_col_name": "UNINUMBR",
    "data_type": "int",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": True,
    "imputation_strategy": "most_frequent"
  },
  "ZIPBR": {
    "relevant": True,
    "clean_col_name": "ZIPBR",
    "data_type": "int",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": True,
    "imputation_strategy": "most_frequent"
  },
  "CERT": {
    "relevant": False,
    "clean_col_name": "CERT",
    "data_type": "int",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "ADDRESS": {
    "relevant": False,
    "clean_col_name": "ADDRESS",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "ASSET": {
    "relevant": True,
    "clean_col_name": "ASSET",
    "data_type": "int",
    "value_map": {},
    "feature_type": "numerical",
    "model_relevant": True,
    "imputation_strategy": "median"
  },
  "BKCLASS": {
    "relevant": False,
    "clean_col_name": "BKCLASS",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "CITY": {
    "relevant": False,
    "clean_col_name": "CITY",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "CNTRYNA": {
    "relevant": False,
    "clean_col_name": "CNTRYNA",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "DENOVO": {
    "relevant": False,
    "clean_col_name": "DENOVO",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "DEPDOM": {
    "relevant": True,
    "clean_col_name": "DEPDOM",
    "data_type": "int",
    "value_map": {},
    "feature_type": "numerical",
    "model_relevant": True,
    "imputation_strategy": "most_frequent"
  },
  "NAMEFULL": {
    "relevant": False,
    "clean_col_name": "NAMEFULL",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "NAMEHCR": {
    "relevant": False,
    "clean_col_name": "NAMEHCR",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "REGAGNT": {
    "relevant": True,
    "clean_col_name": "REGAGNT",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": True,
    "imputation_strategy": "most_frequent"
  },
  "REPDTE": {
    "relevant": False,
    "clean_col_name": "REPDTE",
    "data_type": "datetime",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "RSSDID": {
    "relevant": False,
    "clean_col_name": "RSSDID",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "STALP": {
    "relevant": False,
    "clean_col_name": "STALP",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "STCNTY": {
    "relevant": False,
    "clean_col_name": "STCNTY",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "STNAME": {
    "relevant": False,
    "clean_col_name": "STNAME",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "ZIP": {
    "relevant": False,
    "clean_col_name": "ZIP",
    "data_type": "int",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "BKMO": {
    "relevant": True,
    "clean_col_name": "BKMO",
    "data_type": "int",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": True,
    "imputation_strategy": "most_frequent"
  },
  "LOC_NAME": {
    "relevant": False,
    "clean_col_name": "LOC_NAME",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "STATUS": {
    "relevant": True,
    "clean_col_name": "STATUS",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": True,
    "imputation_strategy": "most_frequent"
  },
  "SCORE": {
    "relevant": False,
    "clean_col_name": "SCORE",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "x": {
    "relevant": False,
    "clean_col_name": "x",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "y": {
    "relevant": False,
    "clean_col_name": "y",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "GeocodeSou": {
    "relevant": False,
    "clean_col_name": "GeocodeSou",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": False,
    "imputation_strategy": "most_frequent"
  },
  "SCORE_T": {
    "relevant": True,
    "clean_col_name": "label",
    "data_type": "boolean",
    "value_map": {
      "False": False,
      "True": True
    },
    "imputation_strategy": "most_frequent",
    "predict_label": True
  },
  "DEP_RATIOS": {
    "relevant": True,
    "clean_col_name": "DEP_RATIOS",
    "data_type": "str",
    "value_map": {},
    "feature_type": "categorical",
    "model_relevant": True,
    "imputation_strategy": "most_frequent"
  }

}



## Data schema to handle data
proy_full_data_schema = proy_base_data_schema



## Parameters for local json containing updated data schema
local_json_path = "pkg_dir/src/parameters/"
json_name = "data_schema"





"----------------------------------------------------------------------------------------------------------------------"
############### XXX ####################################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--------------- XXX ---------------"





"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
############################################# END OF FILE ##############################################################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
