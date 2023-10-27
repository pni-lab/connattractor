ARG BASE_CONTAINER=jupyter/scipy-notebook:python-3.10.8
FROM $BASE_CONTAINER

LABEL author="Tamas Spisak"

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root
#RUN apt-get update && \
#    apt-get install -y datalad
RUN mkdir /mounted
RUN chown -R ${NB_UID}:${NB_GID} /mounted

USER ${NB_UID}
RUN git config --global --add user.name connatractor
RUN git config --global --add user.email connatractor@noaddres.com
COPY --chown=${NB_UID}:${NB_GID} requirements.txt ${HOME}/requirements.txt
RUN pip install -r ${HOME}/requirements.txt
#RUN mkdir ${HOME}/.ssh
#RUN ssh-keyscan -t rsa github.com >> ${HOME}/.ssh/known_hosts
#COPY --chown=${NB_UID}:${NB_GID} *.ipynb ${HOME}/bwas/

WORKDIR /mounted
# to start:
# docker run -it -v $PWD:/mounted/connattractor -p 8080:8080 -p 8888:8888 pnilab/connattractor:latest jupyter notebook