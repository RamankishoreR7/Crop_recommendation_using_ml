Crop Recommendation System using Machine Learning

This project is a Machine Learning-based system that recommends the most suitable crop to grow based on soil and environmental conditions. Instead of relying on guesswork, it uses data to make better agricultural decisions.

Project Overview

Choosing the right crop depends on factors like soil nutrients, temperature, humidity, pH, and rainfall. This project uses a Random Forest Classifier to analyze these inputs and suggest the best crop.

Features

- Predicts the most suitable crop based on input values  
- Uses Random Forest for reliable performance  
- Simple and easy-to-understand ML pipeline  
- Can be extended into a web or mobile application  

Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  

Project Structure

.
├── app.py
├── crop_recommendation.csv
├── crop_model.joblib
├── crop_recommendation_model.ipynb
└── README.md

How It Works

1. Load the dataset using Pandas  
2. Prepare the data for training  
3. Split the dataset into training and testing sets  
4. Train a Random Forest model  
5. Make predictions based on input values  
6. Evaluate performance using accuracy score and classification report  

How to Run

1. Clone the repository  
git clone https://github.com/your-username/crop-recommendation.git  

2. Go to the project folder  
cd crop-recommendation  

3. Install dependencies  
pip install pandas numpy scikit-learn  

4. Run the script  
python main.py  

Example Input

N = 90  
P = 42  
K = 43  
Temperature = 20  
Humidity = 82  
pH = 6.5  
Rainfall = 200  

Example Output

Recommended Crop: Rice  

Why This Project

This project helps in making better agricultural decisions using data. It can improve crop yield and reduce resource waste by suggesting the right crop for given conditions.

Future Improvements

- Add a user interface using Streamlit  
- Deploy the model online  
- Use real-time weather data  
- Try advanced models for better accuracy  

Author

Raman Kishore Aspiring AI/ML Engineer 

Final Note

This is a simple and practical Machine Learning project focused on solving a real-world problem. It can be further improved and extended into a full application.