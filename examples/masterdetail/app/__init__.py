import os
import logging
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.appbuilder import AppBuilder
from sqlalchemy.engine import Engine
from sqlalchemy import event


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
appbuilder = AppBuilder(app, db)

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)


"""
Only include this for SQLLite constraints

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""    

from app import views

