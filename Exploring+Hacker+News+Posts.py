#!/usr/bin/env python
# coding: utf-8

# # Exploring Hacker News Posts
# 
# *Hacker News* is a site started by the startup incubator **[Y Combinator](https://news.ycombinator.com/)**, where user-submitted stories (known as "posts") are voted and commented upon and it is extremely popular in technology and startup circles.
# 
# In this project, we will analyze the posts made by users at the website about questions asked (`Ask HN`), responses on the thread (in terms of comments) and details about projects, products (`Show HN`) or just general interesting topics. We will also compare below two types of posts in the dataset:
# - Do `Ask HN` or `Show HN` receive more comments on average?
# - Do posts created at a certain time receive more comments on average?
# 
# The dataset is extracted from [here](https://www.kaggle.com/hacker-news/hacker-news-posts) and contains *20,000* rows and for reference check the row below from the dataset:
# 
# | id | title | url | num_points | num_comments | author | created_at |
# | -- | -- | -- | -- | -- | -- | -- |
# | 12224879 | Interactive Dynamic Video | http://www.interactivedynamicvideo.com/ | 386 | 52 | ne0phyte | 8/4/2016 11:52 |

# In[1]:


# import libraries
from csv import reader

# reading dataset into list of lists:
opened_file = open('hacker_news.csv')
read_file = reader(opened_file)
hn = list(read_file)
headers = hn[0]
hn = hn[1:]

# displaying header and first five rows
print(headers)
print('\n')
print(hn[:5])


# In[2]:


# creating empty lists
ask_posts = []
show_posts = []
other_posts = []

# iterating through each row to append the
# empty lists fulfilling criteria
for row in hn:
    title = row[1]
    title_lower = title.lower()
    if (title_lower.startswith('ask hn')):
        ask_posts.append(row)
    elif (title_lower.startswith('show hn')):
        show_posts.append(row)
    else:
        other_posts.append(row)

# printing lengths of all posts
print('Length of Ask Posts:', len(ask_posts))
print('Length of Show Posts:', len(show_posts))
print('Length of Other Posts:', len(other_posts))


# In[3]:


# examining first five rows of `ask_posts` & `show_posts`
print(ask_posts[:5])
print('\n')
print(headers)
print('\n')
print(show_posts[:5])


# In[4]:


# calculating total number comments in 'ask_posts'
total_ask_comments = 0
for row in ask_posts:
    number_comments = row[4]
    ask_int = int(number_comments)
    total_ask_comments += ask_int

print('Total Number of ask_comments:', total_ask_comments)


# In[5]:


# calculating avg. number of 'ask comments'
avg_ask_comments = total_ask_comments / len(ask_posts)
avg_ask_comments


# In[6]:


# calculating total number of comments in 'show_posts'
total_show_comments = 0
for row in show_posts:
    number_comments = row[4]
    show_int = int(number_comments)
    total_show_comments += show_int

print('Total Number of show_comments:', total_show_comments)


# In[7]:


# calculating avg. number of 'show_comments'
avg_show_comments = total_show_comments / len(show_posts)
avg_show_comments


# Above results show that on average comments on `ask_posts` are more than `show_posts` and this depicts that users are more engaging in these posts

# In[27]:


# calculating the amount of ask_posts created in each hours of day
# along with number of comments received

import datetime as dt

result_list = []
for row in ask_posts:
    created_at = row[6]
    numb_comments = int(row[4])
    result_list.append([created_at, numb_comments])


# In[29]:


# checking first 5 elements of `result_list`
result_list[:5]


# In[30]:


# creating empty dictionaries
counts_by_hour = {}
comments_by_hour = {}
date_format = "%m/%d/%Y %H:%M"
for row in result_list:
    hour_from_date = row[0]
    comment_num = row[1]
    datetime_object = dt.datetime.strptime(hour_from_date, date_format)
    hour = datetime_object.strftime("%H")
    if hour not in counts_by_hour:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = comment_num
    else:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += comment_num


# In[31]:


comments_by_hour


# In[32]:


counts_by_hour


# In[104]:


# calculating avg. number of comments per post during each hour of the day

avg_by_hour = []
for hr in comments_by_hour:
    avg_by_hour.append([hr, comments_by_hour[hr] / counts_by_hour[hr]])
    
avg_by_hour


# In[105]:


# swapping the elements of `avg_by_hour` list of lists
# for sorting the avg no. of comments per post

swap_avg_by_hour = []
for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])

print(swap_avg_by_hour)


# In[106]:


# sorting the swap_avg_by_hour in descending order
# to get the highest value in list

sorted_swap = sorted(swap_avg_by_hour, reverse=True)

print(sorted_swap)


# In[107]:


# printing the string
print('Top 5 Hours for `Ask HN` Comments')

# iterating through `sorted_swap` to print text using str.format()
for avg, hr in sorted_swap[:5]:
    dt_object = dt.datetime.strptime(hr, '%H')
    format_hour = dt_object.strftime('%H:%M')
    print('{}: {:.2f} average comments per post'.format(format_hour, avg))


# The hour that receives the most comments per post on average is 15:00, with an average of 38.59 comments per post. There's about a 60% increase in the number of comments between the hours with the highest and second highest average number of comments.

# ### Conclusion
# In this project, we analyzed `ask posts` and `show posts` to determine which type of post and time receive the most comments on average. Based on our analysis, to maximize the amount of comments a post receives, we'd recommend the post be categorized as `ask post` and created between 07:00 and 09:00.
# 
# However, it should be noted that the data set we analyzed excluded posts without any comments. Given that, it's more accurate to say that of the posts that received comments, `ask posts` received more comments on average and `ask posts` created between 07:00 and 09:00 received the most comments on average.
