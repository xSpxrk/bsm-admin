from sqlalchemy import VARCHAR, Integer, Column, String, BigInteger
from sqlalchemy.orm import relationship
from .base_class import Base



class Customer(Base):
    customer_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(BigInteger)
    hashed_password = Column(String)
    orders = relationship("Order", back_populates="customer")

    def __repr__(self):
        return self.name
