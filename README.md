# Data-Visualization
A generic model to visualize different datasets with ease 

## 1-D Visualization
### Overall Stats of the Dataset

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/overall_stats.PNG)


### Histogram - all attributes

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Hitogram_1D.png)


### Histogram Plot for a single(numeric) attribute

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Single_Att_Histogram_1D.png)


### Histogram Plot for a single(categorical) attribute

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Signle_Categorical_Histogram_1D.png)


## 2-D Visualization

### Correlation Matrix - Heat Map
*Key:* 

*dataf - the dataframe that holds the entire dataset*

- Plotting Correlation between different attributes
- Correlation Matrix Heatmap  - check out potential relationships or correlations amongst the different data attributes by leveraging a pair-wise correlation matrix and depicting it as a heatmap
- The gradients in the heatmap vary based on the strength of the correlation

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Correlation_Matrix_HeatMap.png)


### Pair-Wise Scatter Plot
*Key:*

*dataf - the dataframe that holds the entire dataset*

*attribute_list - the list of attributes for which you want to plot pair-wise scatter plots*

- Visualizing two-dimensional data with pair-wise scatter plots
- Pair-wise Scatter Plots - Depicting correlation amongst different attributes of the data
- Observe patterns in two-dimensions for data attributes

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Pair_Wise_Scatter_Plot_2D.png)


### Parallel Coordinates
*Key:*

*dataf - the dataframe that holds the dataset*

*attribute_list - the list of attributes for which you want to plot parallel coordinates*

- Points are represented as connected line segments
- Each vertical line represents one data attribute
- One complete set of connected line segments across all the attributes represents one data point
- Points that tend to cluster will appear closer together

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Parallel_Coordinates.png)


### Scatter Joint Plot
*Key:*

*dataf - the dataframe that holds the dataset*

*attributes - the list of the two attributes for which you want to plot 'scatter plot' and 'joint plot'*

- Check for patterns, relationships between the two attributes
- See the individual distributions for the attributes

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Scatter_Joint__Plot_2D.png)

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Scatter_Joint__Plot2_2D.png)


### Categorical Bar Plot - 2 Categories
*Key:*

*dataf_class1 - dataframe with all attributes for class 1*

*dataf_class2 - dataframe with all attributes for class 2*

*attribute - attribute that we want to compare for both classes*

*class_1_label - title/label for class 1 bar plot*

*class_2_label - title/label for class 2 bar plot*

- Separate plots (subplots) or facets for one of the categorical dimensions
- Using subplots or facets along with Bar Plots

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Categorical_Bar_Plot_2D.png)


### Categorical Bar Plot - 3 Categories
*Key:*

*dataf_class1 - dataframe with all attributes for class 1*

*dataf_class2 - dataframe with all attributes for class 2*

*dataf_class3 - dataframe with all attributes for class 2*

*attribute - attribute that we want to compare for both classes*

*class_1_label - title/label for class 1 bar plot*

*class_2_label - title/label for class 2 bar plot*

*class_3_label - title/label for class 2 bar plot*


- Separate plots (subplots) or facets for one of the categorical attributes
- Using subplots or facets along with Bar Plots

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Categorical_Bar_Plot_3Classes_2D.png)


### Histogram and Density Plots for mixed(numeric+categorical) attributes - 2 classes
*Key:*

*dataf_class1 - dataframe with all attributes for class 1*

*dataf_class2 - dataframe with all attributes for class 2*

*attribute - attribute that we want to compare for both classes*

*class_1_label - title/label for class 1 bar plot*

*class_2_label - title/label for class 2 bar plot*

- Facets with histograms
- Visualizing mixed attributes in two-dimensions (essentially numeric and categorical together)
- Faceting\subplots along with generic histograms or density plots

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Mixed_Attributes_Hist_Plot_2D.png)

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Mixed_Attributes_Density_Plot_2D.png)


### Histogram and Density Plots for mixed(numeric+categorical) attributes - 3 classes
*Key:*

*dataf_class1 - dataframe with all attributes for class 1*

*dataf_class2 - dataframe with all attributes for class 2*

*dataf_class3 - dataframe with all attributes for class 3*

*attribute - attribute that we want to compare for both classes*

*class_1_label - title/label for class 1 bar plot*

*class_2_label - title/label for class 2 bar plot*

*class_3_label - title/label for class 3 bar plot*

- Facets with histograms
- Visualizing mixed attributes in two-dimensions (essentially numeric and categorical together)
- Faceting\subplots along with generic histograms or density plots

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Mixed_Attributes_Hist_Plot_3Classes_2D.png)

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Mixed_Attributes_Density_Plot_3Classes_2D.png)


### Box Plots
*Key:*

*dataf - the dataframe holding the entire dataset*

*attribute_x - the attribute to be plot across x_axis*

*attribute_y - the attribute on the y-axis*

- Box Plots - an effective representation of two-dimensional mixed attributes
- Effectively depicting groups of numeric data based on the different values in the categorical attribute
- A good way to know the quartile values in the data and also potential outliers

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Box_Plot_2D.png)


### Violin Plots
*Key:*

*dataf - the dataframe holding the entire dataset*

*attribute_x - the attribute to be plot across x_axis*

