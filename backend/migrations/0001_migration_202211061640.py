# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Document(peewee.Model):
    id = CharField(max_length=255, primary_key=True)
    business_statement = TextField()
    link = CharField(max_length=255)
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


