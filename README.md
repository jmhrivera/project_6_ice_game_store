#### Overview

This project aims to analyze video game sales data to uncover useful insights related to game popularity, sales trends, and regional preferences. The project involves a detailed data cleaning process, data analysis, and visualization using various libraries like pandas, plotly_express, seaborn, and others. The video game data spans different years, platforms, and regions, allowing for a comprehensive exploration of the market dynamics.

#### Objectives

1. Clean and preprocess the video game dataset.
2. Analyze various trends in the gaming industry, such as sales by year, platform, and genre.
3. Determine the top video game platforms and their sales performance.
4. Investigate the correlation between critic/user scores and total sales.
5. Identify the top-selling games across different platforms.
6. Analyze regional preferences in terms of gaming platforms and genres.
7. Perform hypothesis testing to validate certain industry assumptions.

#### Way to Work

1. **Data Importing:** Load the video game sales dataset into a DataFrame.
2. **Data Cleaning:**
    - Convert column names to lowercase.
    - Identify and remove duplicates and handle missing values appropriately.
    - Standardize data formats and correct any inconsistencies or inaccuracies.
3. **Data Analysis and Visualization:**
    - Perform analysis on game releases by year and identify sales trends.
    - Determine the top platforms by total sales and analyze their sales performance by year.
    - Analyze profits per game on different platforms.
    - Investigate the impact of critic and user scores on total sales.
    - Identify the top 10 games and their performance across different platforms.
    - Determine the most popular genres and analyze their regional performance.
    - Analyze the impact of ESRB classifications on game sales.
4. **Hypothesis Testing:**
    - Test whether the average user ratings for Xbox One and PC platforms are the same.
    - Test whether the average user ratings for Action and Sports genres are different.
5. **Conclusion:**
    - Derive insights from the analysis and visualizations.

#### Requirements

- pandas
- numpy
- matplotlib
- plotly_express
- seaborn
- scipy

To install the required packages, use the following command:

```bash
pip install -r requirements.txt
```