FROM public.ecr.aws/docker/library/python:3.8

WORKDIR /app

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