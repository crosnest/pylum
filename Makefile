COSMOS_SDK_URL := https://github.com/cosmos/cosmos-sdk
COSMOS_SDK_VERSION := v0.46.13
COSMOS_SDK_DIR := build/cosmos-sdk-proto-schema

IBCGO_URL := https://github.com/cosmos/ibc-go
IBCGO_VERSION := v5.2.1
IBCGO_DIR := build/ibcgo-proto-schema

CHAIN_URL := https://github.com/lum-network/chain
CHAIN_VERSION := v1.4.5
CHAIN_DIR := build/chain-proto-schema

PYLUM_PROTOS_DIR := pylum/protos
PYLUM_SRC_DIR := pylum
PYLUM_TESTS_DIR := tests
PYLUM_EXAMPLES_DIR := examples
PYLUM_SCRIPTS_DIR := scripts

PROTO_THIRDPARTY_URL := https://github.com/regen-network/protobuf
PROTO_THIRDPARTY_VERSION := v1.3.2-alpha.regen.4
PROTO_THIRDPARTY_DIR := build/gogoproto-proto-schema

COSMOS_PROTO_URL := https://github.com/cosmos/cosmos-proto
COSMOS_PROTO_VERSION := v1.0.0-alpha8
COSMOS_PROTO_DIR := build/cosmos-proto-schema

GOOGLEAPI_PROTO_URL := https://github.com/googleapis/googleapis.git
GOOGLEAPI_PROTO_VERSION := common-protos-1_3_1
GOOGLEAPI_PROTO_DIR := build/googleapi-proto-schema

ICS23_PROTO_URL := https://github.com/confio/ics23
ICS23_PROTO_VERSION := v0.9.0
ICS23_PROTOS_DIR := build/ics23_proto-schema


PYTHON_CODE_DIRS := $(PYLUM_SRC_DIR) $(PYLUM_TESTS_DIR) $(PYLUM_EXAMPLES_DIR) $(PYLUM_SCRIPTS_DIR)

########################################
### Initialise dev environment
########################################

# Create a new poetry virtual environment with all the necessary dependencies installed.
# Once finished, `poetry shell` to enter the virtual environment
v := $(shell pip -V | grep virtualenvs)

.PHONY: new-env
new-env: clean
	if [ -z "$v" ];\
	then\
		poetry install --with main,dev,test,docs;\
		echo "Enter virtual environment with all development dependencies now: 'poetry shell'.";\
	else\
		echo "In a virtual environment! Exit first: 'exit'.";\
	fi

########################################
### Tests
########################################

# Run all tests
.PHONY: test
test:
	coverage run -m pytest $(PYLUM_TESTS_DIR) --doctest-modules
	$(MAKE) coverage-report

# Run all unit tests
.PHONY: unit-test
unit-test:
	coverage run -m pytest $(PYLUM_TESTS_DIR) --doctest-modules -m "not integration"

# Run all integration tests
.PHONY: integration-test
integration-test:
	coverage run -m pytest $(PYLUM_TESTS_DIR) --doctest-modules -m "integration"

# Produce the coverage report. Can see a report summary on the terminal.
# Detailed report on all modules are placed under /coverage-report
.PHONY: coverage-report
coverage-report:
	coverage report -m
	coverage html

########################################
### Code Styling
########################################

# Automatically run black and isort to format the code, and run flake8 and vulture checks
.PHONY: lint
lint: black isort flake8 vulture

# Automatically format the code using black
.PHONY: black
black:
	black $(PYTHON_CODE_DIRS) --exclude $(PYLUM_PROTOS_DIR)

# Automatically sort the imports
.PHONY: isort
isort:
	isort $(PYTHON_CODE_DIRS)

# Check the code format
.PHONY: black-check
black-check:
	black --check --verbose $(PYTHON_CODE_DIRS) --exclude $(PYLUM_PROTOS_DIR)

# Check the imports are sorted
.PHONY: isort-check
isort-check:
	isort --check-only --quiet --verbose $(PYTHON_CODE_DIRS)

# Run flake8 linter
.PHONY: flake8
flake8:
	flake8 $(PYTHON_CODE_DIRS)

# Check for unused code
.PHONY: vulture
vulture:
	vulture $(PYTHON_CODE_DIRS) scripts/whitelist.py --exclude '*_pb2.py,*_pb2_grpc.py' --min-confidence 100

########################################
### Security & safety checks
########################################

# Run bandit and safety
.PHONY: security
security: bandit safety

# Check the security of the code
.PHONY: bandit
bandit:
	bandit -r $(PYLUM_SRC_DIR) $(PYLUM_TESTS_DIR) -s B101
	bandit -r $(PYLUM_EXAMPLES_DIR) -s B101,B105

