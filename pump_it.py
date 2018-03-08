

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import Counter
%matplotlib inline

data_path = '/Users/hernando/Assignment2/'
train_values = pd.read_csv(data_path + 'Training_set_values.csv')
train_labels = pd.read_csv(data_path + 'Training_set_labels.csv')
test = pd.read_csv(data_path + 'Test_set_values.csv')


# Merge the two datasets for training
train = pd.merge(train_values, train_labels)
train.head()


# Counts for each level of status_group
Counter(train['status_group'])



train.groupby('status_group').count()

len(train.columns)




train[train['funder'].isnull()]

with plt.style.context('seaborn'):
    fig, ax = plt.subplots(figsize = (5,7))
    ax.plot(train.loc[train['funder'].isnull(), 'id'], train.loc[train['funder'].isnull(), 'status_group'])
    
    

plt.hist(train.loc[train['funder'].isnull(), 'id'], train.loc[train['funder'].isnull(), 'status_group'].)

plot(pd.DataFrame(train.loc[train['id'].isnull(), ['funder','status_group']]))






