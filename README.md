# Data-Mining-and-Bioinformatics
CSE601: Data Mining and Bioinformatics :  Implementation of Apriori algorithm and Association rule generation algorithm for Frequent Itemsets and Association rule mining of gene expression data.

Associative Analysis instructions
=====================================

- Execute the main.py file using the command "python main.py"
- You will be asked whether you want to input the Queries through file or console. If through file, type "file" and press enter (Code will read queries from 'rules.txt' file) and,
If through console, type "console" and press enter. Now enter you Query and press enter to see the result



- Modify text_file variable in main function of file main.py to change the file from where to read Queries (if you selected "file" above,currently its "rules.txt")
- set debugging_on variable in main function of file main.py to False if you want only rule count, else to True if you want rule counts and also print all the rules
-Modify text_file global variable in Project1_Apriori_PartA.py to specify the input file from where to read input data(currently its set to 'associationruletestdata.txt').
-Modify confidence_threshold and support_Threshold which are global variables in Project1_Apriori_PartA.py to modify Confidence and minsupport respectively
