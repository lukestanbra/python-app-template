
SYSTEM_PYTHON=/usr/bin/python3
SHELL=/bin/bash
.DEFAULT_GOAL=help

venv: ## Creates the virtual environment for testing
	@test -d .venv || ${SYSTEM_PYTHON} -m venv .venv
	@.venv/bin/pip3 install -r test-requirements.txt
	@.venv/bin/pip3 install -r requirements.txt

lint: ## Run pylint against the package source
	@.venv/bin/pylint src/

test: lint test-install ## Run the tests
	@.venv/bin/pytest --cache-clear -v --cov=src/ tests/

test-install: ## Install the package into the virtual environment for testing
	@.venv/bin/python3 ./setup.py --quiet --no-user-cfg install

clean: ## Deletes the virtual environment
	@rm -rf .venv

help: ## Display this help
	@{ echo "Option%Description"; grep "##" Makefile | sed -En "s/^([^:]*):.*\#\# *(.*)$$/$$(tput setaf 2)\1$$(tput sgr0)%\2/p"; } | column -t -s %