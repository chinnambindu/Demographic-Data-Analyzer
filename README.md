# Demographic Data Analyzer

A **freeCodeCamp – Data Analysis with Python** certification project.

## Overview

Analyzes the 1994 UCI Census dataset using **Pandas** to answer nine demographic
questions about education, income, race, occupation, and working hours.

## Questions answered

| # | Question |
|---|----------|
| 1 | How many people of each race are in the dataset? |
| 2 | What is the average age of men? |
| 3 | What percentage of people have a Bachelor's degree? |
| 4 | What percentage of people **with** advanced education earn >50K? |
| 5 | What percentage of people **without** advanced education earn >50K? |
| 6 | What is the minimum number of hours worked per week? |
| 7 | What percentage of min-hour workers earn >50K? |
| 8 | Which country has the highest % of people earning >50K, and what is that %? |
| 9 | What is the most popular occupation for >50K earners in India? |

## Dataset

Download **`adult.data.csv`** from the freeCodeCamp boilerplate repo and place
it in the project root before running:

```
https://github.com/freeCodeCamp/boilerplate-demographic-data-analyzer
```

The CSV must have these columns (space-free header row):

```
age, workclass, fnlwgt, education, education-num, marital-status,
occupation, relationship, race, sex, capital-gain, capital-loss,
hours-per-week, native-country, salary
```

## Requirements

- Python 3.8+
- Pandas

```bash
pip install pandas
```

## Usage

```bash
python main.py
```

**Example output (real dataset):**

```
Number of each race:
 race
White                 27816
Black                  3124
Asian-Pac-Islander     1039
Amer-Indian-Eskimo      311
Other                   271
Name: count, dtype: int64

Average age of men: 39.4
Percentage with Bachelors degrees: 16.4%
Percentage with higher education that earn >50K: 46.5%
Percentage without higher education that earn >50K: 17.4%
Min work time: 1 hours/week
Percentage of rich among those who work fewest hours: 10.0%
Country with highest percentage of rich: Iran
Highest percentage of rich people in country: 41.9%
Top occupations in India: Prof-specialty
```


## Built with

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

