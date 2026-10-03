# Google Cloud Platform (GCP) App Engine Python Static App

![python](https://img.shields.io/badge/python-3.11.6-informational)
![fastapi-0.116.0-informational](https://img.shields.io/badge/fastapi-0.116.0-informational)

This is a FastAPI application, that only serves static files for [Google App Engine Flexible Environment](https://cloud.google.com/appengine),
this is a continuation of my other repositories to deploy simple apps to various cloud providers e.g. [digital ocean](https://github.com/kwame-mintah/digitalocean-static-app),
[azure](https://github.com/kwame-mintah/python-fastapi-azure-k8s-cluster) etc.

[![Open in Cloud Shell][shell_img]][shell_link]

[shell_img]: http://gstatic.com/cloudssh/images/open-btn.png
[shell_link]: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/kwame-mintah/gcp-app-engine-python-fastapi-static-app&page=editor&open_in_editor=README.md

This repository is intended as a quick-start for deploying to App Engine:

- A [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=python) containing runtime information,
- GitHub Action workflow to run linting, unit tests and create a zip file,
- Pre-commit hooks to run on each commit.

## Usage

1. Install python packages used for the service

    ```console
   pip install -r requirements.txt
    ```
2. Run the FastAPI server, which will run on port 8000

    ```console
   python app/main.py
    ```

   Alternatively, if you're within your [virtual environment]:
   ```console
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
Endpoint documentation are available on http://127.0.0.1:8000/docs

## Docker

Running the `docker-compose.yml`, will build a new image python-fastapi-bigger-applications-template-fastapi:latest
which will be used for the `fastapi` service within the container.

```console
docker-compose up -d
```

## Tests

Unit tests are located in `/tests/unit` directory, run unit tests using:

```console
pytest tests/unit
```

Additionally, a coverage report can be generated using [`pytest-cov`](https://pypi.org/project/pytest-cov/):

```console
pytest --cov=app tests/unit --cov-report=html:coverage_report
```

Will generate a coverage HTML file, in the `/coverage_report/` directory, simply open the `index.html` in your chosen
web browser.

Integration tests are located in `/tests/integration` directory, run integration using:

```console
pytest tests/integration
```

## Contributing

Git hook scripts are very helpful for identifying simple issues before pushing any changes.
Hooks will run on every commit automatically pointing out issues in the code e.g. trailing whitespace.

To help with the maintenance of these hooks, [pre-commit](https://pre-commit.com/) is used, along
with [pre-commit-hooks](https://pre-commit.com/#adding-pre-commit-plugins-to-your-project).

Please following [these instructions](https://pre-commit.com/#install) to install `pre-commit` locally and ensure that
you have run
`pre-commit install` to install the hooks for this project.

Additionally, once installed, the hooks can be updated to the latest available version with `pre-commit autoupdate`.

## GitHub Actions (CI/CD)

GitHub project has three workflow set up, found in `.github/workflows/`:

- '🧹 Run linter' (`run-linter.yml`): To run [Flake8](https://flake8.pycqa.org/en/latest/) and check Python code system
  and comply with various style guides.
- '🧪 Run unit tests' (`run-unit-tests.yml`): To run unit tests within a continuous integration (CI) environment,
  using [`pytest`](https://docs.pytest.org/en/8.2.x/).
