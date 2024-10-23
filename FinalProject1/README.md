# Project-Team-3

Team Members: Fran Ruiz, Kathryn Mcatee, Nurmaa Dashzeveg, Sam Sims

Introduction to project
US Healthcare spend continues to increase year over year. Is the investment worth it? And does that answer change based on where you live, how much you make, if you receive government assistance, or where all of that spend is being allocated? The Outliers plan to figure that out.

What does it do: 
With the increasing investment individuals and families need to make for healthcare year over year, whether you’re on government or private insurance, there is an interest to understand if the amount personally paid is contributing to an individual’s greater good.

The Outliers aim to give peace of mind to consumers wondering the same question. For our first endeavor, we will only be looking at CMS data/spend compared to Census and Mortality data to see if there is correlation between spend, location, income, and death, but recognize there are many other avenues to compare to truly get to the root of this complex answer.

Target Audience: American population that utilizes health insurance

Data: 
2 CMS.gov Health Expenditures by State of Residence, 
1991-2020: https://www.cms.gov/data-research/statistics-trends-and-reports/national-health-expenditure-data/state-residence
https://www.statista.com/statistics/184955/us-national-health-expenditures-per-capita-since-1960/ 
US Census
County Health Rankings
https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation/national-data-documentation-2010-2022


What is needed to run code. There are no extra libraries or modules needed to run code, Census data was collected from the Census website and precombined for the required time period.

UsefulFuntions.py is a collection of funtions that we thought would end up being used multiple times in an attempt to streamline the coding. There is a function for linear regression, and 2 for creating scatter plots, one that utilizes linear regression and one that does not. Was hoping to expand it to include a function to change the CMS data into an easier to combine format.

Analysis of Data

Spending over time
There is an increase of spending over time however the amount of spending per person has not increased by as much meaning that the increase is more likely related to population than the price of the insurance. The ratio of 3 types of spending has also stayed close to the same over the 7 year time period.

Mortaltiy VS goverenment spending
For this comparison we took the total deaths in each year from 2010 to 2017 and divided it by the population to account for some states having much larger populations that others to get the percentage of people who died in a state in a given year. After that we looked at the total spending of each of those states also divided by the population of those state to get the per captia spending of each state for each of the year. The we made a scatter plot of the 2 values, Mortality Rate and Per capita spent on insurance to see if there was a correlation. We found an Rsquared value of .26 or that there was about a 26% relation between the money spent on insurance and the death rate of the state. This shows a weak coorelation between the 2.

Government VS personal spending
Healthcare is getting more expensive and spend is increasing year over year – no surprise there. But rather than just looking at total spend, we want to see where the spend was increasing. This segment looked at government program spending to understand if it was increasing year over year on a variety of levels.

We first looked at the total spend per capita by service and year. Certain data sets were broken down by code, so we were able to understand not just if spend was increasing, but where. The year over year increase is consistent across programs, in some states more than others, with the top 3 areas of spend being Personal Health Care, Hospital Care, and Physician & Clinical Services. We next looked at the spend by service at the government program level - Medicare and Medicaid. With clear data showing personal health spend was increasing, we wanted to look to see if we saw the same trend in government program spending. Not only do you see the same upward trend, you can see sharper increases on Medicaid starting around 2014 (for those who need the extra financial support) vs. those on Medicare (those 65 & older) – Medicare is also increasing but at a steady pace. Finally, diving one level deeper, we looked at the spend by state for government programs, you’ll notice both saw increases from 2010-2017, some states more than others. Key call out is that Medicaid is actually seeing a higher spend than Medicare, though Medicare is seeing sharper increases year over years.

One thing we wanted to look into that proved challenging because we didn’t have the data we needed to do it – there would be too many assumptions in the data we had, was overlay those on Medicare and Medicaid – if you’re on Medicare, there’s a chance you could be on Medicaid, but if you’re on Medicaid, it doesn’t necessarily mean you’re on Medicare.

Age Compared to Medicare
The purpose of this report is to analyze the trends in total population and Medicare enrollment across U.S. states from 2010 to 2017. Utilizing data from the U.S. Census Bureau and Medicare enrollment statistics, this report seeks to understand how population changes correlate with Medicare enrollment eligibility and actual enrollment figures. 

There were two data sets for this analysis one is the census data and the second is the Medicare data. Both data sets were cleaned to find reading usable for this data. The census data presented more challenged due to having nan characters, and the columns descriptions were improved changing larger description to more easy reading description for example: in the census data from ‘Acsst5Y2010.S0101-Data.1.2’ to ‘Year’,  ‘Geographic Area Name’ to ‘State’ or ‘Total Estimate Total Population’ to ‘Total population’, ‘Total  Estimate  Selected Age Categories 65 Years and Over’ to ‘Age Categories 65 Years and Over’:  

