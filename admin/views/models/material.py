from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from .base_class import Base


class Material(Base):
    material_id = Column(Integer, primary_key=True)
    name = Column(String)
    order = relationship("Order", back_populates='material')

    def __repr__(self):
        return self.name
