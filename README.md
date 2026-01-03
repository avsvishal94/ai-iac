# ai-iac

AI-based Infrastructure-as-Code (IaC) generator that converts architecture diagrams into structured infrastructure definitions.

This project uses:
- Docker Compose for backend services
- React + Vite for the UI
- A Makefile to standardize local development commands

---

## Prerequisites

Make sure the following are installed and running:

- Docker Desktop (running)
- Node.js (v18+)
- npm
- make

---

## Local Development Workflow

All commands below are executed **from the repository root**.

---

```bash
Step 1: Start backend
make backend-up

Step 2: Rebuild backend (after backend code changes)
make backend-rebuild

Step 3: View backend logs
make backend-logs

Step 4: Install UI dependencies
make ui-install

Step 5: Start UI
make ui-dev

Step 6: Stop everything
make clean