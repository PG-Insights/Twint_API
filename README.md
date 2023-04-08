# Twint Zero API Twitter Query

This is a Python script that uses Twint Zero to perform a Twitter query and save the result in a CSV file. Twint Zero is a lightweight version of Twint that runs faster and with less overhead.

## Prerequisites

Before using this script, please make sure you have the following software installed:

- Python 3.7 or higher
- Go 1.16 or higher
- Twint Zero

To install Twint Zero, follow these steps:

1. Clone the Twint Zero repository to your local machine:

   ```bash
   git clone https://github.com/twintproject/twint-zero
   ```

2. Navigate to the cloned repository:

   ```bash
   cd twint-zero
   ```

3. Initialize the Go module:

   ```bash
   go mod init twint-zero
   ```

4. Tidy the Go module:

   ```bash
   go mod tidy
   ```

   Twint Zero was created by Francesco Poldi, with contributions from Simon Archer.

   [Francesco Poldi](https://twitter.com/noneprivacy)

   [Simon Archer](https://mastodon.social/@archy_bold): JSON formatting and attachments parsing


## Usage

1. Clone this repository to your local machine
2. Open your terminal and navigate to the directory where you cloned the repository
3. Run the following command to install the Python dependencies:

```bash
pip install -r requirements.txt
```

4. Run the script using the following command:

```bash
python main.py [query] [instance] [format]
```

where `[query]` is a string representing your Twitter query, `[instance]` is the instance of the Nitter server to use, and `[format]` is the desired output format ("csv" or "json").

### Example

```bash
python main.py "from:elonmusk since:2022-01-01 until:2022-01-31" birdsite.xanny.family csv
```

This will run a Twitter query for all tweets from Elon Musk between January 1, 2022 and January 31, 2022, using the birdsite.xanny.family instance of the Nitter server, and saving the result in CSV format.

## Output

The script will output the following:

1. A list of the columns in the CSV file
2. A blank line
3. The values of each column for each row in the CSV file

The CSV file will be saved in the same directory as the script and will be named with the date and time of the query and the instance used for the query.

## Contributing

If you would like to contribute to this project, please feel free to create a pull request or open an issue.

## Questions/Issues

If you have any questions or issues with this script or the Twint Zero API, please feel free to reach out to the Twint team.

## License

This project is licensed under the MIT License.

## Credits

This project was created by Dale Ludwinski for [Let MO Play](https://letmoplay.com) 
Visit us on [Twitter](https://twitter.com/LetMOPlay)
