import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay, auc, confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score, roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from colorama import Fore, Style
import time

class Timer:    
    def __enter__(self):
        self.tick = time.time()
        return self
    def __exit__(self, *args, **kwargs):
        self.tock = time.time()
        self.elapsed = self.tock - self.tick

# check nan values ratios
def check_nan_value_ratio(df):
    nan_ratios = df.isna().sum() / len(df)
    for i, ind in enumerate(nan_ratios):
        percentage = ind * 100
        formatted_percentage = f"%{percentage:.5f}"
        print(f"{nan_ratios.index[i]} : {formatted_percentage}")

def find_continuous_columns(df)->[]:
    continuous_columns = [col for col in df.select_dtypes(include='number').columns if df[col].nunique() > 10]
    print("Continuous Features:", continuous_columns)
    return continuous_columns
    
def detect_outliers(df,features):
    outlier_indices = []
    for c in features:
        # 1st quartile
        Q1 = np.percentile(df[c],25)
        # 3rd quartile
        Q3 = np.percentile(df[c],75)
        # IQR
        IQR = Q3 - Q1
        # Outlier step
        outlier_step = IQR * 1.5
        # detect outlier and their indeces
        outlier_list_col = df[(df[c] < Q1 - outlier_step) | (df[c] > Q3 + outlier_step)].index
        # store indeces
        outlier_indices.extend(outlier_list_col)
    outlier_indices = Counter(outlier_indices)
    multiple_outliers = list(i for i, v in outlier_indices.items() if v > 2)
    return multiple_outliers
    
def plot_model_roc_auc_curve(models_list:list, test_df):
    plt.figure(figsize=(7, 5))
    for model in models_list:
        fpr, tpr, _ = roc_curve(test_df['True'], test_df[model])
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, label=f'{model} (AUC = {roc_auc:.2f})')

    # Plot random guess line
    plt.plot([0, 1], [0, 1], 'r--', label='Random Guess')

    # Set labels and title
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves for Two Models')
    plt.legend()
    plt.show()

def run_model(i, models, df, predictions, X_train, X_test, y_train, y_test):
    target_names=['0','1']
    model = list(models.values())[i]
    model.fit(X_train, y_train) # Train model
    
    # Make predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    predictions[list(models.keys())[i]] = model.predict_proba(X_test)[:, 1]
    
    print(list(models.keys())[i])
    print("Training set performance")
    print(type(y_train_pred[0]))
    print(classification_report(y_train, y_train_pred, target_names=target_names))
    model_train_rocauc_score = roc_auc_score(y_train, y_train_pred)
    print(f"Roc-Auc Score Training set: {model_train_rocauc_score}")
    print("Test set performance")
    print(classification_report(y_test, y_test_pred, target_names=target_names))
    model_test_rocauc_score = roc_auc_score(y_test, y_test_pred) #Calculate Roc
    print(f"Roc-Auc Score Test set: {model_test_rocauc_score}")
    print(f"{Fore.BLUE}{Style.BRIGHT}_."*40) # print 50 times = character
    print(Style.RESET_ALL, end="")
    
def make_prediction(models, df):
    X = df.iloc[:,:-1]
    y= df.iloc[:,-1]
    zero_ratio = np.round(len(y[y==0]) / len(y), decimals=2)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    predictions={'True': y_test}

    with Timer() as timer_time:
        for i in range(len(list(models))):
            run_model(i, models, df, predictions, X_train, X_test, y_train, y_test)
        print(predictions)
        plot_model_roc_auc_curve(list(models.keys()), predictions)
    print(f"Fit + Predict time (seconds): {timer_time.elapsed}")   
    return timer_time.elapsed
