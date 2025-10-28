import { useEffect, useState } from "react";
import { listDeliveries, createDelivery } from "./api";

type Req = {
  customer_name: string;
  pickup_address: string;
  dropoff_address: string;
  package_weight_kg: number | string;
  priority: "normal" | "express";
  notes?: string;
  delivery_date: string;
};

const empty: Req = {
  customer_name: "",
  pickup_address: "",
  dropoff_address: "",
  package_weight_kg: "",
  priority: "normal",
  notes: "",
  delivery_date: "",
};

export default function App() {
  const [form, setForm] = useState<Req>(empty);
  const [rows, setRows] = useState<any[]>([]);
  const [error, setError] = useState<string>("");

  const load = async () => setRows(await listDeliveries());
  useEffect(() => { load(); }, []);

  const submit = async (e: any) => {
    e.preventDefault();
    setError("");
    const res = await createDelivery({
      ...form,
      package_weight_kg: Number(form.package_weight_kg),
    });
    if (res.error) setError(res.error);
    else { setForm(empty); await load(); }
  };

  return (
    <div style={{ maxWidth: 720, margin: "24px auto", padding: 16 }}>
      <h1>Delivery Request Form</h1>
      <form onSubmit={submit} style={{ display: "grid", gap: 8 }}>
        <input placeholder="Customer name" value={form.customer_name}
          onChange={e => setForm({ ...form, customer_name: e.target.value })}/>
        <input placeholder="Pickup address" value={form.pickup_address}
          onChange={e => setForm({ ...form, pickup_address: e.target.value })}/>
        <input placeholder="Dropoff address" value={form.dropoff_address}
          onChange={e => setForm({ ...form, dropoff_address: e.target.value })}/>
        <input type="number" placeholder="Package weight (kg)"
          value={form.package_weight_kg}
          onChange={e => setForm({ ...form, package_weight_kg: e.target.value })}/>
        <input type="date" placeholder="Delivery Date" 
          value={form.delivery_date}
          onChange={e => setForm({ ...form, delivery_date: e.target.value })}/>
        <select value={form.priority}
          onChange={e => setForm({ ...form, priority: e.target.value as any })}>
          <option value="normal">Normal</option>
          <option value="express">Express</option>
        </select>
        <textarea placeholder="Notes" value={form.notes}
          onChange={e => setForm({ ...form, notes: e.target.value })}/>
        <button type="submit">Submit</button>
        {error && <p style={{ color: "red" }}>{error}</p>}
      </form>

      <h2 style={{ marginTop: 24 }}>Existing Deliveries</h2>
      <ul>
        {rows.map(r => (
          <li key={r.id}>
            #{r.id} • {r.customer_name} • {r.priority} • {r.package_weight_kg} kg
            <br/> {r.pickup_address} → {r.dropoff_address}
          </li>
        ))}
      </ul>
    </div>
  );
}
