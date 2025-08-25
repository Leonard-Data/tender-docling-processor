from docling.document_converter import DocumentConverter

source = "samples\\I_QGG26762025.pdf"
converter = DocumentConverter()
result = converter.convert(source)

print(result.document.export_to_markdown())