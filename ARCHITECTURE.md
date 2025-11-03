# Architecture Documentation

## System Overview

Universal Educational Web Scraper & AI Text Analyzer is a full-stack application consisting of:
- **Backend**: FastAPI REST API (Python 3.12)
- **Frontend**: React SPA (Node 18)
- **Deployment**: Docker containers with docker-compose

## Architecture Diagram

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   Browser   │ ──HTTP─→│   Frontend   │ ──API─→ │   Backend   │
│  (Client)   │ ←─────→ │   (React)    │ ←─────→ │  (FastAPI)  │
└─────────────┘         └──────────────┘         └─────────────┘
                              :3000                    :8000
                                                         │
                                                         ↓
                                                   ┌──────────┐
                                                   │  Output  │
                                                   │  Files   │
                                                   └──────────┘
```

## Backend Components

### main.py
- FastAPI application entry point
- API endpoint definitions
- CORS middleware configuration
- Request/response models

### scraper.py
- Web scraping engine
- Document extraction (PDF, DOCX, XLSX, PPTX, CSV, TXT)
- Job queue management
- Progress tracking

### ai_text_tools.py
- AI text scoring (1-100 scale)
- Text humanization (De-AI)
- LLM integration placeholder

### auto_update.py
- Dependency auto-updater
- Package version management

## Frontend Components

### App.js
- Main React component
- UI for scraper, scoring, and De-AI features
- State management
- API integration

### api.js
- API client functions
- HTTP request handling
- Error management

## Data Flow

### Scraping Flow
1. User enters URL + document types
2. Frontend POST to `/scrape`
3. Backend creates job, returns job_id
4. Async scraping starts
5. Frontend polls `/status/{job_id}`
6. Results saved to `output_{domain}/`
7. Frontend fetches `/results/{domain}`
8. User downloads via `/download/{domain}/{file}`

### AI Scoring Flow
1. User pastes text
2. Frontend POST to `/score-text`
3. Backend analyzes text
4. Returns score (1-100) + label
5. Frontend displays result

### De-AI Flow
1. User pastes text + selects level
2. Frontend POST to `/deai-text`
3. Backend processes with LLM (placeholder)
4. Returns humanized text
5. Frontend displays result

## Technology Stack

### Backend
- **Framework**: FastAPI 0.120.4
- **Server**: Uvicorn 0.32.1
- **Scraping**: BeautifulSoup4, Selenium, Requests
- **Document Parsing**: python-docx, PyPDF2, pandas, python-pptx
- **Testing**: pytest, pytest-cov, httpx
- **Linting**: ruff, mypy
- **Security**: pip-audit

### Frontend
- **Framework**: React 18.3.1
- **UI Library**: Chakra UI 2.8.2
- **Build Tool**: react-scripts 5.0.1
- **Testing**: Jest, React Testing Library
- **Linting**: ESLint, Prettier

### DevOps
- **Containerization**: Docker, docker-compose
- **CI/CD**: GitHub Actions
- **Build Tool**: Make

## Security Considerations

- CORS restricted to localhost by default
- No authentication (add if needed)
- Input validation on all endpoints
- File type restrictions for uploads
- Dependency scanning with pip-audit/npm audit
- No secrets in code (use .env)

## Scalability

Current limitations:
- In-memory job queue (use Redis for production)
- Local file storage (use S3/blob storage for production)
- Single-instance deployment (add load balancer for scale)

## Future Enhancements

- Real LLM integration (OpenAI, Anthropic, etc.)
- User authentication and authorization
- Database for job persistence
- WebSocket for real-time progress
- Rate limiting
- Caching layer
- Kubernetes deployment
