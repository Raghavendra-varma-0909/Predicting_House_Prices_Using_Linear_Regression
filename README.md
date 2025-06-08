
# 🏡 House Price Prediction using Simple Linear Regression

## 🎯 Aim
Build a simple linear regression model to predict house prices based on features like the number of bedrooms and square footage.

## 📄 Description
This project uses a small synthetic dataset of house prices and applies linear regression to predict house prices. The dataset includes features such as:
- Number of bedrooms
- Square footage

The model is trained and tested using Scikit-learn and performance is evaluated using metrics such as Mean Squared Error (MSE) and R² score.

## 🧰 Technologies Used
- Python
- Pandas
- Scikit-learn
- NumPy

## 📁 Project Structure
```
house-price-prediction/
├── house_price_prediction.py
├── README.md
└── requirements.txt
```

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Run the script:
```bash
python house_price_prediction.py
```

## 📊 Sample Output
- **Model Coefficients**: `[bedrooms ≈ 0, square_feet = 100]`
- **Intercept**: `50000`
- **Prediction Formula**:  
  ```
  price = 100 * square_feet + 50000
  ```

## 📚 What You Learn
- Fundamentals of linear regression
- Data preprocessing and splitting
- Model training and evaluation
- Making predictions with Scikit-learn

---

📌 Note: This is a basic introduction to regression. In real-world scenarios, more features and advanced models would be used.

