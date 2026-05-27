import camelot
import tempfile
import shutil


def extract_tables(file_path):

    table_text=[]

    temp_dir=None

    try:

        temp_dir=tempfile.mkdtemp()

        tables=camelot.read_pdf(
            file_path,
            pages='all'
        )

        print(f"Tables found: {len(tables)}")

        for table in tables:

            table_string=table.df.to_string(
                index=False
            )

            table_text.append(
                table_string
            )

    except Exception as e:

        print(
            f"Table extraction failed: {e}"
        )

    finally:

        if temp_dir:
            shutil.rmtree(
                temp_dir,
                ignore_errors=True
            )

    return table_text