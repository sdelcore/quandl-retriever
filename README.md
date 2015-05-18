# quandl-retriever
Packages:
•	python2.7
•	numpy
•	panda
•	quandl
•	csv
•	urllibb2

Quandl usage rules:
Dataset calls are rate-limited to 2,000 calls per 10 minutes. Search calls are limited to 60 per minute. 

I've created 4 functions
  1.	is_time
    ◦	Description: pauses the script if needed, complying to Quandls usage rules
    ◦	Arguments: 
      ▪	bool search: will specify if the command about to be performed is searching or not 
    ◦	Returns: void
  2.	csv_write
    ◦	Description: Writes a list into a CSV file
    ◦	Arguments: 
      ▪	string filename: name of the CSV file 
      ▪	list data: list of lists to be written into CSV file
    ◦	Returns: void
  3.	update_dataset_csv
    ◦	Description: updates a CSV file with all the codes and names of those codes from a source database
    ◦	Arguments: 
      ▪	string token: API token
      ▪	string source: the Quandl database source
      ▪	string csv_name: name of the CSV file to write the codes to 
    ◦	Returns: void
  4.	retrieve_dataset_codes
    ◦	Description: retreives all the codes from a CSV file
    ◦	Arguments: 
      ▪	string filename: name of the CSV file to write the codes to 
    ◦	Returns: list of dataset codes and names [[code],[name]]
  5.	get_dataset_information
    ◦	Description: retreives data from the dataset from specified source and writes to a CSV file with the name of the dataset
    ◦	Arguments: 
      ▪	string token: API token
      ▪	string source: the Quandl database source
      ▪	string dataset_codes: a list of dataset codes and names 
  ◦	Returns: void

The script will first do search queries to retrieve all the dataset codes and write them to a CSV file, then it'll read from the CSV file and do get requests for the data. It'll then save the data in CSV files with the full name of the dataset as the filename.