# Check the security of the code for known vulnerabilities
.PHONY: safety
safety:
	safety check -i 41002

########################################
### Linters
########################################

# Check types (statically) using mypy
.PHONY: mypy
mypy:
	mypy $(PYTHON_CODE_DIRS) --exclude $(PYLUM_PROTOS_DIR)

# Lint the code using pylint
.PHONY: pylint
pylint:
	pylint -j 0 $(PYTHON_CODE_DIRS)

########################################
### License and copyright checks
########################################

# Check dependency licenses
.PHONY: liccheck
liccheck:
	poetry export > tmp-requirements.txt
	liccheck -s strategy.ini -r tmp-requirements.txt -l PARANOID
	rm -frv tmp-requirements.txt

# Check that the relevant files have appropriate Copyright header
.PHONY: copyright-check
copyright-check:
	python scripts/check_copyright.py --directory .

########################################
### Docs
########################################

# Build documentation
.PHONY: docs
docs:
	mkdocs build --clean

# Live documentation server
.PHONY: docs-live
docs-live:
	mkdocs serve

# Generate API documentation (ensure you add the new pages created into /mkdocs.yml --> nav)
.PHONY: generate-api-docs
generate-api-docs:
	python3 scripts/generate_api_docs.py

########################################
### Poetry Lock
########################################

# Updates the poetry lock
poetry.lock: pyproject.toml
	poetry lock

########################################
### Clear the caches and temporary files
########################################

# clean the caches and temporary files and directories
.PHONY: clean
clean: clean-build clean-pyc clean-test clean-docs

.PHONY: clean-build
clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr pip-wheel-metadata
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

.PHONY: clean-docs
clean-docs:
	rm -fr site/

.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.DS_Store' -exec rm -fr {} +

.PHONY: clean-test
clean-test:
	rm -fr .tox/
	rm -f .coverage
	find . -name ".coverage*" -not -name ".coveragerc" -exec rm -fr "{}" \;
	rm -fr coverage.xml
	rm -fr htmlcov/
	rm -fr .hypothesis
	rm -fr .pytest_cache
	rm -fr .mypy_cache/
	find . -name 'log.txt' -exec rm -fr {} +
	find . -name 'log.*.txt' -exec rm -fr {} +

########################################
### Build
########################################

# Build the project
.PHONY: dist
dist: clean
	poetry build

########################################
### Generate protos and grpc files
########################################

ifeq ($(OS),Windows_NT)
	$(error "Please use the WSL (Windows Subsystem for Linux) on Windows platform.")
else
    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Linux)
		OPEN_CMD := xdg-open
    endif
    ifeq ($(UNAME_S),Darwin)
		OPEN_CMD := open
    endif
endif

define unique
  $(eval seen :=)
  $(foreach _,$1,$(if $(filter $_,${seen}),,$(eval seen += $_)))
  ${seen}
endef
unique = $(if $1,$(firstword $1) $(call unique,$(filter-out $(firstword $1),$1)))

proto: fetch_proto_schema_source generate_proto_types generate_init_py_files

