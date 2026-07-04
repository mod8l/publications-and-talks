.PHONY: index lint

index:
	python3 scripts/generate-index.py

lint:
	@if command -v markdownlint >/dev/null 2>&1; then \
		markdownlint "**/*.md"; \
	elif command -v markdownlint-cli2 >/dev/null 2>&1; then \
		markdownlint-cli2 "**/*.md"; \
	else \
		echo "markdownlint not installed; skipping lint"; \
		exit 0; \
	fi
