dev-setup:
	pip install -r requirements.txt

build:
	pyinstaller json2csv.py --onefile --noconsole