*attribute_y - the attribute on the y-axis*

- Violin Plots - an effective representation of two-dimensional mixed attributes
- Another effective way to visualize grouped numeric data using kernel density plots
- Depicts probability density of the data at different values


![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Violin_Plot_2D.png)



## 3-D Visualization

### Pair-Wise Scatter Plots
*Key:*

*dataf - dataframe that holds the entire dataset*

*attribute_list - the list of attributes for which you want to plot 'Scatter Plots' in comparison*

*category_column - the column name in the dataframe, that holds the class labels*

- Scatter Plot with Hue for visualizing data in 3-D
- Visualizing three-dimensional data with scatter plots and hue (color)
- Check out correlations and patterns and also compare around class groups

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Pair_Wise_Scatter_Plot_3D.png)


### Numeric Data Plot
*Key:*

*dataf - the dataframe that holds the entire dataset*

*attribute_x - the attribute on the x-axis*

*attribute_y - the attribute on the y-axis*

*attribute_z - the attribute on the z-axis*

- Visualizing 3-D numeric data with Scatter Plots
- length, breadth and depth

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Numeric_Data_3D.png)


### Bubble Chart
*Key:*

*dataf - the dataframe holding the entire dataset*

*attribute_x - the attribute to be plot across x_axis*

*attribute_y - the attribute on the y-axis*

*attribute_s - the attribute represented as size  - The values in this atttribute must all be positive*

- Visualizing 3-D numeric data with a bubble chart
- length, breadth and size
- Leverage the regular 2-D axes & introduce the notion of size as the third dimension (essentially a bubble chart) where the size of the dots indicate the quantity of the third dimension.

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Bubble_Chart_3D.png)


### Scatter Plot for mixed(numeric_categorical) attributes
*Key:*

*dataf - the dataframe that holds the entire dataset*

*attribute_x - attribute on the x-axis*

*attribute_c - attribute separating bar plots - for each value of this categorical attribute a different bar plot will be plotted*

*attribute_cat - the categorical attribute - you can use the column name in dataframe holding the class labels - this will act as the third dimension*

*Note: mixed attributes - categorical plus numeric - 2 numberic and 1 categorical*

- Visualizing 3-D mix data using scatter plots
- leveraging the concepts of hue for categorical dimension
- Visualizing mixed attributes in three-dimensions leveraging scatter plots and the concept of hue
- Visualization for three mixed attributes, using the notion of hue for separating our groups in one of the categorical attributes while using conventional visualizations like scatter plots for visualizing two dimensions for numeric attributes


![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Scatter_Plot_3D_Mix_1.png)

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Scatter_Plot_3D_Mix_2.png)


### Kernel Density Plot
*Key:*

*dataf_class1 - dataframe with all attributes for class 1*

*dataf_class2 - dataframe with all attributes for class 2*

*attribute_x - the attribute to place on x-axis*

*attribute_y - the attribute to place on y-axis*

- Visualizing 3-D mix data using kernel density plots
- leveraging the concepts of hue for categorical dimension
- see the density concentrations based on the hue intensity

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Kernel_Density_Plot_3D.png)


## 4-D Visualization

### Scatter Plot for mixed(numeric+categorical) attributes
*Key:*

*dataf - the dataframe that hlds the dataset*

*attribute_x - the attribute to place on x-axis; numeric attribute*

*attribute_y - the attribute to place on y-axis; numeric attribute*

*attribute_z - the attribute to place on z-axis; numeric attribute*

*category_column - the column name in the dataframe, that holds the class labels*

- Visualizing 4-D mix data using scatter plots
- Leveraging the concepts of hue and depth
- Three numberic attributes and one categorical attribute

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Scatter_Plot_4D_Mix.png)


### Bubble Chart 
*Key:*

*dataf - the dataframe that hlds the dataset*

*attribute_x - the attribute to place on x-axis; numeric attribute*

*attribute_y - the attribute to place on y-axis; numeric attribute*

*attribute_z - the attribute to represent as size; numeric attribute*

*category_column - the column name in the dataframe, that holds the class labels*

*Note : depending on the min and max value of attribute z, you can alter the value of 'scale' in the code to adjust the min and max size presented on graph*

- Visualizing 4-D mix data using bubble plots
- Leveraging the concepts of hue and size
- Visualizing data in four-dimensions leveraging bubble charts and the concept of hue and size
- Using size to represent one of the numeric attributes
- Using hue to represent the categorical attribute

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Bubble_Plot_4D_Mix.png)


## 5-D Visualization

### Bubble Chart
*Key:*

*dataf - the dataframe that hlds the dataset*

*attribute_x - the attribute to place on x-axis; numeric attribute*

*attribute_y - the attribute to place on y-axis; numeric attribute*

*attribute_z - the attribute to place on z-axis; numeric attribute*

*attribute_s - the attribute to represent as size; numeric attribute*

*category_column - the column name in the dataframe, that holds the class labels*

- Visualizing 5-D mix data using bubble charts
- leveraging the concepts of hue, size and depth

![alt text](https://github.com/Aqsa-K/Data-Visualization/blob/master/Iris_Figures/Bubble_Chart_5D_Mix.png)

