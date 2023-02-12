from mongoengine import EmbeddedDocument, Document, DENY
from mongoengine.fields import EmbeddedDocumentField, ListField, StringField, ReferenceField


class Author(Document):
    meta = {'collection': 'authors'}
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    meta = {'collection': 'quotes', 'allow_inheritance': True}
    tags = ListField(StringField(max_length=50))
    quote = StringField()
    author = ReferenceField(Author, required=True, reverse_delete_rule=DENY)
