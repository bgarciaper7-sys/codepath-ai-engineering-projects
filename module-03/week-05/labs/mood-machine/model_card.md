# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  
I developed and tested a rule-based sentiment classifier using Python. The classifier uses predefined positive and negative vocabulary, sentiment scoring, and negation handling to predict the mood of short text messages.

**Intended purpose:**  
The Mood Machine is designed to classify short social media posts and text messages into four categories: positive, negative, neutral, and mixed. The project explores how a simple sentiment analysis system processes language and where its predictions become unreliable.

**How it works (brief):**  
The model first preprocesses text by converting it to lowercase, removing punctuation, and separating words and supported emojis into tokens. It then checks these tokens against predefined positive and negative word lists.

Positive words contribute +1 to the sentiment score, while negative words contribute -1. Negation words such as "not" can reverse the sentiment of the following word. The model also checks for both positive and negative signals within the same message to identify mixed emotions.

I expanded the vocabulary to recognize additional expressions, including the slang word "fire" and the 😍 emoji. These improvements helped the model recognize more informal language, although testing also revealed limitations involving sarcasm and context-dependent meanings.


## 2. Data

## 2. Data

**Dataset description:**  
The dataset contains 11 short text posts stored in `SAMPLE_POSTS` in `dataset.py`. Each post has a corresponding sentiment label in `TRUE_LABELS`. I expanded the starter dataset to include additional language patterns and tested the model using examples involving positive, negative, neutral, and mixed emotions.

**Labeling process:**  
Labels were assigned based on the intended emotional meaning of each message rather than individual keywords alone. Some examples were more difficult to classify because they contained both positive and negative expressions or required interpreting negation.

For example, "I am not happy but I love Python" expresses both negative and positive sentiment, so I treated it as mixed during testing.

**Important characteristics of the dataset:**  
The dataset includes short informal messages, positive and negative vocabulary, mixed sentiment, and examples containing slang and emojis. Additional manual tests explored sarcasm and context-dependent language.

**Possible issues with the dataset:**  
The dataset is very small and may not represent the variety of language used in real conversations. Certain sentiment categories or writing styles may be underrepresented. Sarcasm, slang, cultural expressions, and ambiguous statements can also be difficult to label consistently.

The model achieved 100% accuracy on the 11 labeled sample posts, but this does not establish how accurately it will classify unfamiliar messages.
## 3. How the Rule Based Model Works

**Your scoring rules:**

I implemented a rule-based sentiment classifier with the following logic:

- **Positive and negative scoring:** Each recognized positive word contributes +1, while each negative word contributes -1. Repeated sentiment words are counted individually.
- **Negation handling:** Words such as "not," "never," and "don't" reverse the sentiment of a recognized word immediately following them. For example, "not happy" produces a negative score.
- **Mixed sentiment detection:** The classifier tracks positive and negative signals separately. When both are present, it returns "mixed" instead of relying only on the total score.
- **Emoji recognition:** I improved text preprocessing to recognize supported emojis as individual tokens and added 😍 to the positive vocabulary.
- **Slang recognition:** I expanded the positive vocabulary to include "fire" after discovering that the model initially classified "That concert was fire!" as neutral.
- **Final classification:** If the message is not mixed, a positive score produces "positive," a negative score produces "negative," and a score of zero produces "neutral."

**Strengths of this approach:**

The model is relatively simple, transparent, and easy to debug. Its predictions can be traced to specific vocabulary matches and scoring rules.

It achieved 100% accuracy on the 11 labeled sample posts. It also correctly identified "I am not happy but I love Python" as mixed after I improved the negation-aware detection logic.

**Weaknesses of this approach:**

The model relies heavily on predefined vocabulary and cannot reliably interpret context, sarcasm, or unfamiliar expressions.

For example, it incorrectly classified "Great, another three hours of homework. Just what I needed." as positive because it recognized the word "great" without understanding the sarcasm.

Adding "fire" improved slang recognition but introduced another limitation: the model classified "My house caught on fire" as positive because it could not distinguish literal meaning from slang.

