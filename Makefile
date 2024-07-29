CONFIG := $(abspath .xsdata.xml)


gen_classes:
	cd src && xsdata generate -c $(CONFIG) -p greenbutton_objects.data.espi https://www.naesb.org/espi.xsd
	cd src && xsdata generate -c $(CONFIG) -p greenbutton_objects.data.atom https://greenbuttondata.org/xsd/3_3/atom.xsd

lint:
	pre-commit run -a
	nox -s mypy

gen_examples:
	python .\tests\test_rules_engine\generate_example_data.py

test:
	nox -s tests-3.12

build:
	pip install -q build
	python -m build

all: lint gen_examples test build
