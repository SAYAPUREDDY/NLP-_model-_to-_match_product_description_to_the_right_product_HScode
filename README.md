# NLP-_model_to_match_product_description_to_the_right_product_HScode
This project is focused on building a Natural Language Processing (NLP) model to accurately match product descriptions to their corresponding Harmonized System (HS) codes. The model is trained on a custom dataset and utilizes lemmatization, TF-IDF vectorization, and a Multinomial Naive Bayes (NB) classifier.

## **Table of Contents**
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Model Workflow](#model-workflow)
4. [Preprocessing](#preprocessing)
5. [Model Training](#model-training)
6. [Evaluation](#evaluation)
7. [Results](#results)
8. [How to Use](#how-to-use)

## **Introduction**
Matching product descriptions to their correct HS codes is crucial for international trade compliance, but it can be a challenging task due to the diversity of product descriptions. This project aims to simplify this process by developing an NLP model that can automatically classify product descriptions into the correct HS code category.

## **Dataset**
The dataset used in this project was custom-created. It includes product descriptions generated manually and with the assistance of ChatGPT. Additionally, Amazon product descriptions and specifications were used for testing and validation purposes.

## **Model Workflow**
1. **Data Collection**: Generated and collected product descriptions along with their respective HS codes.
2. **Text Preprocessing**: Applied various preprocessing techniques including lemmatization.
3. **Feature Extraction**: Utilized TF-IDF vectorization to convert text data into numerical format.
4. **Model Training**: Trained a Multinomial Naive Bayes classifier on the processed data.
5. **Evaluation**: Tested the model on unseen data from Amazon product descriptions.

## **Preprocessing**
- **Lemmatization**: Reduced words to their base form to ensure consistency in the text data.
- **TF-IDF Vectorization**: Used Term Frequency-Inverse Document Frequency (TF-IDF) to transform text data into numerical features. This method emphasizes important words while reducing the impact of commonly used words.

## **Model Training**
- **Multinomial Naive Bayes**: Chosen due to its effectiveness in text classification tasks, especially when dealing with categorical data like HS codes.
- The model was trained on the preprocessed dataset and hyperparameters were tuned for optimal performance.

## **Evaluation**
The model was tested using Amazon product descriptions and specifications to ensure its ability to generalize to real-world data. Accuracy, precision, recall, and F1-score were the main metrics used for evaluation.

## **Results**
The model achieved a satisfactory accuracy and demonstrated its ability to classify a wide variety of product descriptions into the correct HS code categories. Specific performance metrics can be found in the results section of the code.

## **How to Use**
1. Clone this repository: 
   ```bash
   git clone https://github.com/your-repository/product-description-to-hscode.git
