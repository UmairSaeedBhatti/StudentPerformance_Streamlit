import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
df = pd.read_csv("StudentPerformanceFactors.csv")

st.set_page_config(layout="wide")
st.title("📊 Student Performance Dashboard")

# Sidebar Filters
st.sidebar.header("🔍 Filter Students")
gender = st.sidebar.multiselect("Gender", options=df["Gender"].unique(), default=df["Gender"].unique())
school_type = st.sidebar.multiselect("School Type", options=df["School_Type"].unique(), default=df["School_Type"].unique())
motivation = st.sidebar.multiselect("Motivation Level", options=df["Motivation_Level"].unique(), default=df["Motivation_Level"].unique())

# Apply filters
filtered_df = df[
    (df["Gender"].isin(gender)) &
    (df["School_Type"].isin(school_type)) &
    (df["Motivation_Level"].isin(motivation))
]

st.subheader("📈 Summary Statistics")
st.dataframe(filtered_df.describe())

# Distribution of Exam Score
st.subheader("🎯 Exam Score Distribution")
fig1 = sns.histplot(filtered_df["Exam_Score"], kde=True)
st.pyplot(fig1.figure)

# Correlation Heatmap
st.subheader("📌 Correlation Heatmap")
numerical_cols = df.select_dtypes(include='number').columns
corr = filtered_df[numerical_cols].corr()
fig2 = sns.heatmap(corr, annot=True, cmap="coolwarm")
st.pyplot(fig2.figure)

# Scatter Plots: Exam Score vs Important Features
st.subheader("📉 Exam Score vs Key Numerical Features")
for col in ['Hours_Studied', 'Attendance', 'Previous_Scores', 'Sleep_Hours']:
    fig = sns.scatterplot(data=filtered_df, x=col, y="Exam_Score")
    plt.title(f"Exam Score vs {col}")
    st.pyplot(fig.figure)
    plt.clf()
