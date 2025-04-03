
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://abimanyuganesan2000:Admin1234@test-cluster.dvkbqro.mongodb.net/?retryWrites=true&w=majority&appName=test-cluster"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    print("\n📌 Available Databases:")
    databases = client.list_database_names()
    for db in databases:
        print(f"  - {db}")

    # print(f"\n📌 Collections in '{db_name}' database:")
    # collections = db.list_collection_names()
    # for collection in collections:
    #     print(f"  - {collection}")
except Exception as e:
    print(e)
