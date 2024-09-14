[![Dotproduct](https://github.com/nogibjj/skye-assignment-1/actions/workflows/action.yml/badge.svg)](https://github.com/nogibjj/skye-assignment-1/actions/workflows/action.yml)

# DotProduct Calculation

This project computes the dot product of two vectors using a Python script. The project is integrated with GitHub Actions for continuous integration.

## Usage

To calculate the dot product of two vectors:

```bash
python3 dotp.py [vector_x] [vector_y]
```

Example:


```bash
python3 dotp.py [1,2,3] [4,5,6]
```

Output:

```bash
dot product result is 32.
```

## GitHub Actions Workflow

The workflow is triggered on push, pull request, and manual events to the master branch. It performs the following steps:

Setup: `make setup`
Lint: `make lint`
Test: `make test`
Run: `make run`

# Requirements

- [x] python project skeleton.
- [x] devcontainer with devcontainer.json and Dockerfile
- [x] Makefile with setup, test, and lint
- [x] README.md with setup and usage instructions