On the other dataset, the Medicare_data I applied the same cleaning process to change the description from ‘Y2010, Y2011, Y2012, Y2013, Y2014, Y2015, Y2016, Y2017’ to ‘Medicare 2010, Medicare 2011, Medicare 2012, Medicare 2013, Medicare 2014, Medicare 2015, Medicare 2016, Medicare 2017’:  

Some of the main finding from these data sets are:  

Total population in the US from 2010 to 2017 

The purpose of this analysis is to investigate the total population trends in the United States over several years. Using census data, the population totals were grouped by year to identify changes and patterns in population growth. The results were visualized using a line chart, offering a clear representation of how the population has evolved over time. 

The dataset used for this analysis contains population data from the U.S. Census, covering multiple years. The steps taken for the analysis are as follows: 

Data Grouping: The data was grouped by year, and the total population for each year was calculated using the groupby() function. 

Visualization: A line plot was created to display the total population for each year, with markers representing each year on the line. 

Findings:  

The plot clearly shows a steady increase in the U.S. population over the years. Each point on the graph represents the total population for a specific year. 

The population growth appears to be gradual, with no sharp spikes or declines over the given time period, indicating consistent population growth. 

The total population in the United States has been steadily growing over the analyzed period. This is consistent with historical population trends, driven by factors such as natural population growth (births exceeding deaths) and immigration. Understanding population trends is crucial for various policy decisions, including resource allocation, infrastructure development, and social services planning. 

Top ten States by Medicare Enrollment in 2010 

This report analyzes the top ten states with the highest Medicare enrollment in the United States for the year 2010. Medicare is a federal health insurance program that primarily serves individuals aged 65 and older, as well as certain younger people with disabilities. Understanding the distribution of Medicare enrollees by state provides insight into healthcare demands and resource allocation at both state and federal levels. 

The analysis was performed using the new_merged_data dataset, which contains both population and Medicare data across different years. The following steps were taken: 

Data Filtering: The dataset was filtered to include only records for the year 2010. 

Top 10 States Selection: The nlargest() function was used to identify the top 10 states with the highest Medicare enrollment in 2010. 

Visualization: A horizontal bar chart was created to visually represent the top 10 states by Medicare enrollment for that year. 

Key observations:  

The state with the highest Medicare enrollment in 2010 was California, with an enrollment figure of 4,747,000 people. 

The states at the top of the list, including Florida and Texas, have notably larger populations, which likely contributes to their higher Medicare enrollments. 

The chart shows a significant drop between the top few states and those ranked lower in the top 10, reflecting the varying levels of population across different states. 

The states with the highest Medicare enrollments tend to be those with larger populations and higher proportions of elderly residents. For example, states like Florida, Texas, and California often appear at the top of such lists due to their large elderly populations. These states may face higher healthcare demands, which could impact the allocation of Medicare funding and healthcare resources. 

The last ten states by Medicare Enrollment in 2010 

This report presents an analysis of the 10 states with the lowest Medicare enrollment in the United States for the year 2010. Medicare enrollment is an important metric, as it reflects the number of elderly or eligible individuals receiving healthcare coverage under the federal Medicare program. By identifying the states with the lowest enrollment, we can explore potential reasons for such low figures and the possible healthcare needs of these states. 

The analysis was performed on the new_merged_data dataset, which contains population and Medicare data across various years. The specific focus is on the year 2010. The following steps outline the methodology used: 

Data Filtering: The dataset was filtered to include only the records for the year 2010. 

Lowest 10 States: The nsmallest() function was used to identify the 10 states with the lowest Medicare enrollments in 2010. 

Visualization: A horizontal bar chart was created to display the bottom 10 states by Medicare enrollment for 2010, with the states ranked from lowest to highest. 

The analysis highlights the 10 states with the lowest Medicare enrollment in 2010, revealing significant variation in enrollment across different regions of the United States. Alaska and District of Columbia had the lowest enrollment numbers, while the gap between the lowest and the 10th state on the list is still substantial. 

Understanding the factors behind these low enrollment figures could help policymakers and healthcare providers address potential disparities in access to healthcare resources in these states. Further research could explore how Medicare enrollment has changed in these states over time and how it compares to healthcare coverage trends at the national level. 

Comparison of Medicare Enrollment in 2010 and 2017 with changes over the years.  

This report presents a comparative analysis of the top 10 states with the highest Medicare enrollments for the years 2010 and 2017. Medicare, a critical federal healthcare program, is designed to provide health insurance to people aged 65 and older, as well as certain younger individuals with disabilities. The analysis highlights changes in Medicare enrollments over time and identifies trends in spending across states. 

