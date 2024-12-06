## Business Understanding

Despite being a fairly large company, Jaya Jaya Maju still has difficulties in managing employees. This resulted in a high attrition rate (the ratio of the number of employees who left to the total number of employees) of more than 10%.

### Business Problem

In order to prevent this from getting worse, the HR department manager would like help to identify various factors that affect the high attrition rate. In adittion, he also requested to create business dashboard to help him in monitoring the various factors.

### Project scoope
To answer the business problem, in this project we use two method, correlation analysis and machine learning. Machine learning algorithm that we used is Random Forest Classifier, with the model created we apply the function 'feature importances' to find out what features are most affected by attrition.

We will also conduct an EDA (Exploratory Data Analysis) process to obtain data distribution and overview of the dataset.

In addition, we also created a business dashboard using Tableau to provide insight from the data being analysed, and is useful for monitoring features/factors that affect the high attrition rate.

We also created a web app on streamlit that can be used to predict attrition from inputted employee data.

### Preparation

Data source: [data.csv](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/employee/employee_data.csv)

Setup environment:
1. Open this file '[notebook.ipynb](https://github.com/MuhamadSyarifFakhrezi/Employee-Attrition-Analytics/blob/main/notebook.ipynb)' in Google Colaboratory
2. Running this code
   ```
   !pip install -r requirements.txt
   ```

### Run Streamlit App

```
streamlit run app.py
```
Streamlit prediction app link: [attrition-predictor](https://attrition-predictor.streamlit.app/)

## Business Dashboard
![muhamadsyarif-dashboard](https://github.com/user-attachments/assets/5bd2970b-e67c-463f-a77d-f4ab5865be53)
![muhamadsyarif-dashboard2](https://github.com/user-attachments/assets/ac206197-4f78-4419-9b0b-b8f7c80bf769)

Based on the dashboard that has been created, the following are some of the insights obtained:
- Employees aged 18-26 years old have a higher percentage of attrition rates.
- Gender has no affect on attrition.
- Single employees have a higher attrition rate compared to other categories of marital status.
- Employees with an educational background in the Technical Degree field have the highest attrition rate compared to other fields, but the difference in attrition rates between fields is not very significant.
- Employees with monthly income between 1k-4k are more likely to resign.
- Employees having worked less than 3 years are more likely to quit. *(In this chart, we ignore employees with total working years of 40 years because they are approximately 60 years old, which is the average age for people to quit their job).*
- Employees who work overtime are more likely to resign.
- Employees with the lowest job level are more likely to resign.
- The job role that has the highest percentage rate of resignation is Sales Representative, the difference is quite significant when compared to other roles.

Accessible dashboard link: [Tableau Dashboard](https://public.tableau.com/views/HRAttritionDashboard_17148452730550/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link).

## Conclusion

Based on heatmap correlation analysis, visualization, and machine learning, the features that have the most significant positive and negative correlation with employee attrition are Age, Monthly Income, Over Time, and Total Working Years.

Employees who work overtime, employees who are young (18-26 years old), who have monthly income tends to be low (1k-4k), and who have a relatively low total working years (less than 3 years) are characteristics of employees who are more likely to leave their jobs.

Additional characteristics that can also affect the likelihood of employees to resign include: unmarried employees, employees with Sales Representative roles, and employees with low job levels.

### Recommended Action Items

Some recommended actions that can be done to improve the current employee attrition rate include:  
- The company may be able to provide a clear career path to young employees so that they feel encouraged to stay with the company. This may include development, training, or mentorship programmes specifically for them.
- The company can monitor and manage employees' working hours wisely to avoid work overload and potential attrition.
- Review the company's compensation policy to ensure that the salaries offered are competitive and in line with the contributions that employees make.
- Review the company's onboarding process to ensure that new employees are given the support and resources they need to succeed in their roles.
- Companies can consider employee support or wellbeing programmes such as social support, mentoring programmes, or social activities to help build loyalty.
- Companies can identify Sales Representative positions and then develop specific retention strategies to retain employees who occupy these roles.
- Conduct an analysis to understand the needs and expectations of employees at the lowest levels of the job.
