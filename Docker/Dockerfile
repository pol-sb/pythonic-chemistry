FROM python:3.10.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    bash \
    curl \
    wget \
    xz-utils \
    gcc \
    g++ \
    gfortran \
    cmake \
    make \
    libopenblas-dev \
    liblapack-dev \
    libxrender1 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install Python packages
RUN pip install --no-cache-dir \
    ipython \
    ipykernel \
    numpy \
    pandas \
    matplotlib \
    seaborn \
    ase \
    pymatgen \
    scikit-learn \
    rdkit \
    xtb \
    jupyter-jsmol

# Install xtb-related packages
RUN pip install --no-cache-dir xtb-python || echo "xtb-python installation failed, skipping"

# Install autode
RUN git clone https://github.com/duartegroup/autodE.git /tmp/autodE && \
    cd /tmp/autodE && \
    pip install --no-cache-dir . && \
    cd / && \
    rm -rf /tmp/autodE

# Set unlimited stack size
RUN echo "ulimit -s unlimited" >> /etc/bash.bashrc

# Verify python is accessible
RUN python --version && pip --version
