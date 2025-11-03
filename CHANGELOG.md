# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [9.0.0] - 2025-01-XX

### Added
- Complete project restructure with proper dependency management
- Makefile with setup/verify/build/run targets
- Docker and docker-compose support for containerized deployment
- Comprehensive test suite (pytest for backend, Jest for frontend)
- CI/CD pipeline with GitHub Actions
- Linting and type checking (ruff, mypy, eslint, prettier)
- Security scanning with pip-audit and npm audit
- Environment configuration with .env.example
- Complete documentation (README, CONTRIBUTING, ARCHITECTURE)
- Pre-commit hooks support
- Coverage reporting

### Changed
- Fixed requirements.txt with proper version pinning
- Updated frontend dependencies to latest stable versions
- Improved error handling in API endpoints
- Enhanced CORS configuration

### Fixed
- Missing frontend public/index.html
- Missing frontend src/index.js entry point
- Invalid requirements.txt syntax (docx>=, uvicorn>=)
- Missing test infrastructure

### Security
- Added dependency vulnerability scanning
- Pinned all dependency versions
- Added .gitignore for sensitive files
- Removed hardcoded credentials

## [8.0.0] - Previous

### Added
- Initial web scraper functionality
- AI text scoring
- De-AI text humanization
- React dashboard