These experiments demonstrate that expanding a rule-based vocabulary can improve certain predictions while creating errors in other contexts.

## 4. How the ML Model Works

**Features used:**  
I explored a machine learning sentiment classifier using scikit-learn. The model uses `CountVectorizer` to convert text into numerical bag-of-words features, representing how often words appear in each message.

It then uses `LogisticRegression` to learn statistical relationships between these features and sentiment labels.

**Training data:**  
The ML model was trained using the same 11 posts in `SAMPLE_POSTS` and their corresponding labels in `TRUE_LABELS` from `dataset.py`.

**Training behavior:**  
The ML model achieved 100% accuracy when evaluated on the same 11 posts used for training.

However, when I tested the new sentence "I am not happy but I love Python," the ML model predicted "negative," while my rule-based classifier correctly predicted "mixed."

This demonstrated that strong training accuracy does not guarantee accurate predictions on unfamiliar text.

**Strengths and weaknesses:**  
A strength of the ML approach is that it learns associations between words and sentiment labels without requiring manually assigned positive and negative word scores.

However, the small training dataset limits the patterns it can learn. The bag-of-words representation also does not explicitly capture word order or negation relationships.

The model may overfit to its training examples and struggle with unfamiliar vocabulary, mixed emotions, sarcasm, and context-dependent language.

A larger, more diverse dataset and evaluation on separate test examples would provide a more reliable assessment of its performance.

## 5. Evaluation

**How I evaluated the models:**

I evaluated both the rule-based classifier and the machine learning classifier using the 11 labeled posts in `dataset.py`.

Both models achieved 100% accuracy (11/11 correct) on this dataset. However, the ML model was evaluated on its own training data, and the rule-based model was evaluated on examples used during its development and refinement.

To investigate how well the models handled unfamiliar language, I also performed manual tests involving negation, mixed emotions, sarcasm, slang, and context-dependent vocabulary.

**Examples of correct predictions:**

1. **"That concert was amazing!"**  
   The rule-based model predicted "positive" because "amazing" appears in its positive vocabulary.

2. **"That concert was fire!"**  
   After I added "fire" to the positive vocabulary, the rule-based model correctly predicted "positive" for this slang expression.

3. **"I am not happy but I love Python"**  
   The rule-based model correctly predicted "mixed" after I implemented negation-aware mixed sentiment detection.

**Examples of incorrect predictions:**

1. **Sarcasm:** "Great, another three hours of homework. Just what I needed."  
   The rule-based model predicted "positive" because it recognized "great" as a positive word. However, the intended meaning was negative or frustrated.

2. **Context-dependent vocabulary:** "My house caught on fire."  
   The rule-based model predicted "positive" because "fire" was included in its positive vocabulary. It could not distinguish literal danger from positive slang.

3. **Mixed sentiment in the ML model:** "I am not happy but I love Python"  
   The machine learning model predicted "negative," while the intended label was "mixed." The model did not successfully recognize both sentiment signals in this unfamiliar sentence.

**Comparison and findings:**

Although both models achieved 100% accuracy on the 11 sample posts, their predictions differed on new examples.

The rule-based model handled the tested negation and mixed-sentiment example better because I explicitly programmed those rules. The ML model learned patterns from labeled examples but struggled to generalize beyond its small training dataset.

These experiments demonstrated that training accuracy alone is insufficient to evaluate a sentiment classifier. Testing on new, diverse examples is necessary to understand its actual strengths and weaknesses.

## 6. Limitations

The Mood Machine has several limitations that affect its reliability and ability to generalize to unfamiliar text.

**1. Small dataset:**  
Both models were evaluated using only 11 labeled posts. This dataset is too small to represent the variety of language, emotions, and writing styles found in real conversations.

**2. Difficulty recognizing sarcasm:**  
The rule-based classifier relies on individual sentiment words rather than the speaker's intended meaning. For example, it incorrectly predicted "positive" for the sarcastic statement "Great, another three hours of homework. Just what I needed."

