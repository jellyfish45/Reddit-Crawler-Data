# Reddit-Crawler-Data
In this repository, we are going to store Jupyter notebook regarding the crawling process and the dataset we get to help with future analysis.  
## Creation Timeline 
(1)scrape_reddit.ipynb: Scraping data with a theme of "suicide" from reddit. And find relevant topics about it.

(2)sub_gather.ipynb: Dig deep into the topics and gather the data.   

(3)posts_influence.ipynb: Try to track the influence of the most influencial submissions to their comment authors (Problem: need to scape more data and use more specific emotion analyzing tool)   

(4)sub_analyze.ipynb: Find keywords/valuable Issues related with the topics seperately. （Problem: need to dig deep) 

(5)posts-influence.ipynb: Try to analyze the posts'influence using "empath-client"

(6)Control_Group.ipynb: Find the control group (of the initial submission 3) and analyze them.

Other ipynb files are just auxiliary tools.
All the csv documents are the data I collected.


Dataset Expansion
    data_collection.ipynb: Code for collecting data to be used in analysis
    feature_creation_corrected.ipynb: Code for selecting a matched control group from a treatment group
    dataset_assumptions.txt: any assumptions in our dataset

    ***If you want to scrape data from a set of usernames, go to data_collection.ipynb, look at the first cell and run based on that 

GroupComparison
    notes.txt: old notes, will prob delete soon
    user_comparison_std_mean_diff.ipynb: Do standardize mean difference + standardized mean difference w/ PCA given control, treatment, date of interest, analyze propensity scores 
        Note: to run this replace the control and treatment lists with your control/treatment lists 

    user_group_comaprison.ipynb: same as above but assume same distribution, are they different? Not in use rn
        This is the old one I used - I think we moved away from this approach but I like it bc it is robust in a different way so not deleting it yet


DatasetPrediction/Shap
    I have a double ML model - this might be overkill bc we're matching, but looking into SHAP values and double ML as means of regression - not yet finished

Logan_Questions
    Logan's Notes on meetings


Logan TODOS
- EXPORT CUSTOM REDDITOR CLASS TO FILE TO LOAD FROM
- DOUBLE ML/SHAP
- More control group data gathering