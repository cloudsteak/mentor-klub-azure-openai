# Környezeti változók sablonfájl létrehozása és inicializálása
# Ez a Makefile a Python projekt fejlesztői környezetének kezelését segíti.
# Tartalmaz célokat a virtuális környezet létrehozására (Mac, Linux, Windows), aktiválására, követelmények telepítésére,
# pip frissítésére, .env fájl létrehozására, valamint a Python verzió ellenőrzésére.
# Használat: make <cél>
# Elérhető célok: venv-mac, venv-linux, venv-win, activate-mac, activate-linux, activate-win, deactivate, env, install, upgrade-pip, python-version, all

.PHONY: env

# Virtuális környezet létrehozása Mac/Linux rendszeren
venv-mac:
	python3 -m venv venv

# Virtuális környezet létrehozása Linux rendszeren
venv-linux:
	python3 -m venv venv

# Virtuális környezet létrehozása Windows rendszeren
venv-win:
	python -m venv venv

# Virtuális környezet aktiválása Mac/Linux rendszeren
activate-mac:
	@echo "Futtasd: source venv/bin/activate"

# Virtuális környezet aktiválása Linux rendszeren
activate-linux:
	@echo "Futtasd: source venv/bin/activate"

# Virtuális környezet aktiválása Windows rendszeren
activate-win:
	@echo "Futtasd: venv\\Scripts\\activate"

# Virtuális környezet deaktiválása (mindkét platformon)
deactivate:
	@echo "Futtasd: deactivate"

# .env fájl létrehozása példa alapján
env:
	mv -f example.env .env

# Követelmények telepítése
install:
	pip install -r requirements.txt

# pip frissítése
upgrade-pip:
	python -m pip install --upgrade pip

# Python verzió kiírása
python-version:
	python --version

# Parancssori alkalmazás indítása
run:
	python parancssor.py

reset-all:
	rm -f .env
	rm -rf venv
	@echo "Törölve: .env fájl és venv könyvtár"
	echo 'AZURE_OPENAI_ENDPOINT=https://<ai-studio-neve>.openai.azure.com/' > example.env
	echo 'AZURE_OPENAI_API_KEY=<AZURE_OPENAI_KEY>' >> example.env
	echo 'AZURE_OPENAI_DEPLOYMENT=<Üzemelő példány neve>   # pl. gpt-4o' >> example.env
	echo 'AZURE_OPENAI_API_VERSION=2024-12-01-preview' >> example.env
	@echo "Létrehozva: example.env fájl"
	@echo "Kérlek, töltsd ki a example.env fájlt a megfelelő értékekkel."
	@echo "Majd futtasd a make env parancsot a .env fájl létrehozásához."
	


# Minden lépés futtatása
all: env upgrade-pip install python-version
