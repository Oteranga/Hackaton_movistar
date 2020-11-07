from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class Form(connector.Manager.Base):
    __tablename__ = 'form'
    id = Column(Integer, Sequence('form_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    phone = Column(String(9))
    telephone = Column(String(7))
