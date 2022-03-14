
# Innis-classification-project



## About the Project

### Project Goals

##### This project aims to statistically explore and formulate the factors that contribute to observed increase in customer churning at TelCoCo with a main focus to answer the question '..why are customers parting ways with company services?' Inferred findings are to be used in advicing possible measures to be implemented to reduce the current customer loss rate.¶
 

### Project Description

#### Recently, customer churning in Telco Company is becoming concerning. This has been noticed by the deparment heads and a need to respond is imminent. The company keeps records on its customers and aims to statistically understand the cause of churning and whether, if possible, infer meaning through modeling that willl guide our business recommendations. Project delivered via csv file.


### Initial Questions

>> -  How does **churn** rate vary?
>> -  **Billing format**, in theory may play big role in churning, can we find any effect of this feature?
>> -  Do **phone service** affect churn rate?
>> -  How about if the customer has **multiple phone lines**, how is churn rate affected?

### Data Dictionary

#### The following are encoded words and their meaning as used in this project:

Variable	Meaning
churn	loosing customer/ attrition
enc_... 	encoded variable


### Steps to Reproduce

#### To reproduce this project:

You will need an env.py file that contains the hostname, username and password of the mySQL database that contains the telco_churn database. Concatenate the tables internet_service_types, contract_types, customer_contracts, customer_payments, and payment_types. Store that env file locally in the repository.clone my repo (including the acquireTelco.py and prepareTelco.py) (confirm .gitignore is hiding your env.py file). Libraries used are pandas, matplotlib, seaborn, numpy, sklearn. With these libraries in your machine installed, you should be able to run customer_churn_telcoco.ipynb report.


### The Plan

#### Wrangle

Modules (acquireTelco.py + prepareTelco.py)

NOTE: User-defined functions for acquiring and preparing the data are created and called directly within the respective modules (acquireTelco.py & prepareTelco.py).

#### Procedure to successfully run replicated project

Entire project ran on customer_churn_telcoco.ipynb
Steps:

- import all files and libraries
- acquire data from the acquireTelco.py
- acquire data from the prepareTelco.py (cleans, splits, drop unnecessary columns)
- call the prepare function in notebook (this code splits into train, validate & test data and saves these files in main file)

NOTE: This project splits the data into train: 56%, validate: 24%, test: 20% ratios

### Questions of interest:

How does churn rate vary?
Billing format, in theory may play big role in churning, can we find any effect of this feature?
Do phone service affect churn rate?
How about if the customer has multiple phone lines, how is churn rate affected?


correlation: 2 continuous variables, normally distributed, testing for LINEAR correlation only (H_0: Not linearly dependent)

independent t-test: 1 continuous, somewhat normally distributed variable, one boolean variable, equal variance, independent (H_0: population mean of each group is equal)


Summary (report.ipynb)
Following your exploration section, you summarize your analysis (in a markdown cell using natural language): what you found and how you will use it moving forward.

This includes key takeaways from all the questions answered in explore, a list of which features will be used in modeling and why, and which features will not move forward and why. You may only call out a few of these features in the presentation, but having that there for reference is important in a report. A group of features may have the same reason why, and those can be mentioned together.

Modeling
Select Evaluation Metric (Report.ipynb)
Clear communication as to how you evaluated and compared models.

What metric(s) did you use and why? For example, in one case, you may decide to use precision over accuracy. If so, why? If you use multiple metrics, how will you decide which to select if metric is better for model A but another is better for model B? Will you rank them? Find a way to aggregate them into a single metric you can use to rank?

Evaluate Baseline (Report.ipynb)
Having a baseline tells you whether a model you build using the features you selected is any better than predicting by using only the target variable. One way a baseline is created in classification is by making predictions purely based on the most common outcome class, like predicting that all titanic passengers will die, becuase the majroity did die. By doing that, you end up with the highest accuracy without using extra information from features. The baseline is based on the training dataset. For a continuous target variable, the baseline could be predicting that all salaries will be the median salary of our labeled train data. The predictions should be made on the training data using this information (like the predicted value, y_hat, for all passengers "survived" == 0) and then performance evaluated to measure your models against. If any model you build does not perform as well as a baseline that uses no features, then your features are not significant drivers of the outcome.
Develop 3 Models (Report.ipynb)
The 3 models can differ based on the features used, the hyperparameters selected, and/or the algorithm used to fit the data.
Evaluate on Train (Report.ipynb)
All models should be evaluated on train: the training sample is our largest sample, and it is a sample of data we have to both fit the model AND see how the model performs. We should never skip straight to validate. We would be missing out on valuable observations.
Evaluate on Validate (Report.ipynb)
*The top models should be evaluated with the validation sample dataset. It is important to use the validate sample for checking for any overfitting that may have occurred when fitting the model on train. If you are creating 10's of models, it is also important to only validate a handful of your top models with the Validate dataset. Otherwise, your data will have seen validate as much as train and you could accidentally introduce some implicit bias based on data and results you see while validating on so many models. *
Evaluate Top Model on Test (Report.ipynb)
Your top performing model, and only your top performing model should be evaluated on your test dataset. The purpose of having a test dataset to evaluate only the final model on is to have an estimate of how the model will perform in the future on data it has never seen.
Report (Final Notebook)
code commenting (Report.ipynb)
Your code contains code comments that are helpful to the reader in understanding what each blocks/lines of code are doing.
markdown (Report.ipynb)
Notebook contains adequate markdown that documents your thought process, decision making, and navigation through the pipeline. This should be present throughout the notebook consistently, wtih not just headers, but plenty of content that guides the reader and leaves no questions or doubt as to why you did something, e.g.
Written Conclusion Summary (Report.ipynb)
Your conclusion summary should addresses the questions you raised in the opening of the project, which we would want to see at the end of every final notebook. Ideally, when the deliverable is a report, the summary should tie together your analysis, the drivers of the outcome, and how you would expect your ML model to perform in the future on unseen data, in layman's terms.
conclusion recommendations (Report.ipynb)
Your notebook should ends with a conclusion that contains actionable recommendations based on your insights and analysis to the business stakeholder(s), your simulated audience, or someone who would find this information valuable (if there is no stakeholder). Your recommendations should not be not about what to do differently with the data, but instead should be based on the business or domain you are studying.
conclusion next steps (Report.ipynb)
Your conclusion should include next steps from a data science perspective that will assist in improving your research. Ideally, if you talk about trying more algorithms to improve performance, think about why you need to improve performance. And if the business calls for it, remember the best way to improve performance is to have better predictors/features. If you talk about gathering more data, being specific about what data you think will help you understand the problem better and why is the way to go!
no errors (Report.ipynb)
Your final notebook should run without error. One error in a notebook can lead to the rest of it erroring out. If you have a reader who doesn't know python, they will then not be able to consume your report.
Live Presentation
