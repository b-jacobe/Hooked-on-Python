"""
convert_pdf.py

Convert PDF to excel,
CSV, or XML using Python.
Users the PDFTables library

@Author: Brian Jacobe
@Date: 10-26-2019
"""

import pdftables_api

# IMPORTANT - Free account has 50 page limit.
# Uses Left - 46 pages
pdf_convert = pdftables_api.Client('jwxynei1wljb')
pdf_convert.xlsx('Copy of 10_23_2019 LI Fabric Instock Report.pdf', 'LI Fabric Instock Report')