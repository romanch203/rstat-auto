# plumber.R - API interface
library(plumber)
library(readr)
library(readxl)
library(pdftools)
library(tesseract)
library(ggplot2)
library(rmarkdown)

#* @post /analyze
#* @param file:file The input file
function(file) {
  temp_file <- tempfile(fileext = tools::file_ext(file$name))
  writeBin(file$datapath, temp_file)

  # Determine input type
  ext <- tolower(tools::file_ext(temp_file))
  data <- switch(ext,
    csv = read_csv(temp_file),
    xlsx = read_excel(temp_file),
    pdf = data.frame(text = pdf_text(temp_file)),
    docx = data.frame(text = tesseract::ocr(temp_file)),
    txt = read_lines(temp_file),
    stop("Unsupported format")
  )

  # Save report
  output_file <- tempfile(fileext = ".pdf")
  rmarkdown::render("report/report.Rmd", output_file = output_file, params = list(data = data))
  base64enc::base64encode(output_file)
}
