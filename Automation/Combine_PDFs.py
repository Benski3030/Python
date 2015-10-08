import os
from PyPDF2 import PdfFileReader, PdfFileMerger

files_dir = "file/path"
pdf_files = [f for f in os.listdir(files_dir) if f.endswith("pdf")]
pdf_files = sorted(pdf_files)
merger = PdfFileMerger()

for filename in pdf_files:
    merger.append(PdfFileReader(os.path.join(files_dir, filename), "rb"))

merger.write(os.path.join(files_dir, "MergedWorkbook.pdf"))
