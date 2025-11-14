# CI/CD Pipeline Documentation

This repository uses GitHub Actions for continuous integration and continuous deployment.

## Workflows

### 1. `main.yml` - Main CI/CD Pipeline
**Triggers:**
- Push to `main` or `master` branch
- Pull request opened, updated, or closed
- **Automatically runs when a PR is merged**

**Jobs:**
- **test-and-validate**: Runs tests, linting, and validations
- **on-pr-merge**: Post-merge actions (runs only when PR is merged)

**What it does:**
- ✅ Code formatting check (Black)
- ✅ Linting (Flake8)
- ✅ Migration checks
- ✅ Django system checks
- ✅ Full test suite execution
- ✅ Coverage report generation
- ✅ Static files collection (on merge)

### 2. `ci.yml` - Comprehensive CI Pipeline
**Triggers:**
- Push to `main` or `master`
- Pull request closed (merged)

**Jobs:**
- **test**: Runs tests with PostgreSQL service
- **security**: Security scanning with Safety and Bandit
- **build**: Build validation and static files collection

### 3. `pr-merge.yml` - PR Merge Specific Pipeline
**Triggers:**
- Pull request closed (only when merged)

**What it does:**
- Validates migrations
- Runs full test suite
- Checks for migration conflicts
- Validates Django settings

## How to Use

1. **Create a branch** for your changes
2. **Make your changes** and commit them
3. **Push to GitHub** and create a Pull Request
4. **CI will automatically run** on the PR
5. **When PR is merged**, the pipeline will:
   - Run all tests
   - Validate migrations
   - Check code quality
   - Generate coverage reports

## Local Testing

Before pushing, you can run these commands locally:

```bash
# Run tests
python manage.py test tasks

# Check migrations
python manage.py makemigrations --check

# Run linting (if installed)
flake8 .

# Check code formatting
black --check .
```

## Secrets

The workflows use a `SECRET_KEY` secret. You can set it in:
- Repository Settings → Secrets and variables → Actions

If not set, it will use a default test key for CI purposes.

## Status Badge

Add this to your README.md to show CI status:

```markdown
![CI/CD Pipeline](https://github.com/YOUR_USERNAME/YOUR_REPO/workflows/Django%20CI%2FCD%20Pipeline/badge.svg)
```

