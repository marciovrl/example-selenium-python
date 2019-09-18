all: help

.PHONY: help
help:
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

.PHONY: install-dependencies
install-dependencies: ## Installs project dependencies.
	pip install -q -r requirements.txt

.PHONY: run-test
run-test: ## Execute the tests. Do not forget to pass the ENV_BROWSER parameter, eg env_browser = chrome_headless.
	behave -f allure -o ./report-allure/result -D env_browser="$(browser)"

.PHONY: generate-allure
generate-allure: ## Build report Allure.
	allure serve report-allure/result/

.PHONY: test
test: ## Total execution: Install dependencies, run tests, and report to Allure.
	install-dependencies run-test generate-allure