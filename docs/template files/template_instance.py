#################
#####IMPORTS#####
#################

#Import Modules
from os import getenv
from sqlalchemy import types

#Custom Modules
import csv_collate as collate


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

### MODIFY THE FOLLOWING ###
#Columns in the output csv and SQL table
output_columns = [ 
]

#(Optional) Specify datatypes for SQL. 
#Might raise exception if specified data types does not match existing table.
#May need to DROP existing table first

#Example specifying columns as Dates or Date Time objects
'''
output_dtypes = {
    "date_processed" : types.Date,
    "date_data" : types.Datetime,
}
'''
output_dtypes = {
}

#(Optional) Specify the format of date type columns

#Example
'''
output_dateformats = {
    "date_processed":"%Y-%m-%d",
    "date_data":"%d/%m/%YT%H:%M:%S"
}
'''
output_dateformats = {
}

#Map the loose files to mapping_columns (Remove ".csv" from the file name)
mapping_groups = {
}

#Groups of maps stating how to map the columns in the loose files to the desired output columns
mapping_columns = {
    "base":[]
}

### END MODIFICATIONS ###

#Parameter objects
output = {
    "columns": output_columns,
    "dtypes": output_dtypes,
    "dateformats": output_dateformats
}

mapping = {
    "groups": mapping_groups,
    "columns": mapping_columns 
}

#Main function call
collate.main(output, mapping, settings)