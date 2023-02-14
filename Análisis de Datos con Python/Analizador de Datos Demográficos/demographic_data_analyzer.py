import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    manData = df[df['sex'] == "Male"]
    average_age_men = round((np.mean(manData["age"].values)), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelorsData = df[df['education'] == "Bachelors"]
    percentage_bachelors = round((len(bachelorsData) / len(df) * 100), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    
    # percentage with salary >50K    
    higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education)*100, 1)
    lower_education_rich = round(len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education)*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = np.min(df["hours-per-week"].values)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    minWorkHoursData = df[df["hours-per-week"] == min_work_hours]
    minWorkHoursRichData = df[df["salary"] == ">50K"][df["hours-per-week"] == min_work_hours]    
    rich_percentage = round(len(minWorkHoursRichData) / len(minWorkHoursData) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    peopleRichByCountry = df[df["salary"] == ">50K"]["native-country"].value_counts()
    peopleByCountry = df["native-country"].value_counts()
    richVsTotalByCountry = round((peopleRichByCountry /peopleByCountry * 100).sort_values(ascending=False), 1)
    
    highest_earning_country = richVsTotalByCountry.index[0]
    highest_earning_country_percentage = richVsTotalByCountry[0]

    # Identify the most popular occupation for those who earn >50K in India.
    richInIndiaData = df[df["native-country"] == "India"][df["salary"] == ">50K"]
    top_IN_occupation = richInIndiaData["occupation"].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
