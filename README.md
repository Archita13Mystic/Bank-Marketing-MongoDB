# Bank Marketing — Term Deposit Subscription Prediction

## 1. Project Overview

This project uses MongoDB and machine learning to analyze bank marketing data and predict whether a customer will subscribe to a term deposit.

The project demonstrates MongoDB database operations, data aggregation, indexing, schema validation, and predictive analytics using Python.

## 2. Technologies Used

- Python
- MongoDB Community Server
- MongoDB Shell (`mongosh`)
- MongoDB Compass
- PyMongo
- Pandas
- Scikit-learn
- Joblib

## 3. Dataset

The project uses the Bank Marketing dataset.

- Total customer records: 45,211
- Total original dataset fields: 17
- Target field: `y`
- `no` outcomes: 39,922
- `yes` outcomes: 5,289

The `duration` field is excluded from the main prediction model because call duration is not known before a marketing call.

## 4. MongoDB Implementation

Database: `bank_marketing_db`

Main collections:

- `customers`: original customer records
- `customer_predictions`: model predictions for test records
- `customers_validation_full_test`: full schema validation demonstration
- `customers_validation_script_test`: automated Python validation tests
- `customers_validation_test`: earlier validation demonstration

The project demonstrates CRUD operations, aggregation pipelines, indexes, query execution analysis, and schema validation.

## 5. Machine Learning

A Random Forest classifier is trained using a preprocessing pipeline that converts categorical fields into numeric features.

- Training records: 36,168
- Testing records: 9,043
- Number of input features before encoding: 15
- Random Forest estimators: 200
- Class imbalance handling: `class_weight="balanced"`
- Selected prediction threshold: 0.40

## 6. Model Results

- Accuracy: 88.02%
- ROC-AUC: 0.7923
- Subscriber precision at threshold 0.40: 40.8%
- Subscriber recall at threshold 0.40: 51.0%
- Subscriber F1-score at threshold 0.40: 0.454

Accuracy should be interpreted alongside precision and recall because the dataset contains substantially more non-subscribers than subscribers.

## 7. Saved Results

The trained pipeline is saved in `random_forest_model.joblib`.

The `customer_predictions` collection contains 9,043 test prediction records. Each record includes the customer reference, predicted subscription, probability of subscription, actual outcome, threshold, and model name.

## 8. How to Run

Activate the project's Python virtual environment, ensure MongoDB is running, and execute the relevant scripts from the project folder.

Examples:

```powershell
python test_mongodb_connection.py
python analysis.py
python index_analysis.py
python schema_validation.py
python RF_train_model.py
python test_saved_model.py
```

`RF_train_model.py` retrains the model and updates the prediction collection. The saved model can be loaded separately using `test_saved_model.py`.

## 9. Limitations

- The dataset has an imbalanced target distribution.
- Predictions are estimates and may be incorrect.
- The reported test metrics apply to the project's fixed train/test split.
- The selected probability threshold reflects a trade-off between precision and recall.
- The project is an educational demonstration, not a production banking decision system.

## 10. Conclusion

The project combines MongoDB data management and analysis with a machine learning pipeline. It stores customer data, demonstrates database features, evaluates subscription predictions, and saves prediction results in MongoDB.

