from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..service.delivery_service import DeliveryService

bp = Blueprint("delivery", __name__, url_prefix="/api/deliveries")

def with_session(fn):
    def wrapper(*args, **kwargs):
        db: Session = SessionLocal()
        try:
            return fn(db, *args, **kwargs)
        finally:
            db.close()
    wrapper.__name__ = fn.__name__
    return wrapper

@bp.post("/")
@with_session
def create_delivery(db: Session):
    data = request.get_json()
    service = DeliveryService(db)
    try:
        obj = service.create_request(data)
        return jsonify({"id": obj.id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp.get("/")
@with_session
def list_deliveries(db: Session):
    service = DeliveryService(db)
    rows = service.list_requests()
    return jsonify([
        {
            "id": r.id,
            "customer_name": r.customer_name,
            "pickup_address": r.pickup_address,
            "dropoff_address": r.dropoff_address,
            "package_weight_kg": r.package_weight_kg,
            "priority": r.priority,
            "notes": r.notes or ""
        } for r in rows
    ])
