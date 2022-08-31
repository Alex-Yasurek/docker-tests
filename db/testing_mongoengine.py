from email.policy import default
from mongoengine import connect, Document, ListField, StringField, URLField

connect(db="rptutorials", host="localhost", port=27017)

class Tutorial(Document):
    title = StringField(required=True, max_length=70)
    author = StringField(required=True, max_length=20)
    contributors = ListField(StringField(max_length=20))
    url = URLField(required=True, default="www.google.com")


# tutorial1 = Tutorial(
#     title="Beautiful Soup: Build a Web Scraper With Python",
#     author="Martin",
#     contributors=["Aldren", "Geir Arne", "Jaya", "Joanna", "Mike"],
#     url="https://realpython.com/beautiful-soup-web-scraper-python/"
# )

# tutorial1.save()


# tutorial2 = Tutorial()
# tutorial2.author = "Alex"
# tutorial2.contributors = ["Aldren", "Jon", "Joanna"]
# tutorial2.url = "https://realpython.com/convert-python-string-to-int/"
# # error if no title is given
# tutorial2.title = "Alex's book title"
# tutorial2.save()


for doc in Tutorial.objects:
    print(doc.title)

for doc in Tutorial.objects(author="Alex"):
    print(doc.title)
