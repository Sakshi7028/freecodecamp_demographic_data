import pandas as pd

def demographic_data_analysis():
    # Read data
    df = pd.read_csv("adult.data.csv", header=None, names=[
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"
    ])
    
    # 1. How many people of each race are represented in this dataset?
    race_count = df["race"].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # 4 & 5. Percentage with advanced vs. non-advanced education earning >50K
    higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_education_rich = round((df[higher_education]["salary"] == ">50K").mean() * 100, 1)
    lower_education_rich = round((df[~higher_education]["salary"] == ">50K").mean() * 100, 1)

    # 6. Minimum number of hours a person works per week
    min_work_hours = df["hours-per-week"].min()

    # 7. Percentage of people working minimum hours earning >50K
    rich_percentage = round((df[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")].shape[0] /
                            df[df["hours-per-week"] == min_work_hours].shape[0]) * 100, 1)

    # 8. Country with highest percentage of people earning >50K
    country_counts = df[df["salary"] == ">50K"]["native-country"].value_counts()
    total_country_counts = df["native-country"].value_counts()
    highest_earning_country_percentage = round((country_counts / total_country_counts * 100).max(), 1)
    highest_earning_country = (country_counts / total_country_counts).idxmax()

    # 9. Most popular occupation for those earning >50K in India
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].mode()[0]

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }
