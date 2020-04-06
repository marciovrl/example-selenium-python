all: help

.PHONY: help
help:
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

.PHONY: pip
pip: ## Installs project dependencies.
	pip install -q -r requirements.txt

.PHONY: test
test: ## Execute the tests. Do not forget to pass the BROWSER parameter, eg browser = chrome_headless.
	behave -D env_browser="$(browser)"