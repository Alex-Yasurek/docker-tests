from pymongo import MongoClient
import pprint
# https://realpython.com/introduction-to-mongodb-and-python/

client = MongoClient(host="localhost", port=27017)
# client = MongoClient("mongodb://localhost:27017")

db = client.rptutorials
# db = client["rptutorials"]

# tutorial1 = {
#     "title": "Working With JSON Data in Python",
#     "author": "Lucas",
#     "contributors": [
#              "Aldren",
#              "Dan",
#              "Joanna"
#     ],
#     "url": "https://realpython.com/python-json/"
# }

# tutorial = db.tutorial
# result = tutorial.insert_one(tutorial1)
# print(f"One tutorial: {result.inserted_id}")

# tutorial2 = {
#     "title": "Another Book",
#     "author": "Bob",
#     "contributors": [
#              "Jack",
#              "Diane",
#              "Joanna"
#     ],
#     "url": "https://realpython.com/another-book/"
# }

# tutorial3 = {
#     "title": "Learning React",
#     "author": "O'reilly",
#     "contributors": [
#              "Julie",
#     ],
#     "url": "https://realpython.com/React/"
# }

# new_result = tutorial.insert_many([tutorial2, tutorial3])
# print(f"Multiple tutorials: {new_result.inserted_ids}")


# for doc in tutorial.find():
#     pprint.pprint(doc)

# jon_tutorial = tutorial.find_one({"author": "Bob"})
# pprint.pprint(jon_tutorial)

# client.close()

# this will open and close the client
with MongoClient() as client:
    db = client.rptutorials
    for doc in db.tutorial.find():
        print(doc['title'], '-', doc['contributors'][0])
