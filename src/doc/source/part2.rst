Part 2: Scalability
====================

The model used in this package is Random Forest and the answer to this part will also be based on this algorithm. 

Challenges
##########

One of the parts in which even the development of this package came to a bottleneck, was hyperparameter tuning. A lot of experiments are usually performed to achieve the optimal hyperparameters.  The hyperparameters space could be large and one may not be able to use every combination, therefore the package has used random search in hyperparameter tuning. One should make sure of the target accuracy when making decisions about the trade-off of costs. Another useful method would be to definitely track versions and hyperparameters of the model and store them in the database for avoiding redundant computations. 
In addition, when it comes to random forests, one can achieve a higher accuracy and less overfitting by increasing the number of trees, however, this modification can result in a long processing time due to complexity.
In terms of algorithm complexity, two measures of time complexity and space complexity should be taken into account. 
 

Complexity
##########
To write computation complexity we are assuming:
* n= number of training examples
* d= number of dimensions of the data
* k= number of decision trees

The complexity therefore becomes:  

* Training Time Complexity = O(n*log(n)*d*k)
* Inference Complexity = O(depth of tree* k)
* Space Complexity = O(depth of tree * k)

Which although is more complex than decision trees, performs faster than many other machine learning models and makes the Random Forest a goos choice. 

Suggested Solutions
###################

**Python vs. C/C++**:   The package utilized in this model was ensemble learning from sklearn. Sklearn is mainly written in Python except for some core algorithms written with Cython. In sklearn Numpy is used for dealing with high-performance linear algebra calculation. If the core code can be written in C/C++, it might result in a better performance. 
 

**Choice of Processing Unit**:  For hardware choice, the developed models that CPUs are not ideal for large-scale machine learning and can quickly become a bottleneck. For parallelized computations, GPUs that are vector processors can be used. However, GPUs have a lot of power consumption and could be expensive.  

**Data Formats**: In choosing the data format, particularly in distributed systems, the HDF5 format can be effective. This format can also contain metadata which makes it easier for the data scientist to work with. They can easily have different aggregation levels which seem desirable for particularly this case with two levels of hour and day. 

**Parallellizing**: When it comes to the model selection, the models with inherent parallelizing ability help a lot. Notably, In training the random forest model, the divide and conquer can easily be utilized. One can easily decompose the computations in this algorithm, run them independently and aggregate them later. To this end, both functional decomposition and data decomposition can be performed. In a functional approach, the different parts of the models, that are trees in this case, can be splitted and executed parallely in different devices.  For the data decomposition approach, data is divided into chunks, and multiple machines can perform the exact computation on different data, which is again aligned with how random forest works which is an ensemble manner.  

**Apache Spark**: Another helpful framework that can be used for computation is  the Apache Spark. It has a lot of flexibility and can Join between different data structures. Spark can process large volumes of data and split them across different clusters using Resilient Distributed Dataset (RDD), driver node, and several worker nodes. In the scaling task, one can easily add nodes to the cluster, and avoid buying new hardwares, by easily buying new nodes. Spark can be utilized starting from Gigabytes to Terabytes of data and also for streaming data. 

For Spark, Random Forest is a perfect suit. In Random Forests, since each tree is trained independently, multiple trees can be trained in parallel along with the parallelization in single trees. Therefore, a distributed version of the algorithm can be created. To this end, Spark’s MLlib package can be used. Based on MLib documentation a variable number of sub-trees are trained in parallel, where the number is optimized on each iteration per memory constraints. 
Therefore,  Random Forest is parallelized by generating different models on different nodes, splitting the number of needed trees, and finally taking the mean of each one.
 



**Resource Utilization**:  Serverless architecture like lambda AWS can be utilized to minimize resource utilization since it can be paid per execution. To avoid the costs while using the cloud, one can first run a minimal version of the model on an owned resource and then run the original version on the cloud. Using the lambda function as a service in AWS could save money and provide flexibility for the team. 


My Experience
#############

I have been writing lambda function in the past year as a responsibility in my data science job. Although I have not worked with Spark in my data science job, since we were mostly working with relational databesed such as PostreSQL, I have been learning in Spark for personal development and I’m familiar with Mlib package and I believe I can easily apply it to work purposes. 