**3. Context-dependent vocabulary:**  
Words can have different meanings depending on context. After adding "fire" to recognize positive slang, the classifier incorrectly predicted "positive" for "My house caught on fire."

**4. Limited understanding of complex language:**  
Although I implemented negation and mixed-sentiment detection, these rules only handle certain patterns. More complicated sentences, indirect expressions, and unfamiliar phrases may still produce incorrect predictions.

**5. Machine learning generalization:**  
The ML model achieved 100% training accuracy but incorrectly classified an unfamiliar mixed-sentiment sentence as negative. Its small training dataset and bag-of-words representation limit its ability to recognize complex language patterns.

**6. Limited evaluation:**  
Neither model has been evaluated on a large, independent test dataset. Therefore, the reported 100% accuracy should not be interpreted as evidence of reliable performance in real-world applications.

These limitations demonstrate that sentiment analysis requires more than matching words or memorizing patterns. Context, language diversity, and independent evaluation are essential for developing reliable models.

## 7. Ethical Considerations

**Misinterpreting emotional distress:**  
Sentiment classifiers can incorrectly interpret messages expressing sadness, frustration, or distress. For example, my rule-based model classified "My house caught on fire" as positive because it recognized "fire" as a positive slang word. In a real application, this type of error could cause an important message to be misunderstood.

**Language and cultural bias:**  
People communicate emotions differently depending on their language, culture, community, and writing style. Slang, sarcasm, emojis, and informal expressions may not be represented adequately in the dataset. As a result, the model could perform better for certain communication styles than others.

**Privacy considerations:**  
Text messages and social media posts may contain sensitive personal information. If a sentiment classifier were used in a real application, developers would need to consider consent, secure data handling, and whether storing personal messages is necessary.

**Overreliance on predictions:**  
A sentiment prediction should not be treated as a definitive assessment of someone's emotional state. My experiments demonstrated that both models can make incorrect predictions even when they achieve 100% accuracy on their sample dataset.

**Responsible use:**  
The Mood Machine is an educational project designed to explore sentiment analysis and machine learning. It should not be used to make high-stakes decisions about mental health, employment, or other sensitive situations without substantially more validation and appropriate human oversight.

## 8. Ideas for Improvement

Based on my experiments with the rule-based and machine learning classifiers, I identified several opportunities for improvement.

**1. Expand and diversify the dataset:**  
Collect more labeled examples representing different emotions, writing styles, slang, emojis, and cultural expressions. A larger dataset would help evaluate the models more reliably and potentially improve the ML model's ability to generalize.

**2. Improve context awareness:**  
Develop rules that distinguish between different meanings of the same word. For example, "fire" can describe something excellent or a dangerous situation. Context-aware processing could reduce these classification errors.

**3. Improve sarcasm detection:**  
Explore methods for identifying sarcastic expressions that communicate emotions different from their literal wording. My tests demonstrated that positive keywords can appear in negative statements.

**4. Expand negation handling:**  
Improve the model's ability to recognize more complicated negation patterns instead of only reversing sentiment when a negation word appears immediately before a sentiment word.

**5. Experiment with additional ML features and models:**  
Compare `CountVectorizer` with TF-IDF features and explore models that better capture word relationships and context. A pretrained transformer-based sentiment classifier could also be evaluated.

**6. Create an independent test dataset:**  
Separate training and evaluation examples to measure performance on unfamiliar text. This would provide a more meaningful estimate of generalization than evaluating models only on their training data.

**7. Improve explainability and automated testing:**  
Enhance the `explain()` method so its explanations reflect negation and mixed-sentiment rules. Add automated tests covering sarcasm, slang, emojis, negation, and ambiguous vocabulary.

**Conclusion:**  
This project helped me understand how rule-based sentiment analysis differs from machine learning classification. I learned that improving a model requires more than increasing its accuracy on familiar examples. Testing edge cases, understanding limitations, and evaluating unintended consequences are essential parts of AI engineering.
