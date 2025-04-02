from app.io.input import input_from_console, input_from_file, input_from_file_pandas
from app.io.output import output_to_console, output_to_file, output_to_file_pandas

def main():
    text_console = input_from_console()
    output_to_console(text_console)
    output_to_file("console_output.txt", text_console)

    text_file = input_from_file("input.txt")
    output_to_console(text_file)
    output_to_file("file_output.txt", text_file)

    df = input_from_file_pandas("data.csv")
    output_to_console(df.to_string())
    output_to_file_pandas("data_output.csv", df)

if __name__ == '__main__':
    main()

