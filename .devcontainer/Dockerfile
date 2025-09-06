# Devcontainer for CLASS (xi_interact patch) + Cobaya + GetDist (+ MontePython optional)
FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1

# System deps
RUN apt-get update && apt-get install -y \
    gfortran make git wget curl build-essential ca-certificates cmake pkg-config \
    python3-dev \
    libcfitsio-dev \
    libfftw3-dev \
    libopenblas-dev liblapack-dev \
    gnuplot \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip

RUN pip install numpy scipy matplotlib getdist cobaya jupyter ipykernel setuptools wheel mpi4py

RUN export COBAYA_PACKAGES_PATH=/opt/cobaya_pkgs && \
    cobaya-install -p /opt/cobaya_pkgs \
    planck_2018_lowl.TT planck_2018_lowl.EE \
    planck_2018_highl_plik.TTTEEE_lite_native \
    planck_2018_lensing.native \
    bao.sdss_dr12_consensus_final \
    sn.pantheon

    
# Python sphinx deps
RUN pip install sphinx sphinx-rtd-theme sphinxcontrib-bibtex myst-parser sphinx-autobuild sphinxcontrib-mermaid sphinxcontrib-datatemplates pyyaml --root-user-action=ignore

# Class Clone repo
RUN git clone https://github.com/lesgourg/class_public.git /opt/class_public 

# Python Class install
RUN python -m pip install /opt/class_public

# Dossier de travail par défaut = racine des workspaces
WORKDIR /workspace

CMD ["/bin/bash"]