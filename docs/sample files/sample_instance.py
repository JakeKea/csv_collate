#################
#####IMPORTS#####
#################

#Import Modules
from os import getenv
from sqlalchemy import types

#Custom Modules
import ncl_collate as collate


#Import env
from dotenv import load_dotenv
import json

########################
#####.env VARIABLES#####
########################

#load the env file
load_dotenv(override=True)

#Settings object
#Use json.loads(getenv("ENV_VAR_NAME").lower()) to parse bools (yes it's dumb)
settings = {
    #Run settings
    "METHOD": getenv("METHOD"),

    #SQL settings
    "SQL_UPLOAD": getenv("SQL_UPLOAD"),
    "SQL_REPLACE": json.loads(getenv("SQL_REPLACE").lower()),
    "SQL_DATABASE": getenv("SQL_DATABASE"),
    "SQL_SCHEMA": getenv("SQL_SCHEMA"),
    "SQL_TABLE": getenv("SQL_TABLE"),
    "SQL_CHUNKSIZE": int(getenv("SQL_CHUNKSIZE")),
    "SQL_DTYPES": json.loads(getenv("SQL_DTYPES").lower()),
    "SQL_ADDRESS": getenv("SQL_ADDRESS"),

    #Data settings
    "PATH_PREFIX": getenv("PATH_PREFIX"),
    "DEFAULT_MAP": getenv("DEFAULT_MAP"),
    "LABEL_DATA": getenv("LABEL_DATA"),
}

##########################################
##### MAPPING AND OUTPUT DEFINITIONS #####
##########################################

#Columns in the output csv and SQL table
output_columns = [
    "date",
    "region_code",
    "region_name",
    "icb_code",
    "icb_name",
    "org_code",
    "org_name",
    "sickness_cluster_group",
    "sickness_benchmark_group",
    "staff_group",
    "days_lost",
    "days_available"    
]

#(Optional) Specify datatypes for SQL. 
#Might raise exception if specified data types does not match existing table.
#May need to DROP existing table first
output_dtypes = {
    "date" : types.Date
}

#Map the loose files to mapping_columns (Remove ".csv" from the file name)
mapping_groups = {
    "2022_08":["2022_08", "2022_09", "2022_10", "2022_11", "2022_12", "2023_1", "2023_2", "2023_03"],
    "2022_04":["2022_04", "2022_05", "2022_06", "2022_07"],
    "base":["archive 2018_04 - 2022_03"]
}

#Groups of maps stating how to map the columns in the loose files to the desired output columns
mapping_columns = {
    "2022_08":{
        "DATE":"date",
        "NHSE_REGION_CODE":"region_code",
        "NHSE_REGION_NAME":"region_name",
        "ICS_CODE":"icb_code",
        "ICS_NAME":"icb_name",
        "ORG_CODE":"org_code",
        "ORG_NAME":"org_name",
        "CLUSTER_GROUP":"sickness_cluster_group",
        "BENCHMARK_GROUP":"sickness_benchmark_group",
        "STAFF_GROUP":"staff_group",
        "FTE_DAYS_LOST":"days_lost",
        "FTE_DAYS_AVAILABLE":"days_available",
        "SICKNESS_ABSENCE_RATE_PERCENT":None
    },
    "2022_04":{
        "DATE":"date",
        "NHSE_REGION_CODE":"region_code",
        "NHSE_REGION_NAME":"region_name",
        "ORG_CODE":"org_code",
        "ORG_NAME":"org_name",
        "CLUSTER_GROUP":"sickness_cluster_group",
        "BENCHMARK_GROUP":"sickness_benchmark_group",
        "STAFF_GROUP":"staff_group",
        "FTE_DAYS_LOST":"days_lost",
        "FTE_DAYS_AVAILABLE":"days_available",
        "SICKNESS_ABSENCE_RATE_PERCENT":None
    },
    "base":{
        "Month":None,
        "Tm End Date":"date",
        "Org code":"org_code",
        "Org name":"org_name",
        "Cluster group":"sickness_cluster_group",
        "Benchmark group":"sickness_benchmark_group",
        "NHSE region code":"region_code",
        "NHSE region name":"region_name",
        "Staff group":"staff_group",
        "FTE days lost":"days_lost",
        "FTE days available":"days_available",
        "Sickness absence rate (%)":None
    }
}

#Parameter objects
output = {
    "columns": output_columns,
    "dtypes": output_dtypes
}

mapping = {
    "groups": mapping_groups,
    "columns": mapping_columns 
}

#Main function call
collate.main(output, mapping, settings)