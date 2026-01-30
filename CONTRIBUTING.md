# Contributing

Thanks for your interest in contributing to this project! This document explains the process for contributing, how to run tests, and coding standards.

## How to contribute

1. Fork the repository and create a branch (feature/my-change).
2. Write clear, small commits and a descriptive PR title and description.
3. Add or update tests for new functionality.
4. Run the tests locally and make sure linting passes.
5. Open a Pull Request and reference any related issues.

## Code style

- Follow PEP8 and use `flake8` to check linting.
- Keep functions small and add docstrings + type hints where reasonable.
- Avoid starting a Spark session during module import; use factory functions so tests can import modules without side effects.

## Tests

- Run tests with `pytest`.
- Add unit tests for any new logic.

## CI

This repo uses GitHub Actions to run linting and tests on push and PRs.

## Communication

- Be respectful and clear.
- If your PR is larger, open an issue first to discuss design choices.
