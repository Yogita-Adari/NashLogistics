const BASE = "http://127.0.0.1:5001/api";

export async function listDeliveries() {
  const res = await fetch(`${BASE}/deliveries/`);
  return res.json();
}

export async function createDelivery(payload: any) {
  const res = await fetch(`${BASE}/deliveries/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return res.json();
}
