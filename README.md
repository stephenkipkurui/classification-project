
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
