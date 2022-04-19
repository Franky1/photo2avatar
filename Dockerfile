# this Dockerfile mimics the streamlit cloud runtime
FROM python:3.7-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=120 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

# build tools
RUN apt-get update \
    && apt-get install --yes --no-install-recommends \
    gcc \
    g++ \
    build-essential \
    python3-dev

WORKDIR /app

# if we have a packages.txt, install it
COPY packages.txt packages.txt
RUN xargs -a packages.txt apt-get install --yes

# update python tools
RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade setuptools wheel

# install python packages
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8501

COPY . .

CMD ["streamlit", "run", "app.py"]
# CMD streamlit run --server.port 8080 --server.address=0.0.0.0 --server.enableCORS false app.py

# docker build --progress=plain --tag photo2avatar:latest .
# docker run -ti -p 8501:8501 --rm photo2avatar:latest /bin/bash
# docker run -ti -p 8501:8501 --rm photo2avatar:latest
# docker run -ti -p 8501:8501 -v ${pwd}:/app --rm photo2avatar:latest
# docker run -ti -p 8501:8501 -v ${pwd}:/app --rm photo2avatar:latest /bin/bash