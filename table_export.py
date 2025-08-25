from docling.document_converter import DocumentConverter
import logging
import time 
from pathlib import Path

import pandas as pd

_log = logging.getLogger(__name__)

def main():
    source = "samples\\I_QGG26762025.pdf"
    converter = DocumentConverter()
    start_time = time.time()
    conv_res = converter.convert(source)
    output_dir = Path("scratch")
    output_dir.mkdir(exist_ok=True, parents=True)
    _filename = conv_res.input.file.stem

    # Export tables
    for table_ix, table in enumerate(conv_res.document.tables):
        df: pd.DataFrame = table.export_to_dataframe()
        print(f"## Table {table_ix}")
        print(df.to_markdown())
        # Save the table as csv
        element_csv_filename = output_dir / f"{_filename}-table-{table_ix + 1}.csv"
        _log.info(f"Saving CSV table to {element_csv_filename}")
        df.to_csv(element_csv_filename)

        # Save the table as html
        element_html_filename = output_dir / f"{_filename}-table-{table_ix + 1}.html"
        _log.info(f"Saving HTML table to {element_html_filename}")
        with element_html_filename.open("w") as fp:
            fp.write(table.export_to_html(doc=conv_res.document))

    end_time = time.time() - start_time

    _log.info(f"Document converted and tables exported in {end_time:.2f} seconds.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()