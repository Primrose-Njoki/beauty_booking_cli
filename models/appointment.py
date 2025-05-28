from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, Session

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    stylist_id = Column(Integer, ForeignKey('stylists.id'))
    service = Column(String)
    date_time = Column(DateTime)
    duration = Column(Integer)

    client = relationship("Client")
    stylist = relationship("Stylist")

    def __repr__(self):
        return (f"<Appointment(id={self.id}, service='{self.service}', "
                f"date_time='{self.date_time}', duration={self.duration})>")

    @classmethod
    def create(cls, client_id, stylist_id, service, date_time, duration):
        session = Session()
        appointment = cls(
            client_id=client_id,
            stylist_id=stylist_id,
            service=service,
            date_time=date_time,
            duration=duration
        )
        session.add(appointment)
        session.commit()
        return appointment

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
