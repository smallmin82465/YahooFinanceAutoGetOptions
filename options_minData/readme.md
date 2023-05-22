options_minData():

The code defines a function called optionget_min that accepts a list of stock symbols as parameters. This function uses the yfinance package to retrieve option data for a specified stock symbol and save it as a CSV file. The specific process is as follows:

a. Use yf.Ticker(sym) to get the Ticker object of the stock symbol.

b. Use tk.options to get a list of expiration dates.

c. Create an empty DataFrame(options) to hold the results.

d. Use tk.option_chain(exp[0]) to get the call and put options on the first expiration date.

e. Merge call and put options into one DataFrame(opt).

f. Add the call and put options for each expiration date to the options DataFrame.

g. Use opt['volume'] >= 10 to filter out option contracts with a trading volume greater than or equal to 10.

h. Use the ticker.history() method to retrieve one-minute data within the specified date range.

i. Add contractSymbol and Datetime fields in option data.

j. Round off the Open, High, Low, and Close fields to two decimal places.

k. Select the required fields and save the result to the result DataFrame.

l. Cut out the fields such as stock code, expiration date, CALL_PUT and strike price.

m. Name the CSV file with today's date and stock symbol, save the result to the CSV file
