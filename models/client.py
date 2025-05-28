from sqlalchemy import Column, Integer, String
from database import Base
from database import Session
class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"<Client(id={self.id}, name={self.name})>"
    @classmethod
    def create(cls, name, phone, email):
        session = Session()
        client = cls(name=name, phone=phone, email=email)
        session.add(client)
        session.commit()
        return client

    @classmethod
    def get_all(cls):
        session = Session()
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        session = Session()
        return session.query(cls).get(id)

    def delete(self):
        session = Session()
        session.delete(self)
        session.commit()