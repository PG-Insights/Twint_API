# Twint Zero API Twitter Query

This is a Python script that uses Twint Zero API to perform a Twitter query and save the result in a CSV file.

## Prerequisites

Before using this script, please make sure you have the following software installed:

- Python 3.7 or higher
- Go 1.16 or higher

## Usage

1. Clone this repository to your local machine
2. Open your terminal and navigate to the directory where you cloned the repository
3. Run the following command to install the Python dependencies:

```bash
pip install -r requirements.txt
```

4. Run the script using the following command:

```bash
python main.py [query]
```

where `[query]` is a string representing your Twitter query.

### Example

```bash
python main.py "from:elonmusk since:2022-01-01 until:2022-01-31"
```

This will run a Twitter query for all tweets from Elon Musk between January 1, 2022 and January 31, 2022.

## Output

The script will output the following:

1. A list of the columns in the CSV file
2. A blank line
3. The values of each column for each row in the CSV file

The CSV file will be saved in the same directory as the script and will be named with the date and time of the query and the instance used for the query.

## Contributing

If you would like to contribute to this project, please feel free to create a pull request or open an issue.
