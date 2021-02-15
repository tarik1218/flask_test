import psycopg2

db = psycopg2.connect(user = "TarikId1218", password = "Sanane1218*", host = "finaldata.postgres.database.azure.com",port="5432",dbname = "postgres", sslmode="require")

imlec = db.cursor()
#psycopg2.connect()
#print( db.get_dsn_parameters() )

