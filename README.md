# connattractor

[![GitHub license](https://img.shields.io/github/license/pnilab/connattractor.svg)](https://github.com/pni-lab/connattractor/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/release/pni-lab/connattractor.svg)](https://github.com/pni-lab/connattractor/releases/)
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/pnilab/connattractor?color=blue&label=pnilab%2Fconnattractor%3A&logo=docker&sort=semver)](https://hub.docker.com/repository/docker/pnilab/connattractor)
![Docker Image Size (latest semver)](https://img.shields.io/docker/image-size/pnilab/connattractor?label=%20pnilab%2Fconnattractor&logo=docker&sort=semver)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pni-lab/connattractor/HEAD)

Laboratory for Predictive Neuroimaging - University Hospital Essen, Germany

## Webpage and manuscript and getting started guide
[pni-lab.github.io/connattractor](pni-lab.github.io/connattractor)

## How to install the connattractor package?

*TODO*

```bash
pip install connattractor
```

## How to re-run the analyses?

- **Run the analyses with 1 click (in the cloud)**
  - [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pni-lab/connattractor/HEAD)
  - Open in GitHub Codespaces (click `code` on top right on the github page of the repo)

- **Set up everything to run in 5 mins (locally on your computer)**
  - install [docker](https://www.docker.com/)
  - clone the repo and start your notebook in a docker container
    ```bash
    git clone https://github.com/pni-lab/connattractor.git
    cd connattractor
    docker run -it -v $PWD:/mounted/connattractor -p 8080:8080 -p 8888:8888 pnilab/connattractor:latest jupyter notebook
    ```
  - copy paste the last link in your browser to start the notebook

 - **Bare-metal** (developers)
  - clone this repository with git as above
  - set up a python environment (e.g with conda)
  - install all requirements from requirements.txt
  - start developing

## How to render the web-page locally?
```bash
cd docs
myst start
```
