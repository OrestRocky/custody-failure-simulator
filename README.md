# Custody Failure Simulator

A simulation tool to model and analyze custody/settlement failure scenarios, helping teams test resilience, controls, and recovery workflows.

## Why
Custody and settlement systems are complex. This project lets you simulate failure modes and observe outcomes before they happen in production.

## Features
- Configurable failure scenarios (timeouts, partial fills, missing confirmations, bad balances, etc.)
- Deterministic runs via seeded randomness
- Scenario reports (metrics, timelines, and outcomes)
- Pluggable “actors” (custodian, broker, ledger, reconciliation)
- Export results to JSON/CSV (optional)
- Built-in sanity checks & invariants

## Quick start
> Requirements: (Python/Node/Go + version) — update this line.

```bash
git clone https://github.com/<you>/custody-failure-simulator.git
cd custody-failure-simulator
# install deps:
# e.g. pip install -r requirements.txt
# or npm install
# run:
# e.g. python -m cfs run --scenario examples/basic.yaml
```

## Example

```bash
run --scenario examples/basic.yaml --seed 42
```
