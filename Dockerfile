FROM rocker/r-ver:4.3.1

RUN apt-get update && apt-get install -y   libxml2-dev libcurl4-openssl-dev libssl-dev libpoppler-cpp-dev   tesseract-ocr libtesseract-dev   && R -e "install.packages(c('plumber', 'readr', 'readxl', 'pdftools', 'tesseract', 'ggplot2', 'rmarkdown', 'dplyr', 'base64enc'))"

COPY . /app
WORKDIR /app
CMD ["Rscript", "main.R"]
