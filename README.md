# Twint Zero API Twitter Query

This script runs a "Twint Zero" API Twitter query and returns the results in CSV format. It uses the `main.go` script from [zedeus/nitter](https://github.com/zedeus/nitter) to perform the query.


## Prerequisites

Before using this script, please make sure you have the following software installed:
- [Go](https://golang.org/doc/install) 1.16 or higher
- Twint Zero
- Python 3.10 or higher
- pip install pandas


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

   where `[query]` is a string representing your Twitter query as described in [igorbrigadir/twitter-advanced-search](https://github.com/igorbrigadir/twitter-advanced-search).

   This will run a Twitter query based on the given query string and save the result in CSV format.

   By default, the script uses the `birdsite.xanny.family` instance of nitter, but you can modify this by changing the `-Instance` parameter in the `return_query_results()` function in `main.py`.


## Output

The CSV file will be saved in the `twint-responses` directory in the same directory as the script, and will be named with the date and time of the query and the query string used for the query.


## Contributing

If you would like to contribute to this project, please feel free to create a pull request or open an issue.


## Questions/Issues

If you have any questions or issues with this script, please feel free to fork it and fix it yourself.

## License

This project is licensed under the MIT License.

## Credits

This project was created by Dale Ludwinski for [Let MO Play](https://letmoplay.com). 

Visit us on [Twitter](https://twitter.com/LetMOPlay).
