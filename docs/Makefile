# ===== Makefile (à placer dans docs/) =====
SPHINXBUILD ?= sphinx-build
AUTOBUILD   ?= sphinx-autobuild
HOST        ?= 0.0.0.0

# Ports par défaut
PORT ?= 8000

# Ignore patterns pour éviter les boucles
IGNORE = --ignore "**/_build/**" --ignore "**/.git/**" --ignore "**/__pycache__/**"


.PHONY: help clean build master live-master

help:
	@echo "Cibles:"
	@echo "  make master     -> build statique une fois"
	@echo "  make live-master             -> live-reload sur $(HOST):$(PORT)"
	@echo "Variables override: HOST=0.0.0.0 PORT=9000 ..."

# Builds "one-shot"
master:
	$(SPHINXBUILD) ./ _build/html

build: master

clean:
	rm -rf _build

# Live reload (un watcher par projet)
live-master:
	$(AUTOBUILD) --host $(HOST) --port $(PORT) $(IGNORE) ./ _build/html
