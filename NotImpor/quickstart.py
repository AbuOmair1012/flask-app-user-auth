from pymongo import MongoClient
uri = "mongodb+srv://abdo:eIjs3QqGNVs6f2DB@db-flask-app.t6gyb.mongodb.net/?retryWrites=true&w=majority&appName=db-flask-app"
client = MongoClient(uri)
# try:
#     database = client.get_database("sample_mflix")
#     movies = database.get_collection("movies")
#     # Query for a movie that has the title 'Back to the Future'
#     query = { "title": "Back to the Future" }
#     movie = movies.find_one(query)
#     print(movie)
#     client.close()
# except Exception as e:
#     raise Exception("Unable to find the document due to the following error: ", e)

try:
    database = client.get_database("users_db")
    # users = database.get_collection("users_coll")
    
    doc = database.users_coll
    print(doc)
    # Query for a movie that has the title 'Back to the Future'
    # query = { "users": "Back to the Future" }
    # user = users.find_one(max_time_ms=100)
    # for doc in user:
        
    #     print(doc)
    client.close()
except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)