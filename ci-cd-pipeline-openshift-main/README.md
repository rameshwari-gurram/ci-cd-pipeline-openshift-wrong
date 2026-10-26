# CI/CD Pipeline Project for OpenShift

## Project name
CI/CD Pipeline for Application Deployment on OpenShift

## Overview
A small Python sample application used to demonstrate automated linting, unit testing, Tekton tasks, and an OpenShift pipeline.

## Technologies
- Python 3.8
- GitHub Actions
- flake8
- nose
- Tekton Pipelines
- OpenShift

## Files
- `app.py`: sample application functions
- `tests/test_app.py`: unit tests
- `.github/workflows/workflow.yml`: GitHub Actions lint and test workflow
- `.tekton/tasks.yml`: cleanup and nose Tekton tasks
- `.tekton/pipeline.yml`: example pipeline using the tasks
- `.tekton/pvc.yml`: example PersistentVolumeClaim manifest

## Run locally
```bash
python -m pip install -r requirements.txt
flake8 app.py tests
nosetests -v
```

## GitHub Actions
The workflow runs on pushes and pull requests to `main`. Review the Actions tab for the real results of each run.

## OpenShift / Tekton
Review the manifests under `.tekton/`. Apply them only in the OpenShift project/namespace supplied by your course lab and follow the lab's instructions. Storage class names and permissions may differ by cluster.

## Important
This is a starter sample, not a substitute for any course-provided repository or lab-specific resources. Do not submit fabricated logs or screenshots. Use actual successful workflow output and screenshots from your own OpenShift environment.
