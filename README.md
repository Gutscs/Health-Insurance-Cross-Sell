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
  * Developing a model wich can predict the probability of a customer be interest in the vehicle insurance, so the sales team can prioritize making the calls to this customers.
  * **Questions to be answared:**
    * What are the key insights about the more relevant customer's attributes from the customers interested in obtaining vehicle insurance? 
    * What customer percentage interested in the vehicle insurance will the sales team reach out by making 20K calls?    
    * If the sales team makes 40k calls, what is the new percentage?
    * How many calls will the sales team have to make to reach 80% of the interested customers?
  * **Delivery method:** 
    * A Google Spreadsheet where the sales team can add customers to predict their probability of obtaining the insurance. There will be a button, which calls an API and fills a column with a score that represents the probability for each customer (higher score = higher probability).
