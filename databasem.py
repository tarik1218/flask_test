import psycopg2

db = psycopg2.connect(host = "tarikdatabase1218.postgres.database.azure.com",database = "postgres",user = "TarikId1218",password = "Sanane1218*",ssl="require" )

imlec = db.cursor()
psycopg2.connect()
print( db.get_dsn_parameters() )

