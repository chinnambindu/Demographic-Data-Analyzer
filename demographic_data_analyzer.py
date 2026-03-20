import pandas as pd


def calculate_demographic_data(print_data=True):
    # Load dataset 
    df = pd.read_csv("adult.data.csv")

    # 1. Race counts 
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)

    #  3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").sum() / len(df) * 100, 1
    )

    #  4 & 5. Advanced vs. non-advanced education earning >50K 
    advanced_edu = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_salary = df["salary"] == ">50K"

    higher_education_rich = round(
        (df[advanced_edu & higher_salary].shape[0] / df[advanced_edu].shape[0]) * 100, 1
    )
    lower_education_rich = round(
        (df[~advanced_edu & higher_salary].shape[0] / df[~advanced_edu].shape[0]) * 100, 1
    )

    #  6. Minimum hours worked per week 
    min_work_hours = df["hours-per-week"].min()

    #  7. Percentage of min-hour workers earning >50K 
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(
        (min_workers["salary"] == ">50K").sum() / len(min_workers) * 100, 1
    )

    #  8. Country with highest percentage earning >50K 
    country_counts  = df["native-country"].value_counts()
    country_rich    = df[higher_salary]["native-country"].value_counts()
    country_pct     = (country_rich / country_counts * 100).dropna()

    highest_earning_country            = country_pct.idxmax()
    highest_earning_country_percentage = round(country_pct.max(), 1)

    #  9. Top occupation in India for >50K earners 
    top_IN_occupation = (
        df[(df["native-country"] == "India") & higher_salary]["occupation"]
        .value_counts()
        .idxmax()
    )

    #  Optional print 
    if print_data:
        print("Number of each race:\n",          race_count)
        print("Average age of men:",              average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count":                          race_count,
        "average_age_men":                     average_age_men,
        "percentage_bachelors":                percentage_bachelors,
        "higher_education_rich":               higher_education_rich,
        "lower_education_rich":                lower_education_rich,
        "min_work_hours":                      min_work_hours,
        "rich_percentage":                     rich_percentage,
        "highest_earning_country":             highest_earning_country,
        "highest_earning_country_percentage":  highest_earning_country_percentage,
        "top_IN_occupation":                   top_IN_occupation,
    }
