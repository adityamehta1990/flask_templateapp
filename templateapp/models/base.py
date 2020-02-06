'''Setup database models using sql-alchemy'''

import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from templateapp.web import config
from templateapp.utils.api import custom_json_encoder, custom_json_decoder

LOGGER = logging.getLogger(__name__)


engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI,
    echo=False,
    json_serializer=custom_json_encoder
    # json_deserializer=custom_json_decoder
)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from templateapp import models
    Base.metadata.create_all(bind=engine)
