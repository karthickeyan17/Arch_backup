from pymongo import MongoClient
def main():
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)

    try:
        database = client.get_database("learn")
        movies = database.get_collection("sample1")

        # Query for a movie that has the title 'Back to the Future'
        res = movies.find({})
        for i in res:
            print(i)
        # for i in movie:
        #     print(i)

        client.close()

    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)


if __name__=="__main__":
    main()