# Upgrade Notes - v9.0.0

## Breaking Changes

### Backend
- **Starlette upgraded**: 0.45.1 → 0.49.1
  - No breaking API changes for this project
  - Security fixes applied
- **Requests upgraded**: 2.32.3 → 2.32.4
  - Security patch only

### Frontend
- **React Scripts**: Still on 5.0.1 (has known vulnerabilities in dev dependencies)
  - These are dev-only vulnerabilities, not affecting production builds
  - Consider migrating to Vite in future for better security

## New Dependencies

### Backend
- `python-multipart==0.0.20` - Required for form data parsing

### Frontend
- `@testing-library/jest-dom` - Testing utilities
- `@testing-library/react` - React testing
- `@testing-library/user-event` - User interaction testing
- `web-vitals` - Performance monitoring

## Migration Steps

### From v8.x to v9.0

1. **Backup your data**:
   ```bash
   cp -r output_* backup/
   ```

2. **Pull latest code**:
   ```bash
   git pull origin main
   ```

3. **Clean old dependencies**:
   ```bash
   make clean
   rm -rf backend/venv
   rm -rf frontend/node_modules
   ```

4. **Reinstall**:
   ```bash
   make setup
   ```

5. **Run tests**:
   ```bash
   make test
   ```

6. **Verify**:
   ```bash
   make verify
   ```

## Rollback Instructions

If you need to rollback to v8.x:

```bash
# Stop services
make docker-down

# Checkout previous version
git checkout v8.0.0

# Reinstall dependencies
make setup

# Restart
make run
```

## Known Issues

### Frontend Vulnerabilities
- `react-scripts@5.0.1` has transitive dev dependencies with known vulnerabilities
- **Impact**: Development only, does not affect production builds
- **Mitigation**: Production builds are safe, vulnerabilities are in dev tooling
- **Future**: Plan migration to Vite or upgrade to react-scripts 6.x when stable

### PyPDF2 Deprecation
- PyPDF2 is deprecated in favor of pypdf
- **Impact**: Warning message only, functionality works
- **Future**: Migrate to pypdf in next major version

## Performance Improvements

- Docker multi-stage builds reduce image size
- Frontend build optimizations
- Backend async improvements

## Security Enhancements

- All high/critical vulnerabilities fixed
- Dependency pinning enforced
- Security scanning in CI/CD
- Pre-commit hooks for secret detection

## Configuration Changes

### New Environment Variables
- `CORS_ORIGINS` - Configure allowed origins
- `MAX_SCRAPE_DEPTH` - Limit scraping depth
- `REQUEST_TIMEOUT` - HTTP request timeout

### Removed Variables
- None

## Testing Changes

- Backend coverage now tracked
- Frontend tests simplified
- CI/CD runs full test suite
- Security audits automated

## Documentation Updates

- New ARCHITECTURE.md
- Enhanced CONTRIBUTING.md
- Updated README.md with Docker instructions
- Added this UPGRADE_NOTES.md

## Support

If you encounter issues during upgrade:
1. Check [GitHub Issues](https://github.com/your-repo/issues)
2. Review [TROUBLESHOOTING.md](README.md#troubleshooting)
3. Open a new issue with:
   - Version upgrading from/to
   - Error messages
   - Steps to reproduce
