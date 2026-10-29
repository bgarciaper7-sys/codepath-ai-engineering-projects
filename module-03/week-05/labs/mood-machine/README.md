# The Mood Machine: Sentiment Analysis with Python

## Project Overview

The Mood Machine is a Python sentiment analysis project developed as part of CodePath AI Engineering 101.

The project compares two approaches to classifying short text messages into four sentiment categories: **positive, negative, neutral, and mixed**.

1. **Rule-Based Sentiment Classifier:** Uses predefined vocabulary, sentiment scoring, negation handling, and mixed-emotion detection.
2. **Machine Learning Classifier:** Uses scikit-learn's CountVectorizer and LogisticRegression to learn patterns from labeled text.

I improved the rule-based classifier, expanded its vocabulary, tested difficult language patterns, and compared its predictions with a machine learning model.

## Technologies & Tools

- Python
- scikit-learn
- Regular Expressions (Regex)
- Natural Language Processing (NLP)
- VS Code
- Git and GitHub

## Features & Improvements

### 1. Text Preprocessing

Improved text preprocessing to:

- Convert text to lowercase.
- Remove punctuation that is not part of recognized tokens.
- Separate words and supported emojis into tokens.
- Preserve apostrophes in words such as "don't."

### 2. Sentiment Scoring

Implemented a scoring system where:

- Positive words contribute +1.
- Negative words contribute -1.
- Repeated sentiment words contribute individually.
- Negation words such as "not" reverse the sentiment of the following recognized word when immediately adjacent.

### 3. Mixed Sentiment Detection

Added logic to recognize messages containing both positive and negative sentiment signals.

**Example:**

Input: `I am not happy but I love Python`

Prediction: `mixed`

### 4. Emoji and Slang Recognition

Expanded the positive vocabulary to include additional expressions such as:

- `hopeful`
- `proud`
- `😍`
- `fire`

These changes improved the model's recognition of informal language.

### 5. Machine Learning Comparison

Trained a machine learning classifier using:

- CountVectorizer for bag-of-words text representation.
- LogisticRegression for sentiment classification.
- The same 11 labeled posts used to evaluate the rule-based classifier.

## Project Structure

```text
├── dataset.py          # Sentiment vocabulary and labeled sample posts
├── mood_analyzer.py    # Rule-based sentiment classifier
├── main.py             # Rule-based evaluation and interactive demo
├── ml_experiments.py   # Machine learning training and evaluation
├── model_card.md       # Model evaluation, limitations, and ethical considerations
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## Installation & Usage

**1. Clone the repository**

```bash
git clone <repository-url>
cd <repository-folder>
```

Replace the placeholders with the repository URL and folder name.

**2. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**3. Run the rule-based model**

```bash
python main.py
```

**4. Run the machine learning model**

```bash
python ml_experiments.py
```

Both programs allow interactive sentiment predictions.

## Evaluation Results

Both models achieved 100% accuracy on the 11 labeled sample posts.

| Model | Accuracy | Evaluation |
|---|---|---|
| Rule-Based Classifier | 100% (11/11) | Development dataset |
| Machine Learning Classifier | 100% (11/11) | Training dataset |

**Important:** These results do not represent accuracy on an independent test dataset. Additional testing revealed errors on unfamiliar messages.

### Edge Case Testing

| Test sentence | Model | Prediction | Intended sentiment |
|---|---|---|---|
| That concert was amazing! | Rule-based | Positive | Positive |
| That concert was fire! | Rule-based | Positive | Positive |
| I am not happy but I love Python | Rule-based | Mixed | Mixed |
| I am not happy but I love Python | ML | Negative | Mixed |
| Great, another three hours of homework. Just what I needed. | Rule-based | Positive | Negative (sarcasm) |
| My house caught on fire. | Rule-based | Positive | Negative |

## Key Findings

The experiments revealed several important limitations:

- **Sarcasm:** Positive vocabulary does not always indicate positive sentiment.
- **Context:** The same word can have different meanings depending on how it is used.
- **Vocabulary coverage:** Expanding sentiment word lists can improve some predictions while introducing new errors.
- **Generalization:** High accuracy on training examples does not guarantee accurate predictions on unfamiliar messages.
- **Dataset size:** Eleven labeled examples are insufficient for reliable real-world sentiment classification.

## Model Card

For additional details about the dataset, scoring rules, evaluation, limitations, ethical considerations, and proposed improvements, see [Model Card](model_card.md).

## What I Learned

This project helped me develop a better understanding of natural language processing, rule-based classification, and introductory machine learning.

I practiced implementing Python logic, debugging classification errors, designing edge-case tests, and evaluating the consequences of modeling decisions.

One of my most important takeaways was that improving a classifier on one example can introduce errors elsewhere. Testing beyond the original dataset is essential for understanding whether a model is actually reliable.

## Future Improvements

- Expand the labeled dataset.
- Create separate training and test datasets.
- Improve context-sensitive sentiment detection.
- Explore TF-IDF and more advanced NLP models.
- Add automated regression tests.
- Improve prediction explanations for negation and mixed emotions.

## Disclaimer

This is an educational sentiment analysis project. Its predictions should not be used for mental health assessments or other high-stakes decisions.