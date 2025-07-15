import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# Streamlit page title
st.title("Customer Segmentation Dashboard")

# Load PCA scatter data
pca_df = pd.read_csv("data/processed/responders_pca.csv")
cluster_df = pd.read_csv("data/processed/clustered_responders.csv")

# Assign Cluster from cluster_df to pca_df
pca_df['Cluster'] = cluster_df['Cluster'].values

# ______________________ PCA Scatter Plot colored by cluster _____________________
st.subheader("PCA Scatter Plot (CLustered Customers)")
fig = px.scatter(
    pca_df,
    x='PCA1',
    y='PCA2',
    color='Cluster',
    title='PCA Scatter Plot by Cluster',
    color_continuous_scale='Viridis'
)
fig.write_html("dashboards/plotly/pca_scatter.html")
st.plotly_chart(fig)

# ________________________ Cluster Size Bar Chart _________________________

# Count customers per cluster
cluster_counts = cluster_df['Cluster'].value_counts().sort_index()

# Create bar chart
st.subheader("Number of Customers per Cluster")
cluster_size_bar_chart = px.bar(
    x=cluster_counts.index,
    y=cluster_counts.values,
    labels={"x": "Cluster", "y": "Number of Customers"},
    title="Distribution of Customers across Clusters"
)
cluster_size_bar_chart.write_html("dashboards/plotly/cluster_size.html")
st.plotly_chart(cluster_size_bar_chart)

# ________________________ Income by Cluster _________________________
st.subheader("Income Distribution by Cluster")
fig_income = px.box(
    cluster_df,
    x='Cluster',
    y='Income',
    color='Cluster',
    title="Income Distribution across Clusters"
)
fig_income.write_html("dashboards/plotly/income_by_cluster.html")
st.plotly_chart(fig_income)

# ________________________ Age by Cluster ______________________
st.subheader("Age Distribution by Cluster")
fig_age = px.box(
    cluster_df,
    x="Cluster",
    y="Age",
    color="Cluster",
    title="Age Distribution across Clusters"
)
fig_age.write_html("dashboards/plotly/age_by_cluster.html")
st.plotly_chart(fig_age)


# ________________________ Marital Status Breakdown by Cluster _________________
st.subheader("Marital Status Breakdown by Cluster (%)")

# List of one-hot encoded marital status columns
marital_cols = [
    'Marital_Status_Divorced',
    'Marital_Status_Married',
    'Marital_Status_Single',
    'Marital_Status_Together',
    'Marital_Status_Widow'
]

# Group by cluster and compute mean (proportion) for each marital status
marital_dist = cluster_df.groupby('Cluster')[marital_cols].mean() * 100

# Reshape for plotting (long-form DataFrame)
marital_long = marital_dist.reset_index().melt(
    id_vars='Cluster',
    value_vars=marital_cols,
    var_name='Marital Status',
    value_name='Percentage'
)

# Clean labels
marital_long['Marital Status'] = marital_long['Marital Status'].str.replace('Marital_Status_', '')

# Plot stacked bar
marital_status_fig = px.bar(
    marital_long,
    x='Cluster',
    y='Percentage',
    color='Marital Status',
    title="Marital Status Breakdown by Cluster (%)",
    barmode='stack'
)
marital_status_fig.write_html("dashboards/plotly/marital_status_by_cluster.html")
st.plotly_chart(marital_status_fig, use_container_width=True)