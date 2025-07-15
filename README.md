# Customer Personality Analysis

This project explores customer data to uncover behavioral insights and improve marketing effectiveness through machine learning and clustering techniques.

---

## Project Goals

- Understand customer traits and purchasing behavior.
- Predict which customers are likely to respond to campaigns.
- Segment customers into distinct groups for targeted marketing.
- Build a dashboard to visualize key insights for business decisions.

---

## What Was Done

1. **Data Cleaning & Preprocessing**
   - Handled missing values and encoded categorical variables.
   - Engineered useful features like `Customer_Tenure_Years` and `Total_Accepted_Campaigns`.

2. **Feature Selection**
   - Used `VarianceThreshold` to remove low-variance features.
   - Scaled features before modeling and clustering.

3. **Predictive Modeling**
   - Trained a **Random Forest Classifier** to predict campaign responders.
   - Tuned for better **recall** to prioritize capturing potential responders.
   - Saved model (`best_rf.pkl`) and scaler for future use.

4. **Clustering**
   - Applied **KMeans** on responder data to find natural customer groups.
   - Used **PCA** to reduce dimensions for visualization.
   - Identified 4 key customer segments with business implications.

5. **Dashboard**
   - Built an interactive **Streamlit app** using **Plotly** visualizations.
   - Included:
     - PCA scatter plot by cluster
     - Cluster sizes
     - Income & age distributions
     - Marital status breakdown per cluster

---

## Business Insights

- Clustered responders show clear behavioral traits, enabling:
  - Premium targeting for high-income clusters
  - Cross-selling strategies for active spenders
  - Budget offers for low-income but engaged users

These insights help improve **ROI on marketing campaigns** and drive **personalized customer engagement**.
