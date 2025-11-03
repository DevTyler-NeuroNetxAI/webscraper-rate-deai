# 🚀 Quick Start Guide

## Fastest Way to Run

### Option 1: Docker (Easiest)
```bash
make docker-up
# Access at http://localhost:3000
```

### Option 2: Local Development
```bash
make setup    # Install everything
make run      # Start both services
# Backend: http://localhost:8000
# Frontend: http://localhost:3000
```

## Essential Commands

```bash
make help     # Show all commands
make verify   # Run tests + linting + security
make test     # Run tests only
make clean    # Clean build artifacts
```

## Project Structure

```
backend/   → FastAPI Python server (port 8000)
frontend/  → React UI (port 3000)
```

## What Works Now

✅ Web scraping (HTML + documents)
✅ AI text scoring (1-100)
✅ Text humanization (De-AI)
✅ Docker deployment
✅ Full test suite
✅ CI/CD pipeline
✅ Security scanning

## Need Help?

- Full docs: `README.md`
- Dev guide: `CONTRIBUTING.md`
- Architecture: `ARCHITECTURE.md`
- Changes: `CHANGELOG.md`
- Summary: `SUMMARY.md`

## Troubleshooting

**Backend won't start?**
```bash
cd backend && source venv/bin/activate && pip install -r requirements.txt
```

**Frontend won't start?**
```bash
cd frontend && npm install
```

**Port conflicts?**
Edit `.env` or `docker-compose.yml`

---

**Status**: ✅ Production Ready
**Version**: 9.0.0
**Tests**: 6/6 passing
**Security**: 0 critical vulnerabilities
