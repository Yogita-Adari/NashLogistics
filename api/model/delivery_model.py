from sqlalchemy import Column, Integer, String, Float, Text
from ..db import Base


class DeliveryRequest(Base):
    __tablename__ = "delivery_requests"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String(120), nullable=False)
    pickup_address = Column(String(255), nullable=False)
    dropoff_address = Column(String(255), nullable=False)
    package_weight_kg = Column(Float, nullable=False)
    priority = Column(String(20), nullable=False, default="normal")
    notes = Column(Text, nullable=True)
    delivery_date = Column(String(50), nullable=True)
