from pymongo import MongoClient
def main():
    uri = "mongodb+srv://karthickeyan:9994366529@cluster0.htv3d.mongodb.net/"
    client = MongoClient(uri)

    try:
        database = client.get_database("learn")
        col = database['sample1']
        for val in col.next():
            print(val)
        client.close()

    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)


if __name__=="__main__":
    main()