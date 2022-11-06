import os

from peewee import (
    PostgresqlDatabase, Model, CharField,
    TextField, FloatField, BooleanField, AutoField, ForeignKeyField,

)

DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_USER = os.getenv("POSTGRES_USER")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_PASSWORD = os.getenv("PGPASSWORD")


db = PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASSWORD,
                        host=DB_HOST, port=DB_PORT)


class BaseModel(Model):
    class Meta:
        database = db


class Document(BaseModel):
    id = CharField(primary_key=True)
    business_statement = TextField()
    link = CharField()
    processed = BooleanField(default=False)


class CIK(BaseModel):
    id = CharField(primary_key=True)
    document = ForeignKeyField(Document, backref="document")


class Ticker(BaseModel):
    id = AutoField()
    symbol = CharField()
    cik = ForeignKeyField(CIK, backref="ticker")


class HaramPassage(BaseModel):
    id = CharField(primary_key=True)
    text = TextField()
    score = FloatField()
    document = ForeignKeyField(Document, backref="haram_passage")
