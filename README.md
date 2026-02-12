# Medical AI 101
This repository is to build the foundation and expertise in medical AI.

## How to best use this Resource?
1. Create a [Github profile](https://github.com)
2. Star the repository so that you receive the latest updates.
![image](https://github.com/user-attachments/assets/8c401690-42dc-48df-94f5-506b63be0f4a)
3. The whole page has been broken down in chapters with the time it should take to cover, where you can read about the theory and practical exercises.

## Run in Google Colab
Use the `Open In Colab` badge next to any notebook.
Then run this once in Colab so local `data/` paths work:
```python
import os
if not os.path.exists("/content/Medical-AI-101"):
    !git clone https://github.com/aaekay/Medical-AI-101.git
%cd /content/Medical-AI-101/chapters
```

## Module 0 - Jupyter + Python Bootcamp for Medical Students
Notebook: [00_jupyter_python_basics_for_medical_students.ipynb](chapters/00_jupyter_python_basics_for_medical_students.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aaekay/Medical-AI-101/blob/main/chapters/00_jupyter_python_basics_for_medical_students.ipynb)
### Why this module?
This chapter helps complete beginners run notebooks safely, understand basic Python, and work with simple medical tables before moving into AI concepts.
### Learning objectives
1. Run and troubleshoot Jupyter notebook cells.
2. Learn Python basics with clinical examples (variables, lists, conditions, loops, functions).
3. Load and inspect a small synthetic patient dataset using pandas.
4. Make simple plots and interpret them.
5. Build a toy risk score without training a model.
### What you'll do
1. Practice notebook workflow and fix common errors.
2. Write small Python snippets tied to clinical variables.
3. Explore and clean a CSV with missing values.
4. Visualize data and adjust a follow-up threshold interactively.

## Module 0.1 - Introduction
1. There is no shortcut to understanding and learning the foundational concept of anything.
2. Read the modules step by step at your own pace. Keep on coming back if you don't understand anything, or do ChatGPT if you are not able to understand it. Like "dumb it down for me".
3. Audience: Anyone who wants to start from the basics.

## Module 0.2 - Building the basic understanding
Go to this website and read all the chapters
1. Book here: [Nueral Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/chap1.html). Skip the warning
Now, you are ready to start in the field of Healthcare imaging. Let's start with the understanding of the basic principles of pictures in radiology

## Module 0.3 - Building the foundation of mathematics
If you really want to deep dive into the theoretical part of machine learning and AI, then you need to be good at maths. Otherwise you can skip the mathematics.
### Mathematics concepts
1. Linear algebra - refer to 3Blue1Brown lecture series - [Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra)

### Advanced users
If you don't have Linear algebra or a college-level understanding of mathematics, refer to this book. You need to be patient while following the book [Click](https://mml-book.github.io/book/mml-book.pdf)

## Module 1 - The Evolution of the "AI Doctor" (1970s - 2025)
Notebook: [01_history_of_medical_ai.ipynb](chapters/01_history_of_medical_ai.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aaekay/Medical-AI-101/blob/main/chapters/01_history_of_medical_ai.ipynb)
### Why this module?
This chapter de-mystifies AI by showing how medical problems shaped each era of AI, and why the methods evolved over time.
### Learning objectives
1. Distinguish between rule-based AI and modern machine learning.
2. Understand the "AI Winter" in medicine and why early promises failed.
3. Identify the clinical bottlenecks that led to deep learning and generative AI.
4. Evaluate the trade-off between explainability (rules) and performance (neural nets).
### What you'll do
1. Explore a timeline from MYCIN to LLMs.
2. Build a tiny expert system and fix a rule.
3. Adjust a risk model weight and see how predictions change.
4. See why pixels need deep learning and why LLMs can help with notes.

## Module 2 - Medical Data Fundamentals: Garbage In, Harm Out
Notebook: [02_medical_data_fundamentals.ipynb](chapters/02_medical_data_fundamentals.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aaekay/Medical-AI-101/blob/main/chapters/02_medical_data_fundamentals.ipynb)
### Why this module?
This chapter shows why medical AI projects fail when data quality, units, leakage, representation, and privacy checks are skipped.
### Learning objectives
1. Identify common EHR data pitfalls before any model training.
2. Compare missing-data strategies and understand their trade-offs.
3. Detect unit mismatch and label leakage in readmission data.
4. Audit subgroup representation and preview de-identification.
5. Export a cleaned handoff table for Module 3 modeling.
### What you'll do
1. Audit a synthetic, intentionally dirty readmission dataset.
2. Use widgets to compare missing-data and unit-handling choices.
3. See how a leaky feature can create fake performance.
4. Generate `data/module_02_cleaned_for_module_03.csv` for the next chapter.

## Module 3 - First Clinical Prediction Model (Traditional ML)
Notebook: [03_traditional_ml_readmission.ipynb](chapters/03_traditional_ml_readmission.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aaekay/Medical-AI-101/blob/main/chapters/03_traditional_ml_readmission.ipynb)
### Why this module?
This chapter is the first full model-building workflow: framing a prediction task, training two baseline models, and understanding clinical trade-offs.
### Learning objectives
1. Define model features (`X`) and label (`y`) correctly for readmission prediction.
2. Train and compare Logistic Regression and Decision Tree baselines.
3. Evaluate sensitivity, specificity, precision, F1, and ROC-AUC.
4. Tune classification threshold and observe clinical trade-offs.
5. Perform basic error analysis on missed high-risk patients.
### What you'll do
1. Load the cleaned Module 2 dataset.
2. Train baseline models using structured EHR-like features.
3. Compare confusion counts and key metrics at threshold 0.50.
4. Save test predictions to `data/module_03_test_predictions.csv` for Module 4.

## Module 4 - Evaluating Models in Medicine: Beyond Accuracy
Notebook: [04_evaluating_models_in_medicine.ipynb](chapters/04_evaluating_models_in_medicine.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aaekay/Medical-AI-101/blob/main/chapters/04_evaluating_models_in_medicine.ipynb)
### Why this module?
This chapter shows how model evaluation becomes a clinical policy decision when thresholds, capacity, and trade-offs are explicit.
### Learning objectives
1. Compare ROC-AUC, PR-AUC, sensitivity, specificity, precision, and F1.
2. Explore threshold trade-offs interactively.
3. Simulate top-K triage under limited intervention capacity.
4. Choose thresholds using explicit false-negative and false-positive costs.
5. Generate a policy summary table for stakeholder discussion.
### What you'll do
1. Load Module 3 test predictions from `data/module_03_test_predictions.csv`.
2. Plot ROC and precision-recall curves for logistic regression and decision tree.
3. Tune thresholds and see how workload and miss rates change.
4. Save policy recommendations to `data/module_04_threshold_policy_summary.csv`.

## Module 5 - Deep Learning in Chest X-ray (Top-Down Track)
Dataset setup (one-time, no Kaggle API):
`python scripts/setup_chest_xray_from_gdrive.py`

### Part A: Problem Framing and Method Map
Notebook: [05a_chest_xray_problem_and_method_map.ipynb](chapters/05a_chest_xray_problem_and_method_map.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aaekay/Medical-AI-101/blob/main/chapters/05a_chest_xray_problem_and_method_map.ipynb)
1. Start with a clinical triage problem in chest radiology.
2. Compare rule-based methods, traditional ML, and deep learning.
3. Build a handcrafted-feature baseline and inspect ROC vs PR behavior.

### Part B: Labels, Data Splits, and CNN Training
Notebook: [05b_chest_xray_labels_and_deep_learning_training.ipynb](chapters/05b_chest_xray_labels_and_deep_learning_training.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aaekay/Medical-AI-101/blob/main/chapters/05b_chest_xray_labels_and_deep_learning_training.ipynb)
1. Work with a real-world chest X-ray dataset structure.
2. Audit labels, build balanced subsets, and train a compact CNN.
3. Save training history and prediction files for downstream analysis.

### Part C: Metrics, Thresholds, and Hyperparameter Decisions
Notebook: [05c_chest_xray_metrics_thresholds_and_hyperparameters.ipynb](chapters/05c_chest_xray_metrics_thresholds_and_hyperparameters.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aaekay/Medical-AI-101/blob/main/chapters/05c_chest_xray_metrics_thresholds_and_hyperparameters.ipynb)
1. Compare PR-AUC and ROC-AUC in an imaging context.
2. Use interactive threshold and cost-based policy selection.
3. Compare hyperparameter runs and export a model policy card.



### To Do
- [ ] Add Module 6
