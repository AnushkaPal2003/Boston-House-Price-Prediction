import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Boston House Price Prediction Dashboard")

# Load your results
df_accuracy = pd.read_csv("model_metrics.csv")  # or use a DataFrame directly

# Show raw data
st.subheader("Model Performance Metrics")
st.dataframe(df_accuracy)

# Barplot of R² Scores
st.subheader("R² Score Comparison")
fig, ax = plt.subplots(figsize=(10, 5))
colors = sns.color_palette("husl", len(df_accuracy))
sns.barplot(x="Methods used", y="Accuracy", data=df_accuracy, palette=colors, ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Add dropdown to select model and show details
selected_model = st.selectbox("Select a model to view details", df_accuracy["Methods used"])
model_details = df_accuracy[df_accuracy["Methods used"] == selected_model]
st.write(model_details)