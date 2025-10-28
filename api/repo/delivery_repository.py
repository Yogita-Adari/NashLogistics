from typing import List
from sqlalchemy.orm import Session
from ..model.delivery_model import DeliveryRequest

class DeliveryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, payload: dict) -> DeliveryRequest:
        obj = DeliveryRequest(**payload)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list_all(self) -> List[DeliveryRequest]:
        return self.db.query(DeliveryRequest).order_by(DeliveryRequest.id.desc()).all()