generate_proto_types: download_sources apply_third_party
	rm -frv $(PYLUM_PROTOS_DIR)/*
	python3 -m grpc_tools.protoc --proto_path=$(IBCGO_DIR)/proto --proto_path=$(IBCGO_DIR)/third_party/proto --python_out=$(PYLUM_PROTOS_DIR) --grpc_python_out=$(PYLUM_PROTOS_DIR) $(shell find $(IBCGO_DIR) \( -path */proto/* -or -path */third_party/proto/* \) -type f -name *.proto)
# ensure cosmos-sdk is last as previous modules may have duplicated proto models which are now outdated
#	python3 -m grpc_tools.protoc --proto_path=$(COSMOS_SDK_DIR)/proto --proto_path=$(COSMOS_SDK_DIR)/third_party/proto --python_betterproto_out=$(PYLUM_PROTOS_DIR) $(shell find $(COSMOS_SDK_DIR) \( -not -path */nft/* \) \( -path */proto/* -or -path */third_party/proto/* \) -type f -name *.proto)
#	find $(COSMOS_SDK_DIR) \( -path */proto/* -or -path */third_party/proto/* \) -type f -name *.proto -exec python3 -m grpc_tools.protoc --proto_path=$(COSMOS_SDK_DIR)/proto --proto_path=$(COSMOS_SDK_DIR)/third_party/proto --python_betterproto_out=$(PYLUM_PROTOS_DIR)  {} \;
	# other chains modules
	python3 -m grpc_tools.protoc --proto_path=$(COSMOS_SDK_DIR)/proto --proto_path=$(COSMOS_SDK_DIR)/third_party/proto --proto_path=$(CHAIN_DIR)/proto \
	--python_out=$(PYLUM_PROTOS_DIR) --grpc_python_out=$(PYLUM_PROTOS_DIR) \
	$(shell find $(CHAIN_DIR) $(COSMOS_SDK_DIR) \( -path */proto/* -or -path */third_party/proto/* \) -type f -name *.proto)

fetch_proto_schema_source: $(COSMOS_SDK_DIR) $(IBCGO_DIR) $(CHAIN_DIR)

.PHONY: generate_init_py_files
generate_init_py_files: generate_proto_types
    # restore __init__.py files if missing
	find $(PYLUM_PROTOS_DIR)/ -type d -exec sh -c 'test -e "'{}'/__init__.py" || touch "'{}'/__init__.py"' \;
# restore root __init__.py as it contains code to have the proto files module available
	git restore $(PYLUM_PROTOS_DIR)/__init__.py

$(SOURCE): $(COSMOS_SDK_DIR)

$(GENERATED): $(SOURCE)
	$(COMPILE_PROTOBUFS_COMMAND)

$(INIT_PY_FILES_TO_CREATE): $(GENERATED_DIRS)
	touch $(INIT_PY_FILES_TO_CREATE)

download_sources:
	echo "download sources"
	make $(COSMOS_SDK_DIR) $(ICS23_DIR) $(IBCGO_DIR) $(CHAIN_DIR)

apply_third_party:
	echo "apply third_party"
	make $(PROTO_THIRDPARTY_DIR) $(COSMOS_PROTO_DIR) $(GOOGLEAPI_PROTO_DIR) $(ICS23_PROTO_DIR)

$(GENERATED_DIRS): $(COSMOS_SDK_DIR) $(IBCGO_DIR) $(CHAIN_DIR)

$(GOOGLEAPI_PROTO_DIR): Makefile
	rm -rf $(GOOGLEAPI_PROTO_DIR)
	git clone --branch $(GOOGLEAPI_PROTO_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(GOOGLEAPI_PROTO_URL) $(GOOGLEAPI_PROTO_DIR)
	cd $(GOOGLEAPI_PROTO_DIR) && git checkout $(GOOGLEAPI_PROTO_VERSION) -- $(GOOGLEAPI_PROTO_RELATIVE_DIRS)
	mkdir -p $(COSMOS_SDK_DIR)/third_party/proto/google/api/
	cp -a $(GOOGLEAPI_PROTO_DIR)/google/api/annotations.proto $(GOOGLEAPI_PROTO_DIR)/google/api/http.proto $(COSMOS_SDK_DIR)/third_party/proto/google/api/

$(COSMOS_PROTO_DIR): Makefile
	rm -rf $(COSMOS_PROTO_DIR)
	git clone --branch $(COSMOS_PROTO_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(COSMOS_PROTO_URL) $(COSMOS_PROTO_DIR)
	cd $(COSMOS_PROTO_DIR) && git checkout $(COSMOS_PROTO_VERSION) -- $(COSMOS_PROTO_RELATIVE_DIRS)
	mkdir -p $(COSMOS_SDK_DIR)/third_party/proto/cosmos_proto
	find ${COSMOS_PROTO_DIR}/proto/cosmos_proto -type f -name "*.proto" -exec cp {} $(COSMOS_SDK_DIR)/third_party/proto/cosmos_proto \;

$(PROTO_THIRDPARTY_DIR): Makefile
	rm -rf $(PROTO_THIRDPARTY_DIR)
	git clone --branch $(PROTO_THIRDPARTY_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(PROTO_THIRDPARTY_URL) $(PROTO_THIRDPARTY_DIR)
	cd $(PROTO_THIRDPARTY_DIR) && git checkout $(PROTO_THIRDPARTY_VERSION) -- $(PROTO_THIRDPARTY_RELATIVE_DIRS)
	mkdir -p $(COSMOS_SDK_DIR)/third_party/proto/gogoproto
	find ${PROTO_THIRDPARTY_DIR}/gogoproto -type f -name "*.proto" -exec cp {} $(COSMOS_SDK_DIR)/third_party/proto/gogoproto \;
	mkdir -p $(COSMOS_SDK_DIR)/third_party/proto/google/protobuf
	find ${PROTO_THIRDPARTY_DIR}/protobuf -type f -name "*.proto" -exec cp {} $(COSMOS_SDK_DIR)/third_party/proto/google/protobuf \;

$(ICS23_PROTO_DIR): Makefile
	rm -rf $(ICS23_PROTO_DIR)
	git clone --branch $(ICS23_PROTO_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(ICS23_PROTO_URL) $(ICS23_PROTO_DIR)
	cd $(ICS23_PROTO_DIR) && git checkout $(ICS23_PROTO_VERSION) -- $(ICS23_PROTO_RELATIVE_DIRS)
	mkdir -p $(COSMOS_SDK_DIR)/third_party/proto/confio
	cp -a $(ICS23_PROTO_DIR)/proofs.proto $(COSMOS_SDK_DIR)/third_party/proto/confio/

$(COSMOS_SDK_DIR): Makefile
	rm -rf $(COSMOS_SDK_DIR)
	git clone --branch $(COSMOS_SDK_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(COSMOS_SDK_URL) $(COSMOS_SDK_DIR)
	cd $(COSMOS_SDK_DIR) && git checkout $(COSMOS_SDK_VERSION) -- $(COSMOS_PROTO_RELATIVE_DIRS)
	rm -rf $(COSMOS_SDK_DIR)/third_party/proto


$(IBCGO_DIR): Makefile
	rm -rf $(IBCGO_DIR)
	git clone --branch $(IBCGO_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(IBCGO_URL) $(IBCGO_DIR)
	cd $(IBCGO_DIR) && git checkout $(IBCGO_VERSION) -- $(IBCGO_PROTO_RELATIVE_DIRS)

$(CHAIN_DIR): Makefile
	rm -rf $(CHAIN_DIR)
	git clone --branch $(CHAIN_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(CHAIN_URL) $(CHAIN_DIR)
	cd $(CHAIN_DIR) && git checkout $(CHAIN_VERSION) -- $(CHAIN_PROTO_RELATIVE_DIRS)
	rm -rf $(CHAIN_DIR)/third_party/proto

debug:
	$(info SOURCES_REGEX_TO_EXCLUDE: $(SOURCES_REGEX_TO_EXCLUDE))
	$(info  )
	$(info GENERATED_DIRS: $(GENERATED_DIRS))
	$(info  )
	$(info INIT_PY_FILES_TO_CREATE: $(INIT_PY_FILES_TO_CREATE))
	$(info  )
	$(info SOURCE: $(SOURCE))
	$(info  )
	$(info RELATIVE_SOURCE: $(RELATIVE_SOURCE))
	$(info  )
	$(info GENERATED: $(GENERATED))
	$(info  )
	$(info UNROOTED_SOURCE: $(UNROOTED_SOURCE))
	$(info  )
	$(info PROTO_ROOT_DIRS: $(PROTO_ROOT_DIRS))
	$(info  )
	$(info FIND_CMD: $(FIND_CMD))
	$(info  )
	$(info COMPILE_PROTOBUFS_COMMAND: $(COMPILE_PROTOBUFS_COMMAND))

########################################
### Commands used by CI workflows
########################################

# Live documentation server
.PHONY: docs-live-ci
docs-live-ci:
	mkdocs serve -a localhost:8080

# Produce the coverage report
.PHONY: coverage-report-ci
coverage-report-ci:
	coverage report -m -i

# Check MANIFEST.in file for completeness
.PHONY: check-manifest-ci
check-manifest-ci:
	check-manifest

# Check API documentation is up-to-date
.PHONY: check-api-docs-ci
check-api-docs-ci:
	python scripts/generate_api_docs.py --check-clean

checkout-chain-sources: Makefile
	git clone --branch $(CHAIN_VERSION) --depth 1 --quiet --no-checkout --filter=blob:none $(CHAIN_URL) chain4energy-chain
	cd chain4energy-chain && git checkout $(CHAIN_VERSION) -- $(CHAIN_PROTO_RELATIVE_DIRS)

run-service-docker:
	docker build  --build-arg VERSION=$(CHAIN_VERSION) --build-arg REPOSITORY=$(CHAIN_URL) -t c4echain_serve ./scripts/
	docker run --name testchain -v $(PWD):/test -d -p 1317:1317 -p 4500:4500 -p 26657:26657 -t --rm c4echain_serve chain serve --skip-proto

test-docker: run-service-docker
	# install depends
	docker exec testchain bash -c "apt-get update && apt-get install -y python3-pip"
	docker exec testchain bash -c "pip install tox==3.25.1 poetry"
	# wait for service running
	@echo "Waiting for health check..."
	@until HEALTH=$$(docker exec testchain curl -sv localhost:26657/health); \
	do \
		sleep 1; \
	done
	# call test execution
	docker exec testchain bash -c "cd /test && tox -e test-integration"

stop-service-docker:
	docker stop testchain