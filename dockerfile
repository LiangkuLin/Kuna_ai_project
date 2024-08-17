FROM public.ecr.aws/docker/library/python:3.8

WORKDIR /app

# Install conda
RUN apt-get update && apt-get install -y wget bzip2 \
    && wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -b -p /opt/miniconda \
    && rm /tmp/miniconda.sh

ENV PATH="/opt/miniconda/bin:$PATH"

# insall dependencies
COPY conda/env.yaml /app

RUN conda env create -f env.yaml

RUN conda init 

# go into shell
SHELL ["conda", "run", "-n", "env", "/bin/bash", "-c"]

# put whole proj into docker 
COPY . /app

EXPOSE 8080

CMD ["conda", "run", "--no-capture-output", "-n", "env", "waitress-serve", "--port=8080", "application:app"]