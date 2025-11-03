# Contributing Guide

## Development Workflow

### Prerequisites
- Python 3.12+
- Node.js 18+
- Docker (optional)
- Git

### Setup Development Environment

```bash
# Clone and setup
git clone <repo-url>
cd scrape-rate-deai
make setup
```

### Running Locally

```bash
# Run both services
make run

# Or run separately:
# Terminal 1 - Backend
cd backend && source venv/bin/activate && uvicorn main:app --reload

# Terminal 2 - Frontend
cd frontend && npm start
```

### Testing

```bash
# Run all tests
make test

# Backend only
cd backend && source venv/bin/activate && pytest

# Frontend only
cd frontend && npm test
```

### Linting & Formatting

```bash
# Run all linters
make lint

# Backend
cd backend && source venv/bin/activate && ruff check .

# Frontend
cd frontend && npm run lint
```

### Code Standards

- **Python**: Follow PEP 8, use type hints where possible
- **JavaScript**: Use ESLint + Prettier configuration
- **Commits**: Use conventional commits (feat:, fix:, docs:, etc.)
- **Tests**: Maintain >85% coverage for new code

### Pull Request Process

1. Create feature branch from `main`
2. Make changes with tests
3. Run `make verify` locally
4. Push and create PR
5. Wait for CI to pass
6. Request review

### Security

- Never commit secrets or API keys
- Use `.env` for local configuration
- Run `pip-audit` and `npm audit` before PR
- Report vulnerabilities privately

## Project Structure

```
scrape-rate-deai/
├── backend/          # FastAPI backend
│   ├── main.py       # API endpoints
│   ├── scraper.py    # Web scraping logic
│   ├── ai_text_tools.py  # AI text analysis
│   └── tests/        # Backend tests
├── frontend/         # React frontend
│   ├── src/          # React components
│   └── public/       # Static assets
├── .github/          # CI/CD workflows
└── docs/             # Additional documentation
```

## Getting Help

- Check README.md for quick start
- Review existing issues
- Ask in discussions
- Contact maintainers
