from pymongo import MongoClient

uri = "mongodb+srv://aisyahhh051004_db_user:Aisyah051004@bigdatacluster.swzz2p3.mongodb.net/?appName=BigDataCluster"

try:
    client = MongoClient(uri)
    print("Koneksi berhasil!")
    print("Daftar Database:", client.list_database_names())
except Exception as e:
    print("Koneksi gagal:", e)