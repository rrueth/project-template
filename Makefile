ENV=env

init: $(ENV)/bin/activate

$(ENV)/bin/activate:
 	test -d $(ENV) || virtualenv $(ENV) --python=python3.5
 	$(ENV)/bin/pip install -Ur requirements.txt

test: $(ENV)/bin/activate
	$(ENV)/bin/tox

lint: $(ENV)/bin/activate
	$(ENV)/bin/pylint --rcfile=.pylintrc

clean:
	rm -rf $(ENV) .tox dist sdist *.egg-info
	# Silence 'No such file or directory' warnings by using '|| true'
	find . -name "__pycache__" -exec rm -rf {} \; || true
	find . -name "*.pyc" -exec rm -r {} \;