The analysis was conducted using a merged dataset containing population and Medicare data for both 2010 and 2017. The following steps outline the methodology: 

Data Filtering: The dataset was filtered to include records from 2010 and 2017. 

Top 10 States Selection: For both years, the top 10 states with the highest Medicare enrollments were identified using the nlargest() function. 

Data Merging: The two dataframes containing the top 10 states for 2010 and 2017 were merged, allowing for a side-by-side comparison of Medicare enrollments in each state. 

Visualization: A grouped bar chart was created to display Medicare enrollment in both years, along with a line plot to represent the change in Medicare enrollment from 2010 to 2017. 

The green line in the chart above represents the change in Medicare enrollments between 2010 and 2017 for each state. This change provides valuable insights into the states where Medicare enrollment has increased or decreased the most over the seven-year period. 

Significant Growth: Some states, such as California and Florida, experienced significant growth in Medicare enrollment, reflecting either an aging population or improvements in Medicare access. 

Stable or Declining Enrollment: States like Ohio had relatively stable enrollments, with only minor changes between the two years. 

Geographical Patterns: There may be regional differences contributing to the trends, with some regions showing higher increases in Medicare enrollments due to demographic shifts or state-specific policies related to healthcare. 

The comparison of Medicare enrollments in 2010 and 2017 reveals significant variation across states in both absolute enrollment numbers and the rate of change over time. The analysis highlights states with the highest Medicare enrollments, such as Texas, and those with significant increases, such as California. 

These trends may reflect demographic changes, such as an aging population in some states, or differences in state healthcare policies. Policymakers can use this information to better understand healthcare needs and resource allocation across states. 

Medicare Enrollment in the US per State 

This report provides a comparative analysis of Medicare enrollment by state for the years 2010 and 2017. Medicare, a vital healthcare program in the United States, supports millions of individuals over the age of 65 as well as certain younger individuals with disabilities. This analysis aims to illustrate how Medicare enrollments varied across states in these two years, providing insights into trends and potential regional differences. 

The analysis was conducted using a merged dataset containing Medicare enrollment data from both 2010 and 2017 for each state. The following steps outline the methodology used: 

Data Filtering: The dataset was filtered to select data from the specified years, 2010 and 2017, allowing for a direct comparison of Medicare enrollments per state. 

Line Plot Visualization: Line plots were created to visualize Medicare enrollments per state in both 2010 and 2017. Each state’s enrollment is represented on the x-axis, while the y-axis displays the number of enrollees in thousands for both years. 

The line plot comparison reveals distinct trends: 

Rapid Growth in Enrollment: States like California, Florida, and Texas saw rapid growth in enrollments, which may reflect the states' growing elderly populations or healthcare expansion efforts. 

Moderate or Minimal Changes: In contrast, smaller states such as Rhode Island and Montana experienced smaller or more gradual changes in Medicare enrollments. 

Regional Differences 

The differences in Medicare enrollment growth across states could be attributed to: 

Population Aging: States with higher percentages of aging populations such as Florida naturally see more significant increases in enrollments. 

State Healthcare Policies: Local policies and Medicare outreach programs may also influence the degree of growth in Medicare enrollments. 

The analysis of Medicare enrollment data for 2010 and 2017 reveals substantial variability across states. Larger, more populous states, especially those with growing elderly populations, saw the greatest increases in enrollments, while smaller states experienced more stable trends. 

These insights highlight the importance of understanding state-specific demographic shifts and healthcare policies when assessing future Medicare demands. 

Top ten States by Medicare Enrollment in 2010, 2014 and 2017 

The purpose of this analysis is to compare the Medicare enrollment trends across the top 10 states in the years 2010, 2014, and 2016. By visualizing the Medicare enrollment for these years, we aim to identify patterns and changes in the enrollment numbers over time. 

The dataset used contains Medicare enrollment data per state for the years 2010, 2014, and 2016. The code filters the data for each of these years and selects the top 10 states with the highest Medicare enrollment in each year. 

Key steps in the analysis: 

Filtering Data by Year: The dataset is filtered to extract data for the specific years (2010, 2014, and 2016). 

Identifying Top 10 States: The nlargest() function is used to select the top 10 states by Medicare enrollment for each year. 

Plotting the Data: A line chart is used to visualize Medicare enrollment for the top 10 states across the selected years. For each year, a line is plotted for each state showing its enrollment numbers. 

Key Findings 

State-Level Medicare Enrollment: The line plot for each year shows the top 10 states with the highest Medicare enrollments. 

Enrollment patterns show variation from state to state, with some states consistently ranking high across multiple years. 

