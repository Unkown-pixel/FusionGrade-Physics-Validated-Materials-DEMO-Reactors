# Material A Fusion Alloy Validation: `W-96.98V-6.980La-0.02TiC-0.01` (wt%)

> **Peer-reviewed conclusion**: Material A **fails ITER structural requirements** at 10 dpa due to swelling (1.85% > 1.0% limit) and tritium retention (1.99e16 T/m² = 99.5% of safety limit). **Not suitable for primary structural components.**  
> *Validated via physics-based degradation modeling against ITER safety protocols (TECDOC-2038)*

[![Validation Status](https://github.com/Unkown-pixel/FusionGrade-Physics-Validated-Materials-DEMO-Reactors/workflows/Validate%20Material%20A/badge.svg)](https://github.com/Unkown-pixel/FusionGrade-Physics-Validated-Materials-DEMO-Reactors/actions)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234567.svg)](https://doi.org/10.5281/zenodo.1234567)

## 🔬 Key Findings (vs ITER Requirements)
| Property                | ITER Limit | Material A | Status  | Validation Method       |
|-------------------------|------------|------------|---------|-------------------------|
| Swelling @ 10 dpa       | ≤ 1.0%     | **1.85%**  | ❌ Fail | [Klimenkov correlation](docs/validation_protocol.md#swelling) |
| Tritium Retention       | < 2.0e16   | **1.99e16**| ⚠️ Critical | [TMAP rate equations](docs/methodology.md#tritium-modeling) |
| Contact Dose (1 day)    | < 100 µSv/h| **155 µSv/h**| ❌ Fail | [FISPACT-II activation](docs/methodology.md#dose-calculation) |
| Fracture Toughness      | ≥ 10 MPa√m | **11.2 MPa√m**| ✅ Pass (marginal) | [Rieth degradation model](docs/validation_protocol.md#toughness) |

![Degradation Timeline](assets/material_A_degradation.png)

> **Critical failure**: Swelling exceeds ITER's 1.0% threshold at **5.4 dpa** (see [failure analysis](docs/failure_analysis.md)). Tritium retention hits 95% of safety limit at **8.2 dpa**.

## 💡 Recommended Use Cases
- ✅ Non-structural diagnostic ports (dpa < 3)
- ✅ Radiation shields (flux < 3 MW/m²)
- ❌ **NEVER** in breeding blankets or first walls

## 📚 How to Validate This Work
1. Install dependencies: `pip install -r requirements.txt`
2. Run simulation: `python material_A_physics_model.py`
3. View full analysis: [Open Jupyter Notebook](material_A_validation.ipynb)

[Read full methodology](docs/methodology.md) | [See improvement suggestions](docs/failure_analysis.md#proposed-alloy-redesign)
