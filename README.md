# PSEUDOCODE FOR HOMEWORK9

This program finds the best clustering for IRIS dataset extracted from sklearn by running KMeans clustering algorithm 
multiple times.

Load iris dataset and assign it to a variable    
Set the variable iternim to 10000    
Make an empty list a     
Make an empty list trainselect   
for i= 0 to iternim   
&nbsp;&nbsp;&nbsp;&nbsp;split the dataset into traning and test with respect to a given test size    
&nbsp;&nbsp;&nbsp;&nbsp;call clustering model with specified cluster number     
&nbsp;&nbsp;&nbsp;&nbsp;fit the model using training data   
&nbsp;&nbsp;&nbsp;&nbsp;calculate score using test data   
&nbsp;&nbsp;&nbsp;&nbsp;if score >= 0.80 then      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;store the training data   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print stored training data   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print score   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print 'Threshold is satisfied!'    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;terminate the loop   
&nbsp;&nbsp;&nbsp;&nbsp;append score to list   
&nbsp;&nbsp;&nbsp;&nbsp;if i equals to iternim-1 then   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print '10000 iteration is passed and threshold is not satisfied. This is the best result!'     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print maximum of list a   
end
