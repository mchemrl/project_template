import pandas as pd

def input_from_console():
    """
    Reads input from console.

    Returns:
        str: the input from console.
    """
    return input('enter text:')

def input_from_file(filepath):
    """
    Reads text from file using Python built-in methods.

    Args:
        filepath (str): path to the file

    Returns:
        str: the input from file.

    Raises:
        FileNotFoundError: if the file does not exist.
    """
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'file {filepath} not found')

def input_from_file_pandas(filename):
    """
    Reads input in csv from Pandas DataFrame.

    Args:
        filepath (str): path to the file

    Returns:
        pandas.DataFrame: the input from Pandas DataFrame.

    Raises:
        FileNotFoundError: if the file does not exist.
        IOError: if error occured when reading the file.
    """

    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        raise FileNotFoundError(f'file {filename} not found')
    except IOError:
        raise IOError(f'file {filename} not read')
