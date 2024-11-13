# File: pdf_merger.py

from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_file):
    """Merges multiple PDF files into a single PDF."""
    merger = PdfMerger()
    
    try:
        for pdf in pdf_list:
            merger.append(pdf)
        
        merger.write(output_file)
        merger.close()
        print(f"Merged PDF saved as {output_file}")
    except Exception as e:
        print(f"Error merging PDFs: {e}")

if __name__ == "__main__":
    pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']  # Replace with your files
    output_pdf = "merged.pdf"
    merge_pdfs(pdf_files, output_pdf)
