from mongoengine import *


# Create your models here.
class Autor(Document):
    nombre = StringField()
    foto = StringField()


class Detalle(EmbeddedDocument):
    n_pag = IntField()
    editorial = StringField()
    isbn = StringField()


class Libro(Document):
    nombre = StringField()
    autor = ReferenceField(Autor, required=True, reverse_delete_rule=CASCADE)
    detalles = EmbeddedDocumentField(Detalle)
