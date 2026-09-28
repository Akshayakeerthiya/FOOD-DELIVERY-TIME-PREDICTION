# FOOD DELIVERY TIME PREDICTION

## PROJECT OVERVIEW

A machine learning regression project that predicts **food delivery time in minutes** using delivery distance, traffic, weather, vehicle condition, and delivery-person details.

The trained model is deployed as an interactive **Streamlit web application** where users can enter delivery details and get an estimated delivery time.

## LIVE APPLICATION

**STREAMLIT APP:**
https://food-delivery-time-prediction-ns6r7mizkh4cnjwrrrkuh3.streamlit.app/

## OBJECTIVE

* Predict food delivery time.
* Identify important factors affecting delivery duration.
* Compare different regression models.
* Evaluate model performance.
* Deploy the selected model as a web application.

## DATASET

* **Records:** 41,953
* **Features:** 20
* **Target:** `Time_taken(min)`
* **Problem Type:** Regression
* **Train/Test Split:** 80% / 20%

### KEY FEATURES

* Delivery person age and rating
* Delivery distance
* Traffic density
* Weather conditions
* Vehicle condition
* Multiple deliveries
* Pickup delay
* Order and pickup time
* Order type and vehicle type
* Festival and city

## PROJECT WORKFLOW

`Data Understanding → Data Cleaning → Feature Engineering → EDA → Preprocessing → Model Building → Model Comparison → Overfitting Check → Feature Selection → Prediction → Streamlit Deployment`

## FEATURE ENGINEERING

* Converted delivery time from text to numeric format.
* Calculated **Delivery_Distance** using geographical coordinates.
* Extracted order and pickup time features.
* Created **Pickup_Delay**.
* Handled missing and inconsistent values.
* Encoded categorical features.

## MODELS EVALUATED

* Linear Regression
* Random Forest Regressor
* Gradient Boosting Regressor
* Fine-Tuned Gradient Boosting Regressor

## MODEL PERFORMANCE

| MODEL                   |        MAE |       RMSE |         R² |
| ----------------------- | ---------: | ---------: | ---------: |
| Linear Regression       |     4.7693 |     6.0311 |     0.5778 |
| **Random Forest**       | **3.2274** | **4.0859** | **0.8062** |
| Gradient Boosting       |     3.6687 |     4.6121 |     0.7531 |
| Tuned Gradient Boosting |     3.6574 |     4.6031 |     0.7541 |

## SELECTED MODEL

**Random Forest Regressor**

* **MAE:** 3.2274 minutes
* **RMSE:** 4.0859 minutes
* **R²:** 0.8062

The Random Forest model achieved the best test performance among the evaluated models and was selected for deployment.

## OVERFITTING ANALYSIS

| DATASET  |    MAE |     R² |
| -------- | -----: | -----: |
| Training | 1.2012 | 0.9736 |
| Testing  | 3.2274 | 0.8062 |

The difference between training and testing performance indicates some overfitting.

## UNSEEN DATA PREDICTION

```text
Actual Time       : 18.00 minutes
Predicted Time    : 15.24 minutes
Prediction Error  : 2.76 minutes
```

## STREAMLIT DEPLOYMENT

The selected Random Forest model was deployed using **Streamlit**.

The application allows users to provide **8 delivery-related inputs**:

* Delivery Person Rating
* Multiple Deliveries
* Delivery Distance
* Delivery Person Age
* Vehicle Condition
* Pickup Delay
* Road Traffic Density
* Weather

The application then predicts the estimated food delivery time.

## KEY CONCEPTS

* Regression
* Data Cleaning
* Feature Engineering
* Exploratory Data Analysis
* Categorical Encoding
* Random Forest
* Gradient Boosting
* Model Comparison
* Overfitting Analysis
* Feature Importance
* Unseen Data Prediction
* Streamlit Deployment

## TECHNOLOGIES

**Python | Pandas | NumPy | Matplotlib | Seaborn | Scikit-learn | Joblib | Streamlit | Google Colab**

## CONCLUSION

The project demonstrates an end-to-end machine learning workflow, from data preprocessing and model comparison to deployment.

The **Random Forest Regressor** achieved an R² of **0.8062** with an MAE of **3.23 minutes** on the test dataset and was deployed as an interactive **Streamlit application**.
