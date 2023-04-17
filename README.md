```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```


# YahooFinanceAutoGetOptions
Auto get todays() opentions from Yahoo Finance Options Page

<span style="color: red"> Warning: </span>

after 1.2.4 pandas not support to save Excel datetime with timezone

You'll get error:

ValueError: Excel does not support datetimes with timezones. Please ensure that datetimes are timezone unaware before writing to Excel.

+Solve

uninstall your pandas and yfinance

pip install pandas==1.2.4

pip install yfinance==0.1.66
