# =========================================
# AI IaC Platform - Makefile
# =========================================

.PHONY: help backend-up backend-down backend-build backend-rebuild \
        backend-logs backend-status ui-install ui-dev ui-stop clean

# -----------------------------------------
# Help
# -----------------------------------------
help:
	@echo ""
	@echo "AI IaC Platform - Available Commands"
	@echo ""
	@echo "Backend (Docker):"
	@echo "  make backend-up        Start backend services (detached)"
	@echo "  make backend-down      Stop backend services"
	@echo "  make backend-build     Build backend images"
	@echo "  make backend-rebuild   Rebuild backend images (no cache)"
	@echo "  make backend-logs      Show backend logs"
	@echo "  make backend-status    Show running backend containers"
	@echo ""
	@echo "UI (React / Vite):"
	@echo "  make ui-install        Install UI dependencies"
	@echo "  make ui-dev            Start UI dev server"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean             Stop all backend services"
	@echo ""

# -----------------------------------------
# Backend (Docker)
# -----------------------------------------
backend-up:
	cd infra && docker compose up -d

backend-down:
	cd infra && docker compose down

backend-build:
	cd infra && docker compose build

backend-rebuild:
	cd infra && docker compose down && docker compose build --no-cache && docker compose up -d

backend-logs:
	cd infra && docker compose logs -f

backend-status:
	cd infra && docker compose ps

# -----------------------------------------
# UI (React / Vite)
# -----------------------------------------
ui-install:
	cd apps/idp-ui && npm install

ui-dev:
	cd apps/idp-ui && npm run dev

# -----------------------------------------
# Cleanup
# -----------------------------------------
clean:
	cd infra && docker compose down
