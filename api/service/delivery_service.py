from sqlalchemy.orm import Session
from ..repo.delivery_repository import DeliveryRepository

REQUIRED = [
    "customer_name",
    "pickup_address",
    "dropoff_address",
    "package_weight_kg",
    "priority",
]

class DeliveryService:
    def __init__(self, db: Session):
        self.repo = DeliveryRepository(db)

    def create_request(self, data: dict):
        for field in REQUIRED:
            if field not in data or data[field] in (None, ""):
                raise ValueError(f"Missing field: {field}")

        data["package_weight_kg"] = float(data["package_weight_kg"])
        if data["package_weight_kg"] <= 0:
            raise ValueError("Weight must be greater than 0")

        if data["priority"] not in ("normal", "express"):
            raise ValueError("Priority must be 'normal' or 'express'")

        return self.repo.create(data)

    def list_requests(self):
        return self.repo.list_all()
