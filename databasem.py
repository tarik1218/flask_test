import psycopg2

db = psycopg2.connect(user = "TarikId1218", password = "Sanane1218*", host = "tarikdatabase1218.postgres.database.azure.com",dbname = "postgres", sslmode="require")

imlec = db.cursor()

#print( db.get_dsn_parameters() )

