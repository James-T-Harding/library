sudo apt update && sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
chmod +x venv/bin/activate
./venv/bin/activate
pip install -r requirements.txt
python3 -m pytest --cov=applications
pydoc -w applications applications.book applications.app
python3 -m pydoc -w applications applications.book applications.app