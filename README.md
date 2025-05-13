Project title and short description
"COVID-19 Data Analysis and Global Trends"


Objectives of the project
1. Data Acquisition and Preparation: The project aims to import and clean COVID-19 global data from a reliable source.
2. Trend Analysis: The project seeks to analyze time trends related to COVID-19, specifically focusing on cases, deaths, and vaccinations.
3. Comparative Analysis: The project aims to compare COVID-19 metrics across different countries or regions.
4. Data Visualization: The project aims to visualize the identified trends using appropriate charts and maps.
5. Communication of Findings: The project aims to effectively communicate the insights and findings from the data analysis in a structured report.

List of tools and libraries used
1. pandas: For data manipulation and analysis (loading, cleaning, and transforming the data).
2. matplotlib: For creating basic data visualizations (line charts).
3. seaborn: For creating more visually appealing statistical data visualizations.
4. plotly.express: For creating interactive visualizations, specifically the choropleth map.

How to run/view the project.
The script analyzes COVID-19 data from around the world. It performs these main steps:

1. Loads the data: It reads the data from a file.
2. Cleans the data: It selects data for specific countries (Kenya, USA, and India), removes any incomplete data, and prepares the dates for analysis.
3. Analyzes the data: It calculates and displays key information like total cases, deaths, and vaccination numbers over time.
4. Visualizes the data: It creates graphs to show how these numbers change over time and compares them between the selected countries.
5. Reports the findings: It prints out a summary of the most important observations from the analysis.

Any insights or reflections.
1. Vaccination Disparities: The USA has a significantly higher total vaccination count compared to Kenya and India, highlighting disparities in vaccine access and rollout speed.
2. India's Case Surge: India experienced a sharp surge in new cases, indicating a major wave of the virus.
3. Death Rate Trends: The death rate (total deaths / total cases) varies across countries.
4. Data Limitations: There are missing values in the 'total_vaccinations' column, suggesting that more robust techniques could be employed to handle missing data.
5. Trend Visualization: The line charts effectively illustrate the progression of total cases, deaths, and vaccinations over time for each selected country, making it easy to compare the dynamics of the pandemic.
