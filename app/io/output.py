import pandas as pd

def output_to_console(text):
    """
    Outputs text to console.

    Args:
        text (str): the text to print to console.
    """
    print(text)

def output_to_file(filepath, text):
    """
    Writes text to a file using Python built-in methods.

    Args:
        filepath (str): path to the file.
        text (str): the text to write to the file.

    Raises:
        IOError: if an error occurs when writing to the file.
    """
    try:
        with open(filepath, 'w') as f:
            f.write(text)
    except IOError:
        raise IOError(f'error writing to file {filepath}')

def output_to_file_pandas(filepath, dataframe):
    """
    Writes a Pandas DataFrame to a CSV file.

    Args:
        filepath (str): path to the output CSV file.
        pandas.DataFrame: the DataFrame to save.

    Raises:
        IOError: if an error occurs when writing the file.
    """
    try:
        dataframe.to_csv(filepath, index=False)
    except IOError:
        raise IOError(f'error writing to file {filepath}')
