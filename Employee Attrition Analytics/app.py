import streamlit as st
import pickle
import pandas as pd

def main():
    with open('pipeline.pkl', 'rb') as file:
        pipeline = pickle.load(file) 

    st.title('Employee Attrition Predictor💡')

    st.write('''#### Input some information to predict the attrition of employee''')
        
    gender = st.selectbox('Gender', 
                        ('Male', 'Female'),
                        index=None,
                        placeholder="Select gender...")
    age = st.number_input('Age', 18, 60)
    education_field = st.selectbox('Education Field', 
                                ('Other', 'Medical', 'Life Sciences', 'Marketing',
                                'Technical Degree', 'Human Resources'),
                                index=None,
                                placeholder="Select an education field...")
    marital_status = st.selectbox('Marital Status', 
                                ('Single', 'Married', 'Divorced'),
                                index=None,
                                placeholder="Select marital status...")
        
    department = st.selectbox('Department',
                            ('Human Resources', 'Reserch & Development', 'Sales'),
                            index=None,
                            placeholder="Select department...")
    if department == 'Human Resources':
        job_role = st.selectbox('Job Role', 
                                ('Manager', 'Human Resources'), 
                                index=None, 
                                placeholder="Select the job role...")
    elif department == 'Reserch & Development':
        job_role = st.selectbox('Job Role', ('Manager','Healthcare Representative', 'Research Scientist',
                                'Laboratory Technician', 'Research Director',
                                'Manufacturing Director'),
                                index=None,
                                placeholder="Select the job role...")
    elif department == 'Sales':
        job_role = st.selectbox('Job Role', 
                                ('Manager', 'Sales Executive', 'Sales Representative'),
                                index=None,
                                placeholder="Select the job role...")
    job_level = st.selectbox('Job Level', 
                            (1, 2, 3, 4, 5),
                            index=None,
                            placeholder="Select the job level...")
    overtime = st.selectbox('Overtime', 
                            ('Yes', 'No'),
                            index=None,
                            placeholder="Select overtime...")
    years_in_current_role = st.slider('Years in Current Role', 0, 18)
    years_with_curr_manager = st.slider('Years with Current Manager', 0, 17)
    total_working_years = st.slider('Total Working Years', 0, 40)
    monthly_income = st.number_input('Monthly Income', 1000, 20000, step=1000)
    stockoption_level = st.selectbox('Stock Option Level', 
                                    (0, 1, 2, 3),
                                    index=None,
                                    placeholder="Select the stock option level...")

    ok = st.button('Predict')
    if ok:
        X = pd.DataFrame([[gender, age, education_field, marital_status, department, job_role, job_level,
                        overtime, years_in_current_role, years_with_curr_manager, total_working_years,
                        monthly_income, stockoption_level]],
                        columns=['Gender', 'Age', 'EducationField', 'MaritalStatus',
                        'Department', 'JobRole', 'JobLevel', 'OverTime', 'YearsInCurrentRole',
                        'YearsWithCurrManager', 'TotalWorkingYears', 'MonthlyIncome', 'StockOptionLevel'])
        X = X.replace({'OverTime': {'Yes': 1, 'No': 0}})

        prediction = pipeline.predict(X)
        if prediction == 1.:
            st.subheader('This Employee is Predicted to Resign')
        else:
            st.subheader('This Employee is Predicted to Stay')

    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')
    
    
    st.page_link('https://github.com/MuhamadSyarifFakhrezi', label='Muhamad Syarif Fakhrezi:copyright:')

if __name__ == '__main__':
    main()