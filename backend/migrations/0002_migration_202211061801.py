# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Document(peewee.Model):
    id = CharField(max_length=255, primary_key=True)
    business_statement = TextField(null=True)
    link = CharField(max_length=255, null=True)
    processed = BooleanField(default=False)
    class Meta:
        table_name = "document"


@snapshot.append
class CIK(peewee.Model):
    id = CharField(max_length=255, primary_key=True)
    document = snapshot.ForeignKeyField(backref='document', index=True, model='document')
    class Meta:
        table_name = "cik"


@snapshot.append
class HaramPassage(peewee.Model):
    id = CharField(max_length=255, primary_key=True)
    text = TextField()
    score = FloatField()
    document = snapshot.ForeignKeyField(backref='haram_passage', index=True, model='document')
    class Meta:
        table_name = "harampassage"


@snapshot.append
class Ticker(peewee.Model):
    symbol = CharField(max_length=255)
    cik = snapshot.ForeignKeyField(backref='ticker', index=True, model='cik')
    class Meta:
        table_name = "ticker"


def backward(old_orm, new_orm):
    document = new_orm['document']
    return [
        # Check the field `document.business_statement` does not contain null values,
        # Apply default value '' to the field document.link,
        document.update({document.link: ''}).where(document.link.is_null(True)),
    ]
