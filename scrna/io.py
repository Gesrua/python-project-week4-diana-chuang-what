from scipy.io import mmread
import pandas as pd
def generate_df(matrix_path: str, gene_path: str, barcode_path: str) -> pd.DataFrame:
    """
    - Read count matrix, gene, barcode from given file and merge to a dataframe. 
    - You need to set indices, column labels and their names. For every genes, we only need to use gene symbols as column labels.
    - You may need to read the documentation on docs.scipy.org for more information. Here is a reference:
    https://docs.scipy.org/doc/scipy/reference/tutorial/io.html#matrix-market-files
    """
    df = ???
    return df
