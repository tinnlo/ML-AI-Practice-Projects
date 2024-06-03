## Email

**Subject:** Proposal for Investigating Price Sensitivity in Customer Churn at PowerCo

Dear [Associate Director],

I hope this email finds you well. Following our recent team meeting on SME customer churn at PowerCo, I've collaborated with Estelle to outline a detailed plan to investigate the hypothesis that price sensitivity is a key driver of churn. Below are the steps and considerations for our approach.

### Formulating the Hypothesis as a Data Science Problem

The hypothesis we are testing can be framed as a predictive modeling problem. Specifically, we aim to predict customer churn based on various features, with a particular focus on price sensitivity. We strive to identify customers likely to churn due to pricing and recommend retention strategies such as targeted discounts.

### Steps to Test the Hypothesis

**1. Data Collection**:

- Gather historical data on customer behavior, including churn events.
- Collect information on pricing changes, billing history, and customer discounts.
- Additional relevant data such as customer demographics, competitor pricing, and service data.

**2. Feature Engineering**:

- Identify relevant features influencing churn, including:
    - Price changes and sensitivity
    - Usage patterns
    - Service Quality
    - Demographic information
    - Customer tenure
    - External Factors: Competitor pricing, market trends, and regulatory changes.

**3. Data Preprocessing**:

- Handle missing values and outliers.
- Normalize or scale numerical features.
- Appropriately encode categorical variables.

**4. Model Selection**:

- Consider machine learning algorithms such as logistic regression, decision trees, or ensemble methods.
- Evaluate model performance using metrics like accuracy, precision, recall, and F1-score.

**5. Model Training and Validation**:

- Split the dataset into training and validation sets.
- Train the model on historical data and validate its performance on a separate dataset.

**6. Interpretability Analysis**:

- Visualizing the impact of key factors like price changes, service quality, and customer engagement on churn rates.
- Understand how potential interventions (e.g., price adjustments) and their predicted impact affect the likelihood of churn.

**7. Prediction for Monthly Discount Offers**:

- Apply the trained model to categorize customers based on churn likelihood and identifying high-risk segments.
- Recommend a 20% discount to customers identified as high-risk.

**8. Monitoring and Iteration**:

- Regularly monitor the model's performance and update it as new data becomes available.
- Iterate and refine the model based on ongoing insights and feedback.

### Data Requirements

To proceed with our analysis, we would need access to the following data from PowerCo:

- **Customer Information:** Demographics, business location, industry type, and size.
- **Transactional Data:** Billing history, payment patterns, and contract details over the past 5 years.
- **Churn Data:** Records of churned customers, including dates and reasons if available.
- **Discount Data:** Details on discounts offered to customers
- **Service Data:** Records of service usage, outages, and customer service interactions.
- **Competitive Data:** Market prices and offers from competitors over the same period.

### Timeline

Considering PowerCo's plan to use the predictive model by the 1st working day of each month, we propose the following timeline:

- **Weeks 1-2**: Data collection and preprocessing
- **Week 3**: Model development and validation
- **Week 4**: Final model ready for deployment

We aim to have the model ready well before the deployment deadline. I look forward to discussing this proposal further and welcome any additional insights or suggestions from the team.

Best regards,

Xingting Luo 

Data Scientist, BCG GAMMA  
+46 1xxxxxxxxxx