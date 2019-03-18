PROJECT = repy
FNAME = repy


.PHONY: init lint test clean mypy

init: ;
# 	conda env create -f conda_packages.yml

clean:
	find . -name '*.py[oc]' -delete
	rm -r tests/__pycache__

mypy:
	mypy $(FNAME)

lint:
	flake8 $(FNAME)

test:
	nosetests

all_checks: mypy lint test ;

release_major:
	repy Major

release_minor:
	repy Minor

release_patch:
	repy Patch
