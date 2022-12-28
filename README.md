# Challenge 2 - Save Qualified Loans

This program is designed to assist users in obtaining and saving a list of qualified loans based on their user criteria. 

---

## Technologies

This project leverages python 3.7 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface and entry-point.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
```

---

## Usage

To look up and save qualifying loans simply clone the repository and run the **app.py**. You'll need to pull the data from the following location: *./data/daily_rate_sheet.csv* 

### Pulling Qualified Loans ###
Upon launching **app.py** you will be prompted for the data source location: *./data/daily_rate_sheet.csv* 

It will then ask you for your:
```
Credit Score
Monthly Debt
Monthly Income
Desired Loan Amount
Home Value
```

The app will then provide you with your debt to income ratio, loan to value ratio, and the number of qualified loans it found. You will then be asked if you would like to save your results.

### Saving Your Results ###

If you confirm Yes, the app will ask you where you wish to download your results. No need to add the csv name as this is already completed. Simply list the folder loaction. Sush as: *./data*

### Example ###

![Vidoe that shows an example]("https://giphy.com/embed/PTVoBU04kTo55PFcXy")
---

## Contributors

Solely created by Michael Roth

---

## License

N/A
