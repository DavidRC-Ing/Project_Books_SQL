import pandas as pd
from sqlalchemy import create_engine


db_config = {
            'user': 'practicum_student', # username
 'pwd': 'QnmDH8Sc2TQLvy2G3Vvh7', # password
 'host': 'yp-trainers-practicum.cluster-czs0gxyx2d8w.us-east-1.rds.amazonaws.com',
 'port': 5432, # connection port
 'db': 'data-analyst-final-project-db' # the name of the database
 }
connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_c
onfig['user'],

db_config['pwd'],

db_config['host'],
db_config['port'],

db_config['db'])