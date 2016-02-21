PLATFORM = $(shell uname)


PYTHON_MODULES=pynes_stdlib


WGET = wget -q 

OK=\033[32m[OK]\033[39m
FAIL=\033[31m[FAIL]\033[39m
CHECK=@if [ $$? -eq 0 ]; then echo "${OK}"; else echo "${FAIL}" ; fi

default: python.mk
	@$(MAKE) -C . test

ifeq "true" "${shell test -f python.mk && echo true}"
include python.mk
endif

python.mk:
	@${WGET} https://raw.githubusercontent.com/gutomaia/makery/master/python.mk && \
		touch $@

clean: python_clean

purge: python_purge
	@rm python.mk
	@rm -rf .tox

build: python_build

test: python_build ${REQUIREMENTS_TEST}
	${VIRTUALENV} nosetests --processes=4

doctest: python_build ${REQUIREMENTS_TEST}
	${VIRTUALENV} $(MAKE) -C docs doctest

ci: doctest
	${VIRTUALENV} CI=1 nosetests

pep8: ${REQUIREMENTS_TEST}
	${VIRTUALENV} pep8 --statistics -qq pynes | sort -rn || echo ''

todo:
	${VIRTUALENV} pep8 --first pynes
	find pynes -type f | xargs -I [] grep -H TODO []

search:
	find pynes -regex .*\.py$ | xargs -I [] egrep -H -n 'print|ipdb' [] || echo ''

report:
	coverage run --source=pynes setup.py test

tdd:
	${VIRTUALENV} tdaemon --ignore-dirs="build,dist,bin,site,pynes.egg-info,venv" --custom-args="--with-notify --no-start-message"

tox:
	${VIRTUALENV} tox

register:
	${VIRTUALENV} python setup.py register -r pypi

distribute: dist
	${VIRTUALENV} python setup.py sdist bdist_wheel upload -r pypi

docs:
	@${VIRTUALENV} $(MAKE) -C docs html

.PHONY: clean linux windows dist nsis installer run report docs ghpages
