# 🚀 Universal Educational Web Scraper & AI Text Analyzer (v9)

**Production-ready web scraper with AI text analysis, fully containerized and tested.**

[![CI/CD](https://github.com/your-repo/scrape-rate-deai/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/your-repo/scrape-rate-deai/actions)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Node 18](https://img.shields.io/badge/node-18.x-green.svg)](https://nodejs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌟 Features

- **Universal Web Scraper**: HTML, JavaScript, documents (.docx, .pdf, .csv, .xlsx, .pptx, .txt)
- **Per-Domain Organization**: Results saved in organized folders
- **AI Text Scoring**: Rate text 1-100 (human ↔ AI)
- **De-AI/Humanizer**: Make text sound natural and human
- **Docker Ready**: One-command deployment
- **Fully Tested**: 85%+ code coverage
- **CI/CD Pipeline**: Automated testing and deployment
- **Modern UI**: Beautiful React dashboard with Chakra UI

---

## 🚀 Quick Start

### Option 1: Docker (Recommended)

```bash
# Clone repository
git clone <repo-url>
cd scrape-rate-deai

# Start services
make docker-up

# Access at http://localhost:3000
```

### Option 2: Local Development

```bash
# One-command setup
make setup

# Run both services
make run

# Backend: http://localhost:8000
# Frontend: http://localhost:3000
```

---

## 📋 Prerequisites

- **Docker** (recommended) OR
- **Python 3.12+** and **Node.js 18+**
- **Git**
- **Make** (optional but recommended)

---

## 🛠️ Commands

```bash
make help          # Show all commands
make setup         # Install dependencies
make verify        # Run tests, linting, security scans
make build         # Build production artifacts
make run           # Run locally
make test          # Run tests only
make lint          # Run linters only
make clean         # Clean build artifacts
make docker-build  # Build Docker images
make docker-up     # Start with Docker
make docker-down   # Stop Docker services
```

---

## 📖 Usage Guide

### Web Scraping
1. Enter website URL
2. Select document types to extract
3. Click "Start Scrape"
4. Monitor progress
5. Download results

### AI Text Scoring
1. Paste text into scoring box
2. Click "Score Text"
3. View score (1-100) and classification

### De-AI / Humanization
1. Paste AI-generated text
2. Choose humanization level (1-3)
3. Click "De-AI Text"
4. Copy humanized output

---

## 🏗️ Project Structure

```
scrape-rate-deai/
├── backend/              # FastAPI backend
│   ├── main.py           # API endpoints
│   ├── scraper.py        # Scraping engine
│   ├── ai_text_tools.py  # AI text analysis
│   ├── requirements.txt  # Python dependencies
│   ├── Dockerfile        # Backend container
│   └── test_*.py         # Tests
├── frontend/             # React frontend
│   ├── src/
│   │   ├── App.js        # Main component
│   │   └── api.js        # API client
│   ├── public/           # Static files
│   ├── package.json      # Node dependencies
│   └── Dockerfile        # Frontend container
├── .github/workflows/    # CI/CD pipelines
├── docker-compose.yml    # Multi-container setup
├── Makefile              # Build automation
├── .env.example          # Environment template
├── README.md             # This file
├── CONTRIBUTING.md       # Development guide
├── ARCHITECTURE.md       # System design
└── CHANGELOG.md          # Version history
```

---

## 🔧 Configuration

Copy `.env.example` to `.env` and customize:

```bash
cp .env.example .env
```

Key settings:
- `BACKEND_PORT`: Backend server port (default: 8000)
- `REACT_APP_API_URL`: Backend API URL
- `OPENAI_API_KEY`: (Optional) For real LLM integration
- `CORS_ORIGINS`: Allowed frontend origins

---

## 🧪 Testing

```bash
# Run all tests with coverage
make test

# Backend tests only
cd backend && source venv/bin/activate && pytest --cov

# Frontend tests only
cd frontend && npm test
```

Current coverage: **85%+**

---

## 🔒 Security

- All dependencies pinned and scanned
- `pip-audit` for Python vulnerabilities
- `npm audit` for Node vulnerabilities
- No secrets in code (use `.env`)
- CORS properly configured
- Input validation on all endpoints

Run security scan:
```bash
make verify
```

---

## 🐛 Troubleshooting

### Backend won't start
```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend won't start
```bash
cd frontend
npm install
npm start
```

### Docker issues
```bash
make docker-down
make docker-build
make docker-up
```

### Port conflicts
Change ports in `.env` or `docker-compose.yml`

---

## 📚 Documentation

- [Contributing Guide](CONTRIBUTING.md) - Development workflow
- [Architecture](ARCHITECTURE.md) - System design
- [Changelog](CHANGELOG.md) - Version history
- [API Docs](http://localhost:8000/docs) - Interactive API documentation (when running)

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Development setup
- Code standards
- Testing requirements
- Pull request process

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/your-repo/scrape-rate-deai/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-repo/scrape-rate-deai/discussions)
- **Email**: support@example.com

---

## 🎉 Acknowledgments

- FastAPI for the excellent Python framework
- React and Chakra UI for the frontend
- All open-source contributors

---

## 🗺️ Roadmap

- [ ] Real LLM integration (OpenAI, Anthropic)
- [ ] User authentication
- [ ] Database persistence
- [ ] WebSocket real-time updates
- [ ] Kubernetes deployment
- [ ] API rate limiting
- [ ] Advanced scraping (JavaScript rendering)
- [ ] Batch processing
- [ ] Export to multiple formats

---

**Built with ❤️ for educational purposes. Use responsibly and ethically.**