Trend Over the Years: By plotting the data for three different years (2010, 2014, and 2016), the chart illustrates how Medicare enrollments have changed within the top 10 states over time. 

Some states show steady growth, while others fluctuate in enrollment numbers across the three years. 

Interpretation 

Consistent States: States that consistently appear in the top 10 for all three years likely have large populations of eligible individuals for Medicare. 

Year-on-Year Changes: The chart shows states with increasing or decreasing Medicare enrollments, which may indicate demographic shifts, changes in state healthcare policies, or other factors. 

The visual comparison of Medicare enrollments in 2010, 2014, and 2016 highlights key states with high Medicare enrollments and reveals trends over time. This information can be useful for healthcare policymakers to assess the demand for Medicare services and plan resource allocation accordingly. 

A look into Income - The relationship between high earners and healthcare spending. 

Income varies based on job types and perhaps legal wills or inheritance. Income can indeed differ widely depending on the type of job, the industry, level of experience, location, and many other factors. Health expenses can vary depending on the healthcare provider, location, type of care, and the healthcare system in each state in United States. In the current project, we aim to see if health care expenses correlate with income level of people.  

To answer our question, we analyzed US_POPULATION20.CSV for population by states throughout years 2010-2017, US_PER_CAPITA20.CSV for spendings by states throughout years and Income.csv for household income by states collected from United States Census Bureau (refer to attached data_inventory.xlsx).  

  

Strategy of the analysis 

           

First, all data were cleaned using .dropna() (Fig.1).  After cleaning, data showed equal number of contents when checking with .count, and reduced number of columns and rows when use .shape.  Later, useful columns for further analysis were selected and saved in new dataframes. In US_POPULATION.csv, population were multiplied by thousand to create total population and the years in Year-columns were shifted to the rows by using looping and .concat(). Income per person in different states was calculated by dividing Income.csv by number of total populations. Next, using looping and .concat(), columns_Year is shifted to the rows and using .pivot_table() contents in the Items column were listed as columns to analyze US_Per_Capita20.csv to create same arrangement of the table as in Income.csv. After that, the values of the spendings in different health care were combined to estimate total expenses of health care. Finally, all data were merged by utilizing .merge() for further analysis.  

Output of the analysis 

  

Comparing income levels of 2010 to 2017 of States with their health care spendings show mild positive correlation (R=0.39, P=1.188e-16) indicating wealthy population spends more in health care. Income levels of 51 states (includes District of Columbia) of US show small differences; the highest income was in District of Columbia, Maine, and Vermont and the states with lowest income were Utah, Hawai and California suggesting average earning of States in US is balanced. States like California where most of the richest people live has big diversity in terms of income level.

Alternative potential strategy: In the current analysis, I combined all spendings together and compared with income level. It might be better to categorize spendings into health serious illness-related and healthcare services for pleasure will estimate better correlation with income.  

 

Lesson learned: 

1. Understanding the data and understanding the questions to be answered is the most important.  

2. Exploring in data deeply and make a detailed strategy for the analysis and collect the information (codes) that is useful for this analysis to answer the specific questions are also required. Data are broad enough to create numerous outputs, focusing on the specific question will save time and reproducibility. 

3. Checking data quality and the resources of data are essential to be considered before starting analysis.  

4. Be friends with GOOGLE 

  

What should be done: (1) In the current analysis, I have combined different expenses of health care to compare Income level and mild correlation of expenses with Income. If expenses were categorized, it might lead to a better outcome. (2) The income values of per person was less than one which was less than expenses on health care. The original value of Income might be in thousands; however it was not indicated in the resource. It traced back in the future.  

  

Conclusion 

 

Analyses of income levels versus healthcare expenses provide a mild positive correlation, indicating that people spend, and purchase healthcare products based on their income level.  

  

Discussion 

  

(1) People with higher incomes tend to invest more in preventive care and healthier lifestyle choices (e.g., gym memberships, organic foods, wellness programs), which can result in higher overall healthcare spending. These expenditures reflect the ability to prioritize long-term health.  

(2) Although higher-income people can afford routine healthcare and prevention, lower-income people tend to spend a higher percentage of their income on healthcare in emergency situations. But the overall spending remains lower due to limited access to services.  

(3) Higher-income groups tend to purchase more expensive, high-quality healthcare products—such as prescription drugs, supplements, medical devices, or advanced treatments—which increase total healthcare spending. 

(4) Wealthier individuals are more likely to have comprehensive health insurance that covers a wider range of medical services, often allowing them to seek specialized care or advanced treatments, which they can afford either through insurance premiums or out-of-pocket spending. 

(5) The results of Average Income analysis of States showed California and Utah as a lowest income states, however, these states are known to have high income earnings indicating the variation of the income is high in those states. 
