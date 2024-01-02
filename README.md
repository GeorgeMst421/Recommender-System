# Recommender System Project

Author: Moustos Georgios  
AM: 7110132200214  
MSC: Control & Computing (Interdepartmental Program)  
Course: Big Data Management  
Professor: A. Ntoulas

# Info

The following project is a simple implementation of a recommender system made for the course Big Data Management (Μ111).    
The algorithms that were implemented are User-User, Item-Item, Tag-Based, Hybrid.   
This implementation works with both the ml-100k and ml-latest datasets but with different run commands  

### <b>Dataset ml-100k must include the following files:</b>  
u.data  
u.genre  
u.info  
u.user  
u.occupation  
u.item

### <b>Dataset ml-latest must include the following files:</b>  
genome-scores.csv  
genome-tags.csv  
links.csv  
movies.csv  
ratings.csv  
tags.csv

# How to Run

Open the terminal, navigate to the 'final_project' directory and run:

pip install .

## How to Run with the ml-latest dataset

<b>First command</b>:  

preprocess -d 'path-to-ml-latest-dataset'    

<b>Second Command:</b>  
  
  recommender -i -a -s -n 

<b>passing arguments: </b>    
-s : similarity ['jaccard', 'dice', 'cosine', 'pearson']  
-a : algorithm ['user', 'item', 'tag', 'hybrid', 'title']  
-n : number of final recommendations  
-i : input id

## How to Run with the ml-100 dataset

<b>First Command</b>:  

preprocess_100 -d 'path-to-ml-100-dataset'    

<b>Second Command:</b>  
  
recommender_100 -i -a -s -n 

<b>passing arguments: </b>    
-s : similarity ['jaccard', 'dice', 'cosine', 'pearson']  
-a : algorithm ['user', 'item', 'title, 'hybrid']  
-n : number of final recommendations  
-i : input id

 *Note: ml-100 dataset does not have tags so the algorithms that work with this dataset is the user-user and item-item*

# Running times in the Large Dataset
<b>*The following times have been calculated/processed with a laptop i7-12700 cpu. Times may vary depending on the cpu as well as the input id* </b>  
Preprocess time &emsp;&emsp;&emsp;&emsp;: ~15 mins  
User-User Algorithm &emsp;&emsp;:  all similarities 15~25 mins  
Item-Item Algorithm &emsp;&emsp;:  jaccard/dice/cosine ~30 mins , pearson 35~160mins  
Hybrid Algorithm &emsp;&emsp;&emsp; : User-Time + Item-Time   
Tag-Based Algorithm &emsp;&emsp;: &lt;1 min  
Content-Based Algorithm : &lt;1 min

