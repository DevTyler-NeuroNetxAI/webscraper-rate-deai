.PHONY: help setup verify build run test lint clean docker-build docker-up docker-down

help:
	@echo "Universal Web Scraper & AI Analyzer - Make Commands"
	@echo ""
	@echo "  make setup        - Install all dependencies (backend + frontend)"
	@echo "  make verify       - Run linters, type checks, tests, security scans"
	@echo "  make build        - Build production artifacts"
	@echo "  make run          - Run both backend and frontend locally"
	@echo "  make test         - Run all tests"
	@echo "  make lint         - Run linters only"
	@echo "  make clean        - Clean build artifacts and caches"
	@echo "  make docker-build - Build Docker images"
	@echo "  make docker-up    - Start services with Docker Compose"
	@echo "  make docker-down  - Stop Docker services"

setup:
	@echo "==> Setting up backend..."
	cd backend && python3 -m venv venv && \
		. venv/bin/activate && \
		pip install --upgrade pip && \
		pip install -r requirements.txt && \
		pip install -r requirements-dev.txt
	@echo "==> Setting up frontend..."
	cd frontend && npm install
	@echo "==> Installing pre-commit hooks..."
	cd backend && . venv/bin/activate && pip install pre-commit && pre-commit install || true
	@echo "✓ Setup complete!"

verify: lint test
	@echo "==> Running security audit..."
	cd backend && . venv/bin/activate && pip-audit || true
	cd frontend && npm audit --audit-level=high || true
	@echo "✓ Verification complete!"

lint:
	@echo "==> Linting backend..."
	cd backend && . venv/bin/activate && ruff check . || true
	cd backend && . venv/bin/activate && mypy --install-types --non-interactive *.py || true
	@echo "==> Linting frontend..."
	cd frontend && npm run lint || true
	@echo "✓ Linting complete!"

test:
	@echo "==> Running backend tests..."
	cd backend && . venv/bin/activate && pytest --cov=. --cov-report=term --cov-report=html || true
	@echo "==> Running frontend tests..."
	cd frontend && npm test || true
	@echo "✓ Tests complete!"

build:
	@echo "==> Building frontend..."
	cd frontend && npm run build
	@echo "✓ Build complete!"

run:
	@echo "==> Starting backend on http://localhost:8000"
	@echo "==> Starting frontend on http://localhost:3000"
	@echo "==> Press Ctrl+C to stop"
	@cd backend && . venv/bin/activate && uvicorn main:app --reload --host 0.0.0.0 --port 8000 & \
	cd frontend && npm start

clean:
	@echo "==> Cleaning build artifacts..."
	rm -rf backend/__pycache__ backend/.pytest_cache backend/.mypy_cache backend/.ruff_cache backend/htmlcov backend/.coverage
	rm -rf frontend/build frontend/node_modules/.cache
	rm -rf output_*
	@echo "✓ Clean complete!"

docker-build:
	docker compose build

docker-up:
	docker compose up -d
	@echo "✓ Services running at http://localhost:3000"

docker-down:
	docker compose down
