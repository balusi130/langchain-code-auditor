# Changelog

## [1.1.0] - 2026-04-10
### Added
- Correlated subquery detection agent
- `.gitignore` for Python projects

## [1.0.1] - 2026-03-22
### Fixed
- Style agent crashing on files with Windows line endings (CRLF)
- Security agent false positive on commented-out credential lines

## [1.0.0] - 2026-03-01
### Added
- Initial release with complexity, security, and style agents
- CLI entry point with `--file` and `--dir` flags
- Unit tests for all three agents
- requirements.txt and README
