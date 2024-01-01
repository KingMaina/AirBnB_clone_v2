FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update && \
	    apt-get install -y \
	    libffi-dev \
	    libssl-dev \
	    build-essential \
	    python3.4.0 \
	    python3.4-dev \
	    libpython3-dev

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

RUN apt-get autoremove -y && \
	    apt-get clean && \
	    rm -rf /var/lib/apt/lists/*

CMD ["python3"]
