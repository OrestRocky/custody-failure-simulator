 Custody Failure Simulator

Custody Failure Simulator is a deterministic simulation framework for modeling custody, settlement, and reconciliation failure scenarios.  
It helps engineers and risk teams test system resilience, controls, and recovery flows **before failures occur in production**.

---

## 🚀 Key Features

- Failure scenario simulation (timeouts, partial execution, missing confirmations)
- Deterministic runs using seeded randomness
- Modular actor-based architecture
- Config-driven scenarios (YAML / JSON)
- Reproducible reports with timelines and metrics
- Designed for testing, education, and system validation

---

## 📦 Use Cases

- Stress‑testing custody and settlement logic  
- Verifying reconciliation invariants  
- Replaying historical or hypothetical failure events  
- Teaching failure‑mode analysis  

---

## ⚡ Quick Start

### Requirements
- Runtime: **Python 3.10+** (change if needed)
- OS: Linux / macOS / Windows

### Installation
```bash
git clone https://github.com/<your-username>/custody-failure-simulator.git
cd custody-failure-simulator
pip install -r requirements.txt
Run a sample scenario
python -m cfs run --scenario examples/basic_failure.yaml --seed 42

Usage
Run simulator
cfs run \
  --scenario examples/timeout.yaml \
  --seed 1337 \
  --out reports/result.json
CLI Options
Option	Description
--scenario	Path to scenario config
--seed	Deterministic random seed
--out	Output report path
--verbose	Extended logs

 Scenario Format (YAML)
name: custody-timeout
steps:
  - actor: custodian
    action: transfer_out
    asset: USDC
    amount: 1000

  - actor: network
    action: timeout
    after_ms: 5000

  - actor: reconciliation
    action: detect_mismatch

 Architecture
src/
 ├── engine/        # Simulation engine
 ├── actors/        # Custodian, broker, ledger, network
 ├── scenarios/     # Scenario parsing & validation
 ├── reports/       # Output generation
 └── cli.py         # CLI entrypoint

examples/
tests/
docs/

 Testing
pytest

 Safety Disclaimer
This project is a simulation and educational tool only.
It must NOT be used to operate, exploit, or bypass real custody or financial systems.

 Roadmap
 More predefined failure templates
 Visual timeline reports
 Docker support
 CI (lint + test)
 Scenario fuzzing

 Contributing
Fork the repo
Create a feature branch
Add tests where applicable
Open a PR with a clear description

 License
MIT License


