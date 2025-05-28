from sqlalchemy import Column, Integer, String
from database import Base, Session

class Stylist(Base):
    __tablename__ = 'stylists'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialty = Column(String)

    def __repr__(self):
        return f"<Stylist(id={self.id}, name={self.name})>"

    @classmethod
    def create(cls, name, specialty):
        session = Session()
        stylist = cls(name=name, specialty=specialty)
        session.add(stylist)
        session.commit()
        return stylist

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
