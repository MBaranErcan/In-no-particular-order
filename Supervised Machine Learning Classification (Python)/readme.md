```
Mustafa Baran ERCAN
```
# IBM Course Final Project

## Supervised Machine Learning: Classification

**_1. Primary Objective_**

The primary objective of our analysis is to develop a predictive model using the Indian Liver Patient
Dataset (ILPD). This model aims to accurately predict the presence of liver disease based on various
health indicators. For healthcare providers and stakeholders, it can aid in early detection and treatment
planning, potentially improving patient outcomes. Furthermore, it can provide valuable insights into
the factors contributing to liver disease, supporting preventative healthcare measures.

**_2. Dataset Description_**

The dataset I have chosen for this analysis is the Indian Liver Patient Dataset (ILPD. It comprises
583 observations with ten features and one target output. With this analysis, I aim to gain insights into
the relationships between these health indicators in our dataset and the presence of liver disease, which
could be valuable for preventative healthcare measures and early detection of the disease.

![image](https://github.com/user-attachments/assets/fe6ec1fd-00fa-473f-9855-272b6f23cb21)


In our analysis of the Indian Liver Patient Dataset (ILPD), I initially explored the data, identifying key
features and their distributions. During data cleaning, I handled missing values, and converted
categorical variables into a numerical format. Feature engineering involved creating meaningful
feature interactions and preparing the dataset for effective model training.

![image](https://github.com/user-attachments/assets/a021c379-af54-4617-bb5c-60ff834ba04a)



**_3. Training Summary for Classifiers_**

I trained three different classifier models on the Indian Liver Patient Dataset (ILPD) to predict the
presence of liver disease.

_Model 1 – Logistic Regerssion_

This model serves as a simple and interpretable baseline. It achieved a score of approximately 0.76 on
the test set.

![image](https://github.com/user-attachments/assets/538eae09-f7e9-4942-b226-364d35bb467d)


_Model 2 – Random Forest_

This is an ensemble model known for its high predictive power and ability to handle a large number of
features effectively. It achieved a score of approximately 0.75 on the test set.

![image](https://github.com/user-attachments/assets/6806c3da-86bd-4597-bb7a-47c42f85cc4f)


_Model 3 – Support Vector Machine (SVM)_

This model is effective in high-dimensional spaces and is known for its robustness in classification
tasks. It achieved a score of approximately 0.74 on the test set.

![image](https://github.com/user-attachments/assets/f1b0ec0a-39ca-49a8-a1c1-40598fe534ce)


4. **_Model Recommendation_**

Based on the results of my analysis, I would recommend the Logistic Regression model as the
final model. This model achieved the highest accuracy score of approximately 0.76 on the test set,
indicating its strong predictive performance. Moreover, Logistic Regression models are known for
their simplicity and interpretability. It provides a clear insights into how each feature contributes to the
predictions, and can be very valuable in understanding the underlying patterns in the data. Therefore,
in terms of both accuracy and explainability, the Logistic Regression model appears to best fit my
needs for this analysis.

5. **_Summary_**

In analyzing the Indian Liver Patient Dataset (ILPD), Logistic Regression emerged as the top-
performing model with an accuracy of approximately 0.76, closely followed by Random Forest and
Support Vector Machine (SVM). Key insights revealed the importance of features such as 'Total
Bilirubin', 'Direct Bilirubin', and 'Albumin' in predicting liver disease, underscoring the dataset's
relevance to liver health assessment. Our meticulous data preprocessing, including handling missing
values and balancing class distribution through random oversampling, played a pivotal role in
enhancing model performance. These findings not only facilitate accurate disease prediction but also
deepen our understanding of liver health determinants, offering valuable insights for healthcare
practitioners to improve patient outcomes.

**_6. Suggestions_**

To advance my analysis of the Indian Liver Patient Dataset (ILPD), I could consider refining my
model through feature engineering, incorporating domain-specific data, and exploring advanced
modeling techniques like gradient boosting or neural networks. Additionally, optimizing model
parameters, conducting feature importance analysis, and prioritizing interpretability can enhance our
understanding of liver health predictors and improve model performance. Further validation studies
and external validation would strengthen the reliability and generalizability of our findings,
contributing to more effective early detection and intervention strategies for liver disease.

