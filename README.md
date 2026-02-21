# Basic-Projects-
## 1 :- 
There are main Three projects that are helpfull for beginners as a Data Analysis.
First is project_1 (1).ipynb in that specific project i only did EDA and Feature Engineering for better model taraning and comparision between LINEAR REGRESSION and LOGISTIC REGRESSION 

I found some key insights from the data set that are available in the code.

1st delivery time vs distance :- is a strong positive relationship is observed between delivery distance and delivery time.
2nd delivery time vs traffic conditons mens
LOW traffic shorter delivery time.
MEDIUM traffic medium delivery time.
HIGH traffic longer delivery time.
last delivery time vs weather & delivery time vs time of day & delivery time vs delivery person experience etc.
    OVERALL INSIGHTS among all variables distance and traffic conditions have the strongest impact on delivery time, followed by
wheater conditions and time of a day these pattern explain why the predictive models performed well in these areas.
    Data transformation and encoding the data like traffic conditions wheather condition is very critical for me to predict the delivery time.
but i encode it in the binary type of value like (0,1,2) etc.
then mean mode and varience of the numeric data is given below.
Vehicle_Type_en                1.03500     1.000       0.657060
Weather_Condition_en           1.39500     1.000       1.194950
Traffic_Condition_en           0.85000     1.000       0.640704

THEN come to machine learning model first i predict the value with help of linear regression model with the matrix r2score.
The result is 0.0119 is good prediction for that model. And other matrix resutl is as follows.

Linear Regression Model Evaluation
Mean Squared Error (MSE): 913.8672
Mean Absolute Error (MAE): 25.3516
R-squared (R²): 0.0119

I also use the LogisticRegression model for prediction of the model the result the accuracy of that regression is around 0.325
and other matrix result is as follows.

Accuracy: 0.325
Precision (macro): 0.3761904761904762
Recall (macro): 0.337223778400249
F1-score (macro): 0.3209862810530219
Confusion Matrix:
 [[ 6 11  0]
 [ 2  4  3]
 [ 6  5  3]]

 I also diffentiate the accuracy of two model Linear & Logistic regression.

Linear Regression Accuracy: 0.225
Logistic Regression Accuracy: 0.325
logistic regression is better than linear regression.
linear regression confusion matrix
 [[0,17,0]
 [0,9,0]
 [0,14,0]]
 logistic regression confusion matrix
 [[6,11,0]
 [2,4,3]
 [6,5,3]]

 ## 2 :-
 And second is Assingment_2 in That same dataset i used for model traning but the ML algo is different. 
 I used this Algo in specific Assingment_2 Naive Bayes, KNN, Decision Tree

Objective
The objective of this project is to classify food deliveries as Fast (0) or Delayed (1) using machine learning models. This helps delivery platforms proactively identify late deliveries and improve operational efficiency.

Data Preprocessing & Feature Engineering
Missing values were handled using mean imputation for numerical features and mode imputation for categorical features.

Categorical variables were encoded using Label Encoding.

Geographic distance between restaurant and customer was calculated using the Haversine formula, as distance directly impacts delivery time.

Delivery time was converted into a binary target variable:

0 → Fast (≤ 30 minutes)

1 → Delayed (> 30 minutes)

To avoid data leakage, normalization was applied after train–test split.

Model Evaluation & Comparison Comparative Performance Table Model Accuracy Precision Recall F1-Score Business Interpretation Naive Bayes Moderate Moderate Lower Moderate Misses some delayed cases KNN High Moderate High High Detects delayed deliveries well
Decision Tree High High High Highest Balanced & explainable 4. Linking Metrics to Business Decisions

Recall is critical for delayed delivery detection because missing a delayed order negatively affects customer satisfaction.

Precision is important to avoid falsely labeling fast deliveries as delayed, which can cause unnecessary interventions.

Model-wise Interpretation:

Naive Bayes: Fast and simple but lower recall, making it less reliable for identifying delayed deliveries.

KNN: High recall makes it effective for detecting delayed orders, but it lacks interpretability and is computationally expensive.

Decision Tree: Provides a strong balance of precision and recall while also offering clear decision rules, making it suitable for operational use.

Visualization Insights
Confusion matrices showed that the Decision Tree produced fewer false negatives for delayed deliveries.

ROC curves indicated that the Decision Tree achieved the best class separation ability.

Feature importance analysis from the Decision Tree revealed that distance, traffic conditions, and weather are the most influential factors affecting delivery delays.

Final Recommendation
The Decision Tree classifier is the most suitable model for this task.

Reason:

Accurately predicts delayed deliveries (high recall)

Maintains strong overall accuracy

Offers interpretability for business decision-making

Helps logistics teams understand why delays occur

Conclusion
This project demonstrates that while all three models can classify delivery status, the Decision Tree model best satisfies both technical performance and business requirements. Its ability to balance accuracy with interpretability makes it ideal for real-world food delivery systems.


## 3 :- 
In this i used another type of dataset and i use the same ML algo's.
I used this Algo in specific Assingment_3 Naive Bayes, KNN, Decision Tree.

Final Conclusion

In this project, the Global_Pollution_Analysis.csv dataset was used to study pollution severity across different countries using machine learning classification techniques. The data was first cleaned by handling missing values, removing outliers, encoding categorical variables, and scaling pollution-related features to ensure reliable analysis.

New features such as energy consumption per capita and yearly pollution trends were created to enhance understanding of pollution patterns. Countries were then classified into Low, Medium, and High pollution levels based on pollution indices.

Three classification models—Naive Bayes, K-Nearest Neighbors (KNN), and Decision Tree—were implemented and evaluated using accuracy, precision, recall, F1-score, and confusion matrices. Among these models, the Decision Tree classifier performed the best, indicating that pollution severity depends on complex, non-linear relationships between pollution indicators.

The results highlight that countries with higher pollution indices require targeted environmental policies and improved pollution control measures. Overall, this project demonstrates how data preprocessing, feature engineering, and machine learning models can be effectively used to analyze environmental pollution and support data-driven decision making.

Actionable Policy Recommendations
Model results show that countries classified under High Pollution Severity also exhibit higher average energy recovery potential. This indicates strong opportunities for waste-to-energy systems and industrial heat recovery.

• High-severity countries should prioritize renewable energy integration and industrial emission controls.

• Medium-severity regions should focus on efficiency improvements and pollution monitoring to prevent escalation.

• Low-severity countries should maintain current environmental policies and invest in sustainable growth strategies.

These recommendations directly align with the classification outputs produced by the Decision Tree and KNN models.