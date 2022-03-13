# Health Insurance - Cross Sell

<p align="center">
  <img src="img/Insurance.jpg" />
</p>

# 1. CONTEXT

The Insurance ALL is a company which provides health insurance to its customers and the product team is evaluating the possibility of offering a new product to them: vehicle insurance. As well as the health insurance, the customers should pay annually (annual premium) for this new insurance to obtain its benefits. 

Nearly 380K customers were surveyed about their interest to obtain this new product and their responses were stored together with their other information. The product team selected 127K new customers, who had not responded to the survey, to make the offer about the vehicle insurance. 

The offer will be made by phone call, but the sales team can only make 20K calls within the campaign period. Therefore, they need to make this limited number of calls to the customers who have a higher probability to obtain the insurance.

## 1.1 BUSINESS PROBLEM

* **Motivation**
  * The Insurance All product team is evaluating the possibility of offering a new product to their customers: vehicle insurance. 

* **The problem's root cause** 
  * The sales team can only make 20K calls within the campaign period to offer their customers this new insurance, but there are 127K customers. Therefore, they need to make this limited number of calls to the customers who have a higher probability to obtain the insurance.

* **The Stakeholder**
  * The CPO.

* **The solution format**
  * Developing a model which can predict the probability of a customer be interest in the vehicle insurance, so the sales team can prioritize making the calls to this customers.
  * **Questions to be answered:**
    * What are the key insights about the more relevant customer's attributes from the customers interested in obtaining vehicle insurance? 
    * What customer percentage interested in the vehicle insurance will the sales team reach out by making 20K calls?    
    * If the sales team makes 40k calls, what is the new percentage?
    * How many calls will the sales team have to make to reach 80% of the interested customers?
  * **Delivery method:** 
    * A Google Spreadsheet where the sales team can add customers to predict their probability of obtaining the insurance. There will be a button, which calls an API and fills a column with a score that represents the probability for each customer (higher score = higher probability).

# 2. DATA

The datasets are in CSV format and can be found at the following kaggle link: https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction.

## 2.1. FILES

The files used for the project are as follows:

* **train.csv** - data about the customers who responded to the survey.
* **test.csv** - data about the new customers who will be offered vehicle insurance.

## 2.2. DATA FIELDS

* **Id:**	Unique ID for the customer
* **Gender:**	Gender of the customer
* **Age:**	Age of the customer
* **Driving_License:**	0 -> Customer does not have DL / 1 -> Customer already has DL
* **Region_Code:**	Unique code for the region of the customer
* **Previously_Insured:**	0 -> Customer doesn't have vehicle insurance / 1 -> Customer already has vehicle insurance
* **Vehicle_Age:**	Age of the vehicle
* **Vehicle_Damage:**	0 -> Customer didn't get his/her vehicle damaged in the past / 1 -> Customer got his/her vehicle damaged in the past
* **Annual_Premium:**	The amount customer needs to pay as premium in the year
* **PolicySalesChannel:**	Anonymized code for the channel of outreaching to the customer ie. Different agents, over mail, over phone, in person, etc.
* **Vintage:**	Number of days that the customer has been associated with the company
* **Response:**	0 -> Customer is not interested in the vehicle insurance / 1 -> Customer is interested in the vehicle insurance

# 3. PROJECT MANAGEMENT METHOD

The management method used for this project was the CRISP-DM, which is a cyclic developing method focused on delivering a solution as soon as possible and then improving it in the next cycles. 

The steps performed are as follows: 

1. **Business problem understanding**
    * Defining the motivation, problem's root cause, who is the stakeholder and the solution format.

2. **Data Description**
    * Checking dimensions, data types and NA values to apply descriptive statistics methods to better understand the data fields and their characteristics.

3. **Feature Engineering**
    * Creating new features and raising hypotheses to understand the phenomenon that is being modeled and it's agents.

4. **Data Filtering**
    * Filtering rows and columns that are not relevant to solve the problem. 

5. **Exploratory Data Analysis (EDA)**
    * Validating the business hypothesis;
    * Understanding what might be the most important features to the model.

6. **Data Preparation**
    * Preparing the data to be used for the machine learning model.
      * Applying transformations such as Standardization, Scaling and Encoding. 

7. **Feature Selection**
    * Selecting the most significant features to train the model.

8. **Machine Learning Modeling**
    * Testing different machine learning models to compare performance and choose one of them to solve the problem. 
      *KNN, Logistic Regression and Extra Trees Classifier were tested.

9. **Model Performance**
    * Choosing the best model and getting its performance metrics.

10. **Deploy Model to Production**
    * Deploying the model to a cloud service and creating a google spreadsheet where the product/sales team gets the predictions.

# 4. RESULTS


# 5. DEPLOY
