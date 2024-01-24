FROM python:3.11.4

ARG DEBIAN_FRONTEND=noninteractive

ENV PYTHONUNBUFFERED=1

RUN mkdir /sd-webui

WORKDIR sd-webui

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

#RUN pip install -U git+https://github.com/huggingface/transformers.git
#RUN pip install --no-cache-dir diffusers transformers accelerate scipy safetensors omegaconf
#RUN pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118

#RUN pip install --upgrade --no-cache-dir diffusers[torch]

#RUN pip install --no-cache-dir omegaconf

COPY . .

RUN chmod a+x deploy/*.sh

# WORKDIR src

# CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000