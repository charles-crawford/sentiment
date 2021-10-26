FROM python:3.6
COPY . app/
WORKDIR app/
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["/usr/local/bin/waitress-serve","--listen=*:5000","--threads=12","--backlog=2048","--url-scheme=http","wsgi:app"]