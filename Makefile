venv-init:
	virtualenv --python python3 ~/.virtualenvs/env
	source ~/.virtualenvs/env/bin/activate
	pip install domovoi

venv:
	source ~/.virtualenvs/env/bin/activate
	
