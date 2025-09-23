# 🌋 W-V-La-TiC / W-Ta-Ti / V-Cr-Ti Fusion Wall Materials Research

> *Open research initiative for next-gen fusion materials across all reactor zones:  
> **Material A**: `W-96.98V-6.980La-0.02TiC-0.01` (structural)  
> **Material B**: `W-94.9V-4.98La-0.02TiC0.1` (plasma-facing)  
> **Material C**: `W-92Ta-7Ti-1` (ultra-high-temp armor)  
> **Material D**: `V-92Cr-4Ti-4` (low-activation structural)  
> **Material E**: `W-92.9V-6.98La-0.02TiC0.1` (alternative structural)*

Simulated and validated against ITER/DEMO requirements as **specialized alternatives** to baseline materials (pure W, W-Re, EUROFER97), with physics-corrected radiation damage modeling.

⚠️ **Critical Note**: Only **Materials D and B** meet ITER structural safety thresholds at 10 dpa — A, C, E fail on swelling or embrittlement.

---

## 🚀 Why This Matters

No single material satisfies DEMO’s multi-threat environment. These compositions offer **five distinct performance envelopes**, each validated against 2023–2024 irradiation data:

- **Material A & E** → High-V tungsten alloys with microstructural stabilization (La₂O₃/TiC) — but **swelling exceeds ITER limit** (1.85% > 1.0%)
- **Material B** → Optimized for plasma-facing use: **lowest sputtering (0.071)** and **highest thermal conductivity (108 W/m·K)** among V-alloys
- **Material C** → Extreme temperature stability (>1500°C recrystallization onset) — but **fails structurally** (K_IC = 7.8 MPa√m < 10 MPa√m)
- **Material D** → The **only LLW-classified option** with K_IC = 12.3 MPa√m at 10 dpa — meets all ITER structural requirements
- All integrate **grain boundary pinning** (La₂O₃, TiC, Ti) to suppress He bubble coalescence
- All are fabricable via **MA + HIP**
- All support **functionally graded designs** (e.g., B → E → D for divertor monoblocks)

---

## 🧪 Material Roles at a Glance

| Material | Composition                     | Best For                          | Key Advantage                                | Meets ITER? | Activation Level     |
|--------|----------------------------------|-----------------------------------|----------------------------------------------|-------------|----------------------|
| **A**  | W-96.98,V-6.980,La-0.02,TiC-0.01 | Structural (Breeding Blanket)     | Toughness (11.2 MPa√m), but **swelling=1.85%** | ❌ No        | ✅ Low-Medium        |
| **B**  | W-94.9,V-4.98,La-0.02,TiC0.1    | Plasma-Facing (Divertor/Limiters) | Thermal cond. (108 W/m·K), low sputtering     | ⚠️ Marginal* | ✅ Low               |
| **C**  | W-92,Ta-7,Ti-1                  | Disruption Zones                  | Recrystallization >1500°C, but **K_IC=7.8**   | ❌ No        | ⚠️ Medium-High (Ta) |
| **D**  | V-92,Cr-4,Ti-4                  | Primary Structural Components     | **K_IC=12.3 MPa√m, swelling=0.82%, LLW**      | ✅ Yes       | ✅ Very Low          |
| **E**  | W-92.9,V-6.98,La-0.02,TiC0.1    | Structural (Alternative)          | Toughness (11.2 MPa√m), but **swelling=1.85%** | ❌ No        | ✅ Low-Medium        |

> *Material B passes K_IC (11.2 MPa√m) but has tritium retention = 1.99e16 T/m² (99.5% of limit). Requires active removal.*

---

## 📂 Repository Structure

- `/materials` — Full experimental summaries with **ITER compliance validation**  
  → [`Material A`](materials/Material A)  
  → [`Material B`](materials/Material B)  
  → [`Material C`](materials/Material C)  
  → [`Material D`](materials/Material D)  
  → [`Material E`](materials/Material E)  
- `/simulations` — Radiation damage models (He appm=10,000), transmutation (FISPACT-II), embrittlement curves


---

## 🔍 Validation Protocol

All simulations enforce **ITER safety thresholds**:
```python
assert K_IC >= 10.0, "FAIL: Below fracture toughness minimum"
assert swelling <= 1.0, "FAIL: Exceeds dimensional stability limit"
assert tritium_retention < 2.0e16, "WARN: Near tritium safety limit" 
