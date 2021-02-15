import psycopg2

db = psycopg2.connect(user = "TarikId1218",
                      password = "Sanane1218*",
                      host = "tarikdatabase1218.postgres.database.azure.com",
                      port = "5432",
                      database = "postgres")

imlec = db.cursor()
psycopg2.connect()
print( db.get_dsn_parameters() )

