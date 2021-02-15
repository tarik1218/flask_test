import psycopg2

db = psycopg2.connect(host = "tarikdatabase1218.postgres.database.azure.com",dbname = "postgres",user = "TarikId1218",password = "Sanane1218*", ssl="disable" )

imlec = db.cursor()
psycopg2.connect()
print( db.get_dsn_parameters() )

