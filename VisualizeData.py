import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns


# -------------------------------------VISUALIZING DATA IN ONE DIMENSIONS-------------------------------------#

def SubsetAttributes(dataf, attributes):
    # Key:
    #       dataf - the dataframe that holds the dataset
    #       attributes - the attributes/features for which you want to print stats

    # Plot:
    #       Print count, mean, std, min, quartiles, max for the attributes defined
    #       Display the table

    ws = round(dataf[attributes].describe(), 2)
    print(ws)


def Plot_Histograms(dataf):
    # Key:
    #       dataf - the dataframe that holds the dataset

    # Plot:
    #       Plot histograms for all attributes in the combined dataset

    dataf.hist(bins=15, color='steelblue', edgecolor='black', linewidth=1.0,
               xlabelsize=8, ylabelsize=8, grid=False)

    plt.tight_layout(rect=(0, 0, 1.0, 1.0))
    plt.show()


def Plot_Single_Attribute_Hist_Density_Plot(dataf, attribute):
    # Key:
    #       dataf - the dataframe that holds the dataset
    #       attribute - the 'numeric' attribute for which you want to plot the histogram and density plot

    # Plot:
    #       Plot histogram and density plot for a single attribute
    #       For numeric attribute

    # Histogram
    fig = plt.figure(figsize=(6, 4))
    title = fig.suptitle(attribute + " Content", fontsize=14)
    fig.subplots_adjust(top=0.85, wspace=0.3)

    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel(attribute)
    ax.set_ylabel("Frequency")
    ax.text(1.2, 800, r'$\mu$=' + str(round(dataf[attribute].mean(), 2)),
            fontsize=12)
    freq, bins, patches = ax.hist(dataf[attribute], color='steelblue', bins=15,
                                  edgecolor='black', linewidth=1)
    plt.show()

    # Density Plot
    fig = plt.figure(figsize=(6, 4))
    title = fig.suptitle(attribute + " Content", fontsize=14)
    fig.subplots_adjust(top=0.85, wspace=0.3)

    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_xlabel(attribute)
    ax1.set_ylabel("Frequency")
    sns.kdeplot(dataf[attribute], ax=ax1, shade=True, color='steelblue')


def Plot_Single_Categorical_Attribute(dataf, attribute):
    # Key:
    #       dataf - the dataframe that holds the dataset
    #       attribute - the 'categorical' attribute for which you want to plot the histogram and density plot

    # Plot:
    #       Plot histogram and density plot for a single attribute
    #       For categorical attribute
    #       Visualize Categorical Data - Visualizing a discrete, categorical data attribute is slightly different and bar plots are good for this

    # Bar Plot   - Plotting Single Attribute Frequency
    fig = plt.figure(figsize=(6, 4))
    title = fig.suptitle(attribute + " Frequency", fontsize=14)
    fig.subplots_adjust(top=0.85, wspace=0.3)

    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel(attribute)
    ax.set_ylabel("Frequency")
    w_q = dataf[attribute].value_counts()
    w_q = (list(w_q.index), list(w_q.values))
    ax.tick_params(axis='both', which='major', labelsize=8.5)
    bar = ax.bar(w_q[0], w_q[1], color='steelblue',
                 edgecolor='black', linewidth=1)
    plt.show()


# -------------------------------------VISUALIZING DATA IN TWO DIMENSIONS-------------------------------------#



def Correlation_Matrix_HeatMap(dataf): 
    # Key:
    #       dataf - the dataframe that holds the dataset

    # Plot:    
    #       Plotting Correlation between different attributes
    #       Correlation Matrix Heatmap  - check out potential relationships or correlations amongst the different data attributes by leveraging a pair-wise correlation matrix and depicting it as a heatmap.
    #       The gradients in the heatmap vary based on the strength of the correlation
    
    f, ax = plt.subplots(figsize=(10, 8))
    corr = dataf.corr()
    hm = sns.heatmap(round(corr, 2), annot=True, ax=ax, cmap="coolwarm", fmt='.2f',
                     linewidths=.05)
    f.subplots_adjust(top=0.95)
    t = f.suptitle('Attribute Correlation Heatmap', fontsize=14)
    plt.show()


def Pair_Wise_Scatter_Plot(dataf, attribute_list):  
    # Key:
    #       dataf - the dataframe that holds the dataset
    #       attribute_list - the attributes/features for which you want to plot pair wise scatter plots

    # Plot:
    #       Visualizing two-dimensional data with pair-wise scatter plots
    #       Pair-wise Scatter Plots - Depicting correlation amongst different attributes of the data
    #       Observe patterns in two-dimensions for data attributes
    
    pp = sns.pairplot(dataf[attribute_list], size=1.8, aspect=1.8,
                      plot_kws=dict(edgecolor="k", linewidth=0.5),
                      diag_kind="kde", diag_kws=dict(shade=True))

    fig = pp.fig
    fig.subplots_adjust(top=0.93, wspace=0.3)
    t = fig.suptitle('Wine Attributes Pairwise Plots', fontsize=14)
    plt.show()


def Parallel_Coordinates(dataf, attribute_list, category_types):
    # Key:
    #       dataf - dataframe that holds the entire dataset
    #       attribute_list - the list of attributes for which you want to plot parallel coordinates
    #       category_types - the name of the column in the dataframe that holds the class labels or category types

    # Plot:
    #       Points are represented as connected line segments
    #       Each vertical line represents one data attribute
    #       One complete set of connected line segments across all the attributes represents one data point
    #       Points that tend to cluster will appear closer together

    # Scaling attribute values to avoid few outiers
    subset_df = dataf[attribute_list]

    from sklearn.preprocessing import StandardScaler            # To standardize the data - convert to mean 0, so that all attributes are on the same scale of range
    ss = StandardScaler()

    scaled_df = ss.fit_transform(subset_df)
    scaled_df = pd.DataFrame(scaled_df, columns=attribute_list)
    final_df = pd.concat([scaled_df, dataf[category_types]], axis=1)
    # final_df.head()

    # plot parallel coordinates
    from pandas.tools.plotting import parallel_coordinates
    parallel_coordinates(final_df, category_types)
    plt.show()


def Plot_Scatter_Joint(dataf, attributes):          
    # Key:
    #       dataf - dataframe that holds the entire dataset
    #       attributes - the list of the two attributes (numeric) for which you want to plot 'scatter plot' and 'joint plot'

    # Plot:
    #       visualize two continuous, numeric attributes
    #       Check for patterns, relationships between the two attributes
    #       See the individual distributions for the attributes

    # Scatter Plot
    plt.scatter(dataf[attributes[0]], dataf[attributes[1]],
                alpha=0.4, edgecolors='w')

    plt.xlabel(attributes[0])
    plt.ylabel(attributes[1])
    plt.title(attributes[0] + ' - ' + attributes[1], y=1.05)
    plt.show()

    # Joint Plot
    sns.jointplot(x=attributes[0], y=attributes[1], data=dataf,
                  kind='reg', space=0, size=5, ratio=4)
    plt.show()


def TwoD_Categorical_Bar_Plots(dataf_class1, dataf_class2, attribute, class_1_label, class_2_label):       
    # Key:
    #       dataf_class1 - dataframe with all attributes for class 1
    #       dataf_class2 - dataframe with all attributes for class 2
    #       attribute - attribute(categorical) that we want to compare for both classes
    #       class_1_label - title/label for class 1 bar plot
    #       class_2_label - title/label for class 2 bar plot

    # Plot:
    #       visualizing two discrete, categorical attributes
    #       Separate plots (subplots) or facets for one of the categorical dimensions
    #       Using subplots or facets along with Bar Plots

    fig = plt.figure(figsize=(10, 4))
    title = fig.suptitle('Category ' + class_1_label + ' and ' + class_2_label, fontsize=14)
    fig.subplots_adjust(top=0.85, wspace=0.3)

    # class 1 - attribute
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_title(class_1_label)
    ax1.set_xlabel(attribute)
    ax1.set_ylabel("Frequency")
    rw_q = dataf_class1[attribute].value_counts()
    rw_q = (list(rw_q.index), list(rw_q.values))
    # ax1.set_ylim([0, 2500])
    ax1.set_xlim([0, 4])
    ax1.tick_params(axis='both', which='major', labelsize=8.5)
    bar1 = ax1.bar(rw_q[0], rw_q[1], color='red',
                   edgecolor='black', linewidth=1)

    # class 2 - attribute
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_title(class_2_label)
    ax2.set_xlabel(attribute)
    ax2.set_ylabel("Frequency")
    ww_q = dataf_class2[attribute].value_counts()
    ww_q = (list(ww_q.index), list(ww_q.values))
    # ax2.set_ylim([0, 2500])
    ax2.set_xlim([0, 4])
    ax2.tick_params(axis='both', which='major', labelsize=8.5)
    bar2 = ax2.bar(ww_q[0], ww_q[1], color='white',
                   edgecolor='black', linewidth=1)

    plt.show()


def Categorical_Bar_Plots_3Class_2D(dataf_class1, dataf_class2, dataf_class3, attribute, class_1_label, class_2_label,
                                    class_3_label):       
    # Key:
    #       dataf_class1 - dataframe with all attributes for class 1
    #       dataf_class2 - dataframe with all attributes for class 2
    #       attribute - attribute (categorical) that we want to compare for both classes
    #       class_1_label - title/label for class 1 bar plot
    #       class_2_label - title/label for class 2 bar plot

    # Plot:
    #       visualizing two discrete, categorical attributes - one for each class
    #       Separate plots (subplots) or facets for one of the categorical dimensions
    #       Using subplots or facets along with Bar Plots

    fig = plt.figure(figsize=(16, 4))
    title = fig.suptitle('Category Frequency in Each Class', fontsize=14)
    fig.subplots_adjust(top=0.85, wspace=0.3)

    # class 1 - attribute
    ax1 = fig.add_subplot(1, 3, 1)
    ax1.set_title(class_1_label)
    ax1.set_xlabel(attribute)
    ax1.set_ylabel("Frequency")
    rw_q = dataf_class1[attribute].value_counts()
    rw_q = (list(rw_q.index), list(rw_q.values))
    ax1.set_ylim([0, 60])
    ax1.set_xlim([0, 4])
    ax1.tick_params(axis='both', which='major', labelsize=8.5)
    bar1 = ax1.bar(rw_q[0], rw_q[1], color='red',
                   edgecolor='black', linewidth=1)

    # class 2 - attribute
    ax2 = fig.add_subplot(1, 3, 2)
    ax2.set_title(class_2_label)
    ax2.set_xlabel(attribute)
    ax2.set_ylabel("Frequency")
    ww_q = dataf_class2[attribute].value_counts()
    ww_q = (list(ww_q.index), list(ww_q.values))
    ax2.set_ylim([0, 60])
    ax2.set_xlim([0, 4])
    ax2.tick_params(axis='both', which='major', labelsize=8.5)
    bar2 = ax2.bar(ww_q[0], ww_q[1], color='green',
                   edgecolor='black', linewidth=1)

    # class 3 - attribute
    ax3 = fig.add_subplot(1, 3, 3)
    ax3.set_title(class_3_label)
    ax3.set_xlabel(attribute)
    ax3.set_ylabel("Frequency")
    ww_q = dataf_class3[attribute].value_counts()
    ww_q = (list(ww_q.index), list(ww_q.values))
    ax3.set_ylim([0, 60])
    ax3.set_xlim([0, 4])
    ax3.tick_params(axis='both', which='major', labelsize=8.5)
    bar2 = ax3.bar(ww_q[0], ww_q[1], color='blue',
                   edgecolor='black', linewidth=1)

    plt.show()


def Categorical_Mulitple_Bar_Plot(dataf, attribute, category_column):     
    # Key:
    #       dataf - dataframe that holds the entire dataset
    #       attribute - the attribute (categorical) you want to compare for the classes
    #       category_column - the name of the column in the dataframe that holds the class labels or category types

    # Plot:
    #       visualizing two discrete, categorical attributes
    #       Multi-bar Plot
    #       Effectively compare the different categories easily from a single plot

    sns.countplot(x=attribute, hue=category_column, data=dataf)
    plt.show()


def Mixed_Attributes_Hist_Density_Plot(dataf_class1, dataf_class2, attribute, class_1_label, class_2_label):       
    # Key:
    #       dataf_class1 - dataframe with all attributes for class 1
    #       dataf_class2 - dataframe with all attributes for class 2
    #       attribute - attribute that we want to compare for both classes
    #       class_1_label - title/label for class 1 bar plot
    #       class_2_label - title/label for class 2 bar plot
    #       graph_title - title to display on graph plot

    # Plot:
    #       Facets with histograms
    #       Visualizing mixed attributes in two-dimensions (essentially numeric and categorical together)
    #       Faceting\subplots along with generic histograms or density plots

    fig = plt.figure(figsize=(10, 4))
    title = fig.suptitle(attribute + ' and Category', fontsize=14)
    fig.subplots_adjust(top=0.85, wspace=0.3)

    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_title(class_1_label)
    ax1.set_xlabel(attribute)
    ax1.set_ylabel("Frequency")
    # ax1.set_ylim([0, 1200])
    ax1.text(1.2, 800, r'$\mu$=' + str(round(dataf_class1[attribute].mean(), 2)),
             fontsize=12)
    r_freq, r_bins, r_patches = ax1.hist(dataf_class1[attribute], color='red', bins=15,
                                         edgecolor='black', linewidth=1)

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_title(class_2_label)
    ax2.set_xlabel(attribute)
    ax2.set_ylabel("Frequency")
    # ax2.set_ylim([0, 1200])
    ax2.text(0.8, 800, r'$\mu$=' + str(round(dataf_class2[attribute].mean(), 2)),
             fontsize=12)
    w_freq, w_bins, w_patches = ax2.hist(dataf_class2[attribute], color='white', bins=15,
                                         edgecolor='black', linewidth=1)

    # facets with density plots
    fig = plt.figure(figsize=(10, 4))
    title = fig.suptitle(attribute + ' and Category', fontsize=14)
    fig.subplots_adjust(top=0.85, wspace=0.3)

    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_title(class_1_label)
    ax1.set_xlabel(attribute)
    ax1.set_ylabel("Density")
    sns.kdeplot(dataf_class1[attribute], ax=ax1, shade=True, color='r')

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_title(class_2_label)
    ax2.set_xlabel(attribute)
    ax2.set_ylabel("Density")
    sns.kdeplot(dataf_class2[attribute], ax=ax2, shade=True, color='y')
    plt.show()


def Mixed_Attributes_Hist_Density_Plot_3_Classes(dataf_class1, dataf_class2, dataf_class3, attribute, class_1_label, class_2_label, class_3_label):
    # Key:
    #       dataf_class1 - dataframe with all attributes for class 1
    #       dataf_class2 - dataframe with all attributes for class 2
    #       attribute - attribute (numeric) that we want to compare for both classes
    #       class_1_label - title/label for class 1 bar plot
    #       class_2_label - title/label for class 2 bar plot
    #       graph_title - title to display on graph plot

    # Plot:
    #       Facets with histograms
    #       Visualizing mixed attributes in two-dimensions (essentially numeric and categorical together)
    #       Faceting\subplots along with generic histograms or density plots

    fig = plt.figure(figsize=(16, 4))
    title = fig.suptitle(attribute + ' and Category', fontsize=14)
    fig.subplots_adjust(top=0.85, wspace=0.3)

    ax1 = fig.add_subplot(1, 3, 1)
    ax1.set_title(class_1_label)
    ax1.set_xlabel(attribute)
    ax1.set_ylabel("Frequency")
    # ax1.set_ylim([0, 1200])
    ax1.text(1.2, 800, r'$\mu$=' + str(round(dataf_class1[attribute].mean(), 2)),
             fontsize=12)
    r_freq, r_bins, r_patches = ax1.hist(dataf_class1[attribute], color='red', bins=15,
                                         edgecolor='black', linewidth=1)

    ax2 = fig.add_subplot(1, 3, 2)
    ax2.set_title(class_2_label)
    ax2.set_xlabel(attribute)
    ax2.set_ylabel("Frequency")
    # ax2.set_ylim([0, 1200])
    ax2.text(0.8, 800, r'$\mu$=' + str(round(dataf_class2[attribute].mean(), 2)),
             fontsize=12)
    w_freq, w_bins, w_patches = ax2.hist(dataf_class2[attribute], color='white', bins=15,
                                         edgecolor='black', linewidth=1)

    ax3 = fig.add_subplot(1, 3, 3)
    ax3.set_title(class_3_label)
    ax3.set_xlabel(attribute)
    ax3.set_ylabel("Frequency")
    # ax2.set_ylim([0, 1200])
    ax3.text(0.8, 800, r'$\mu$=' + str(round(dataf_class3[attribute].mean(), 2)),
             fontsize=12)
    w_freq, w_bins, w_patches = ax3.hist(dataf_class2[attribute], color='blue', bins=15,
                                         edgecolor='black', linewidth=1)

    # facets with density plots
    fig = plt.figure(figsize=(10, 4))
    title = fig.suptitle(attribute + ' and Category', fontsize=14)
    fig.subplots_adjust(top=0.85, wspace=0.3)

    ax1 = fig.add_subplot(1, 3, 1)
    ax1.set_title(class_1_label)
    ax1.set_xlabel(attribute)
    ax1.set_ylabel("Density")
    sns.kdeplot(dataf_class1[attribute], ax=ax1, shade=True, color='r')

    ax2 = fig.add_subplot(1, 3, 2)
    ax2.set_title(class_2_label)
    ax2.set_xlabel(attribute)
    ax2.set_ylabel("Density")
    sns.kdeplot(dataf_class2[attribute], ax=ax2, shade=True, color='y')

    ax3 = fig.add_subplot(1, 3, 3)
    ax3.set_title(class_3_label)
    ax3.set_xlabel(attribute)
    ax3.set_ylabel("Density")
    sns.kdeplot(dataf_class3[attribute], ax=ax3, shade=True, color='b')

    plt.show()


def Multiple_Histogram(dataf, attribute, category_column):
    # Key:
    #       dataf - the dataframe that holds the entire dataset
    #       attribute - attribute(numeric) that we want to compare for both classes
    #       category_column - column name in dataframe holding class labels
    #       graph_title - title to give to the graph plot

    # Plot:
    #       Using multiple Histograms
    #       Compare across the distributions easily

    fig = plt.figure(figsize=(6, 4))
    title = fig.suptitle(attribute + " - " + category_column, fontsize=14)
    fig.subplots_adjust(top=0.85, wspace=0.3)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel(attribute)
    ax.set_ylabel("Frequency")

    g = sns.FacetGrid(dataf, hue=category_column)
    g.map(sns.distplot, attribute, kde=False, bins=15, ax=ax)
    ax.legend(title=category_column)

    plt.close(2)
    plt.show()


def Box_Plots(dataf, attribute_x, attribute_y):
    # Key:
    #       dataf - the dataframe holding the entire dataset
    #       attribute_x - the attribute to be plot across x_axis ; 'numeric' 
    #       attribute_y - the attribute on the y-axis ; 'categorical'

    # Plot:
    #       Box Plots - an effective representation of two-dimensional mixed attributes
    #       Effectively depicting groups of numeric data based on the different values in the categorical attribute
    #       A good way to know the quartile values in the data and also potential outliers

    f, (ax) = plt.subplots(1, 1, figsize=(12, 4))
    f.suptitle(attribute_x + " - " + attribute_y, fontsize=14)

    sns.boxplot(x=attribute_x, y=attribute_y, data=dataf, ax=ax)
    ax.set_xlabel(attribute_x, size=12, alpha=0.8)
    ax.set_ylabel(attribute_y, size=12, alpha=0.8)
    plt.show()


def Violin_Plots(dataf, attribute_x, attribute_y):
    # Key:
    #       dataf - the dataframe holding the entire dataset
    #       attribute_x - the attribute to be plot across x_axis ; 'numeric' 
    #       attribute_y - the attribute on the y-axis ; 'categorical'

    # Plot:
    #       Violin Plots - an effective representation of two-dimensional mixed attributes
    #       Another effective way to visualize grouped numeric data using kernel density plots
    #       (depicts probability density of the data at different values)


    f, (ax) = plt.subplots(1, 1, figsize=(12, 4))
    f.suptitle(attribute_x + " - " + attribute_y, fontsize=14)

    sns.violinplot(x=attribute_x, y=attribute_y, data=dataf, ax=ax)
    ax.set_xlabel(attribute_x, size=12, alpha=0.8)
    ax.set_ylabel(attribute_y, size=12, alpha=0.8)
    plt.show()


# -------------------------------------VISUALIZING DATA IN THREE DIMENSIONS-------------------------------------#




def Pair_Wise_Scatter_Plot_3D(dataf, attribute_list, category_column):
    # Key:
    #       dataf - dataframe that holds the entire dataset
    #       attribute_list - the list of attributes for which you want to plot 'Scatter Plots' in comparison
    #       category_column - the column name in the dataframe, that holds the class labels
    # Plot:
    #       Scatter Plot with Hue for visualizing data in 3-D
    #       Visualizing three-dimensional data with scatter plots and hue (color)
    #       Check out correlations and patterns and also compare around class groups

    pp = sns.pairplot(dataf[attribute_list], hue=category_column, size=1.8, aspect=1.8,
                      plot_kws=dict(edgecolor="black", linewidth=0.5))
    fig = pp.fig
    fig.subplots_adjust(top=0.93, wspace=0.3)
    t = fig.suptitle('Attributes Pair Wise Scatter Plot', fontsize=14)
    plt.show()


def Numeric_Data_3D(dataf, attribute_x, attribute_y, attribute_z):
    # Key:
    #       dataf - the dataframe that holds the entire dataset
    #       attribute_x - the attribute on the x-axis
    #       attribute_y - the attribute on the y-axis
    #       attribute_z - the attribute on the z-axis

    # Plot:
    #       Visualizing 3-D numeric data with Scatter Plots
    #       length, breadth and depth

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    xs = dataf[attribute_x]
    ys = dataf[attribute_y]
    zs = dataf[attribute_z]
    ax.scatter(xs, ys, zs, s=50, alpha=0.6, edgecolors='w')

    ax.set_xlabel(attribute_x)
    ax.set_ylabel(attribute_y)
    ax.set_zlabel(attribute_z)
    plt.show()


def Bubble_Chart_3D(dataf, attribute_x, attribute_y, attribute_s):         
    # Key:
    #       dataf - the dataframe holding the entire dataset
    #       attribute_x - the attribute to be plot across x_axis ; numeric
    #       attribute_y - the attribute on the y-axis ; numeric
    #       attribute_s - the attribute (numeric) represented as size  - The values in this atttribute must all be positive

    # Plot:
    #       Visualizing three-dimensional numeric data by introducing the notion of size
    #       Visualizing 3-D numeric data with a bubble chart
    #       length, breadth and size
    #       Leverage the regular 2-D axes & introduce the notion of size as the third dimension (essentially a bubble chart)
    #       where the size of the dots indicate the quantity of the third dimension.

    size_scale_factor = 25
    plt.scatter(dataf[attribute_x], dataf[attribute_y], s=dataf[attribute_s] * size_scale_factor,
                alpha=0.4, edgecolors='w')

    plt.xlabel(attribute_x)
    plt.ylabel(attribute_y)
    plt.title(attribute_x + " - " + attribute_y + " - " + attribute_s, y=1.05)
    plt.show()


def Bar_Plot_3D(dataf, attribute_x, attribute_c, category_column):              # categorical data - 3D plot
    # Key:
    #       dataf - the dataframe that holds the entire dataset
    #       attribute_x - attribute on the x-axis
    #       attribute_c - attribute separating bar plots - for each value of this categorical attribute a different bar plot will be plotted
    #       category_column - the column name in dataframe holding the class labels - this will act as our third dimension
    #       Note: all three attributes are categorical
    
    # Plot:
    #       Visualizing 3-D categorical data using bar plots
    #       Leveraging the concepts of hue and facets/subplots to support the additional third dimension
    #       Clearly shows the frequency pertaining to each of the dimensions
    #       Easy and effective in understanding relevant insights.

    fc = sns.factorplot(x=attribute_x, hue=category_column, col=attribute_c,
                        data=dataf, kind="count",
                        palette={"red": "#FF9999", "white": "#FFE888"})
    plt.show()


def Scatter_Plot_3D_Mix_Data(dataf, attribute_num_x, attribute_num_y, attribute_cat):
    # Key:
    #       dataf - the dataframe that holds the entire dataset
    #       attribute_x - attribute on the x-axis  ; numeric
    #       attribute_c - attribute separating bar plots - for each value of this categorical attribute a different bar plot will be plotted
    #       attribute_cat - the categorical attribute - you can use the column name in dataframe holding the class labels - this will act as the third dimension
    #       Note: mixed attributes - categorical plus numeric - 2 numberic and 1 categorical

    # Plot:
    #       Visualizing 3-D mix data using scatter plots
    #       leveraging the concepts of hue for categorical dimension
    #       Visualizing mixed attributes in three-dimensions leveraging scatter plots and the concept of hue
    #       Visualization for three mixed attributes, using the notion of hue for separating our groups in one of the categorical attributes
    #       while using conventional visualizations like scatter plots for visualizing two dimensions for numeric attributes


    jp = sns.pairplot(dataf, x_vars=[attribute_num_x], y_vars=[attribute_num_y], size=4.5,
                      hue=attribute_cat,
                      plot_kws=dict(edgecolor="k", linewidth=0.5))

    # we can also view relationships\correlations as needed
    lp = sns.lmplot(x=attribute_num_x, y=attribute_num_y, hue=attribute_cat,
                    data=dataf, fit_reg=True, legend=True,
                    scatter_kws=dict(edgecolor="k", linewidth=0.5))

    plt.show()


def Kernel_Density_Plot_3D(dataf_class1, dataf_class2, attribute_x, attribute_y):
    # Key:
    #       dataf_class1 - dataframe with all attributes for class 1
    #       dataf_class2 - dataframe with all attributes for class 2
    #       attribute_x - the attribute to place on x-axis ; numeric
    #       attribute_y - the attribute to place on y-axis ; numeric

    # Plot:
    #       Visualizing 3-D mix data using kernel density plots
    #       leveraging the concepts of hue for categorical dimension
    #       see the density concentrations based on the hue intensity

    ax1 = sns.kdeplot(dataf_class1[attribute_x], dataf_class1[attribute_y], legend=True, cbar=True,
                      cmap="YlOrBr", shade=True, shade_lowest=False)
    ax2 = sns.kdeplot(dataf_class2[attribute_x], dataf_class2[attribute_y], legend=True, cbar=True,
                      cmap="Reds", shade=True, shade_lowest=False)

    red_patch = mpatches.Patch(color='red', label='Class1')
    yellow_patch = mpatches.Patch(color='yellow', label='Class2')
    plt.legend(handles=[red_patch, yellow_patch])

    plt.show()


def Violin_Plot_3D_Mix(dataf, attribute_x, attribute_y, category_column):
    # Key:
    #       dataf - the dataframe that holds the entire dataset
    #       attribute_x - the attribute on the x-axis ; should be categorical
    #       attribute_y - the attribute on the y-axis ; numeric
    #       category_column - the column name in dataframe holding the class labels - this will act as our categorical third dimension

    # Plot:
    #       Visualizing 3-D mix data using violin plots
    #       leveraging the concepts of hue and axes for > 1 categorical dimensions

    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))
    f.suptitle(category_column + " - " + attribute_x + " - " + attribute_y, fontsize=14)

    sns.violinplot(x=attribute_x, y=attribute_y,
                   data=dataf, inner="quart", linewidth=1.3, ax=ax1)
    ax1.set_xlabel(attribute_x, size=12, alpha=0.8)
    ax1.set_ylabel(attribute_y, size=12, alpha=0.8)

    sns.violinplot(x=attribute_x, y=attribute_y, hue=category_column,
                   data=dataf, inner="quart", linewidth=1.3, ax=ax2)

    ax2.set_xlabel(attribute_x, size=12, alpha=0.8)
    ax2.set_ylabel(attribute_y, size=12, alpha=0.8)
    l = plt.legend(loc='upper right', title=category_column)

    plt.show()


def Box_Plots_3D_Mix(dataf, attribute_x, attribute_y, attribute_cat):
    # Key:
    #       dataf - the dataframe that holds the entire dataset
    #       attribute_x - the attribute on the x-axis ; should be categorical
    #       attribute_y - the attribute on the y-axis ; numeric
    #       attribute_cat - the column name in dataframe holding the class labels - this will act as our categorical third dimension
    #       Note: you can also have any other categorical attribute as the second categorical attribute
    
    # Plot:
    #       Box plots for representing mixed attributes with more than one categorical variable
    #       Visualizing 3-D mix data using box plots
    #       leveraging the concepts of hue and axes for > 1 categorical dimensions


    ax = sns.boxplot(x=attribute_x, y=attribute_y, hue=attribute_cat,
                     data=dataf)
    ax.set_xlabel(attribute_x, size=12, alpha=0.8)
    ax.set_ylabel(attribute_y, size=12, alpha=0.8)

    l = plt.legend(loc='best', title=attribute_cat)
    plt.title(attribute_cat + " - " + attribute_x + " - " + attribute_y, fontsize=14)
    plt.show()


# -------------------------------------VISUALIZING DATA IN FOUR DIMENSIONS-------------------------------------#



#   One way to visualize data in four dimensions is to use depth and hue as specific data dimensions in a conventional plot

def Scatter_Plot_4D_Mix(dataf, attribute_x, attribute_y, attribute_z, category_column):
    # Key:
    #       dataf - the dataframe that holds the entire dataset
    #       attribute_x - the attribute on the x-axis ; numeric
    #       attribute_y - the attribute on the y-axis ; numeric
    #       attribute_z - the attribute on the z-axis ; numeric
    #       category_column - the column name in dataframe holding the class labels - this will act as our categorical third dimension
    
    # Plot:
    #       Visualizing 4-D mix data using scatter plots
    #       Leveraging the concepts of hue and depth
    #       Three numberic attributes and one categorical attribute

    fig = plt.figure(figsize=(8, 6))
    t = fig.suptitle(attribute_x + " - " + attribute_y + " - " + attribute_z + " - " + category_column, fontsize=14)
    ax = fig.add_subplot(111, projection='3d')

    xs = list(dataf[attribute_x])
    ys = list(dataf[attribute_y])
    zs = list(dataf[attribute_z])

    df_category_unique = pd.unique(dataf[category_column])
    dataf['color'] = 0
    color_type = ['red', 'yellow', 'blue', 'green']

    for i in range(len(df_category_unique)):
        dataf.loc[dataf[category_column] == df_category_unique[i], 'color'] = color_type[i]

    colors = dataf['color'].tolist()

    data_points = [(x, y, z) for x, y, z in zip(xs, ys, zs)]

    for data, color in zip(data_points, colors):
        x, y, z = data
        ax.scatter(x, y, z, alpha=0.4, c=color, edgecolors='none', s=30)

    ax.set_xlabel(attribute_x)
    ax.set_ylabel(attribute_y)
    ax.set_zlabel(attribute_z)

    plt.show()


def Bubble_Plot_4D_Mix(dataf, attribute_x, attribute_y, attribute_z, category_column):
    # Key:
    #       dataf - the dataframe that holds the entire dataset
    #       attribute_x - the attribute on the x-axis ; numeric
    #       attribute_y - the attribute on the y-axis ; numeric
    #       attribute_z - the attribute on the z-axis ; numeric
    #       category_column - the column name in dataframe holding the class labels - this will act as our categorical third dimension
  
    # Plot:
    #       Visualizing 4-D mix data using bubble plots
    #       Leveraging the concepts of hue and size
    #       Visualizing data in four-dimensions leveraging bubble charts and the concept of hue and size
    #       Using size to represent one of the numeric attributes
    #       Using hue to represent the categorical attribute

    size = dataf[attribute_z] * 25

    df_category_unique = pd.unique(dataf[category_column])
    dataf['edge_color'] = 0
    dataf['fill_colors'] = 0
    color_type = ['red', 'orange', 'blue', 'green']
    fill_type = ['#FF9999', '#FFE888', '#888fff', '#7fff99']

    for i in range(len(df_category_unique)):
        dataf.loc[dataf[category_column] == df_category_unique[i], 'edge_color'] = color_type[i]
        dataf.loc[dataf[category_column] == df_category_unique[i], 'fill_color'] = fill_type[i]

    edge_colors = dataf['edge_color'].tolist()
    fill_colors = dataf['fill_color'].tolist()

    plt.scatter(dataf[attribute_x], dataf[attribute_y], s=size,
                alpha=0.4, color=fill_colors, edgecolors=edge_colors)

    plt.xlabel(attribute_x)
    plt.ylabel(attribute_y)
    plt.title(attribute_x + " - " + attribute_y + " - " + attribute_z + " - " + category_column, y=1.05)

    plt.show()


def Scatter_Plot_4D_Mix_Plane(dataf, attribute_x, attribute_y, attribute_cat,
                              category_column):        # Plotting 4D in a 2D plane - @categorcial and 2 numeric attributes
    # Key:
    #       dataf - the dataframe that holds the entire dataset
    #       attribute_x - the attribute on the x-axis ; numeric
    #       attribute_y - the attribute on the y-axis ; numeric
    #       attribute_cat - the attribute represented as hue (color shade) ; categorical
    #       category_column - the column name in dataframe holding the class labels - this will act as our categorical third dimension
  

    # Plot:
    #       Visualizing 4-D mix data using scatter plots
    #       Leveraging the concepts of hue and facets for > 1 categorical attributes
    #       Two categorical attributes
    #       Two numeric attributes
    #       Easily spot multiple patterns

    col_order_types = pd.unique(dataf[category_column].values)
    hue_order_types = pd.unique(dataf[attribute_cat].values)

    g = sns.FacetGrid(dataf, col=category_column, hue=attribute_cat,
                      col_order=col_order_types, hue_order=hue_order_types,
                      aspect=1.2, size=3.5, palette=sns.light_palette('navy', 4)[1:])

    g.map(plt.scatter, attribute_x, attribute_y, alpha=0.9,
          edgecolor='white', linewidth=0.5, s=100)
    fig = g.fig
    fig.subplots_adjust(top=0.8, wspace=0.3)
    fig.suptitle(category_column + " - " + attribute_x + " - " + attribute_y + " - " + attribute_cat, fontsize=14)
    l = g.add_legend(title=attribute_cat)

    plt.show()


# -------------------------------------VISUALIZING DATA IN FIVE DIMENSIONS-------------------------------------#



def Bubble_Chart_5D_Mix(dataf, attribute_x, attribute_y, attribute_z, attribute_s, category_column):
    # Key:
    #       dataf - the dataframe that holds the entire dataset
    #       attribute_x - the attribute on the x-axis ; numeric
    #       attribute_y - the attribute on the y-axis ; numeric
    #       attribute_z - the attribute on z-axis; numeric
    #       attribute_s - the attribute represented as varying size ; nummeric
    #       category_column - the column name in dataframe holding the class labels - this will act as our categorical dimension
 
    # Plot: 
    #       Visualizing 5-D mix data using bubble charts
    #       leveraging the concepts of hue, size and depth
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    t = fig.suptitle(
        attribute_x + " - " + attribute_y + " - " + attribute_z + " - " + attribute_s + " - " + category_column,
        fontsize=14)

    xs = list(dataf[attribute_x])
    ys = list(dataf[attribute_y])
    zs = list(dataf[attribute_z])
    data_points = [(x, y, z) for x, y, z in zip(xs, ys, zs)]

    scale = 20
    ss = list(dataf[attribute_s] * scale)

    df_category_types = pd.unique(dataf[category_column])

    colors = []

    for wt in list(dataf[category_column]):
        if wt == df_category_types[0]:
            colors.append('red')
        elif wt == df_category_types[1]:
            colors.append('blue')
        else:
            colors.append('yellow')


    for data, color, size in zip(data_points, colors, ss):
        x, y, z = data
        ax.scatter(x, y, z, alpha=0.4, c=color, edgecolors='none', s=size)

    ax.set_xlabel(attribute_x)
    ax.set_ylabel(attribute_y)
    ax.set_zlabel(attribute_z)

    plt.show()


def Bubble_Chart_5D_Mix_Plane(dataf, attribute_x, attribute_y, attribute_z, attribute_cat, category_column):
    # Key:
    #       dataf - the dataframe that holds the entire dataset
    #       attribute_x - the attribute on the x-axis ; numeric
    #       attribute_y - the attribute on the y-axis ; numeric
    #       attribute_z - the attribute represented as varying size ; nummeric
    #       attribute_cat - the attribute represented as hue (color intensity) ; categorical
    #       category_column - the column name in dataframe holding the class labels - this will act as our categorical dimension

    # Plot:
    #       Visualizing 5-D mix data using bubble charts
    #       Leveraging the concepts of hue, size and facets

    col_order_types = pd.unique(dataf[category_column].values)
    hue_order_types = pd.unique(dataf[attribute_cat].values)
    scale = 100

    g = sns.FacetGrid(dataf, col=category_column, hue=attribute_cat,
                      col_order=col_order_types, hue_order=hue_order_types,
                      aspect=1.2, size=3.5, palette=sns.light_palette('black', 4)[1:])
    g.map(plt.scatter, attribute_x, attribute_y, alpha=0.8,
          edgecolor='white', linewidth=0.5, s=dataf[attribute_z] * scale)
    fig = g.fig
    fig.subplots_adjust(top=0.8, wspace=0.3)
    fig.suptitle(
        category_column + " - " + attribute_x + " - " + attribute_y + " - " + attribute_z + " - " + attribute_cat,
        fontsize=14)
    l = g.add_legend(title=attribute_cat)

    plt.show()


# -------------------------------------VISUALIZING DATA IN SIX DIMENSIONS-------------------------------------#

# We will leverage depth, hue, size and shape besides our regular two axes to depict all the six data dimensions.


def Scatter_Plot_6D(dataf, attribute_x, attribute_y, attribute_z, attribute_s, attribute_cat, category_column):
    # Key:
    #       dataf - the dataframe that holds the entire dataset
    #       attribute_x - the attribute on the x-axis ; numeric
    #       attribute_y - the attribute on the y-axis ; numeric
    #       attribute_z - the attribute on the z-axis ; numeric
    #       attribute_s - the attribute represented as varying size ; nummeric
    #       attribute_cat - the attribute represented as hue (color intensity) ; categorical
    #       category_column - the column name in dataframe holding the class labels - this will act as our categorical dimension

    # Plot:
    #       Visualizing 6-D mix data using scatter charts
    #       Leveraging the concepts of hue, size, depth and shape

    fig = plt.figure(figsize=(8, 6))
    t = fig.suptitle(
        category_column + " - " + attribute_x + " - " + attribute_y + " - " + attribute_z + " - " + attribute_s + " - " + attribute_cat,
        fontsize=14)
    ax = fig.add_subplot(111, projection='3d')

    xs = list(dataf[attribute_x])
    ys = list(dataf[attribute_y])
    zs = list(dataf[attribute_z])
    data_points = [(x, y, z) for x, y, z in zip(xs, ys, zs)]

    df_category_types = pd.unique(dataf[category_column])
    df_attricute_cat_types = pd.unique(dataf[attribute_cat])

    scale = 10
    ss = list(dataf[attribute_s] * scale)
    colors = ['red' if wt == df_category_types[0] else 'blue' if wt == df_category_types[1] else 'yellow' for wt in
              list(dataf[category_column])]
    markers = [',' if q == df_attricute_cat_types[0] else 'x' if q == df_attricute_cat_types[1] else 'o' for q in
               list(dataf[attribute_cat])]

    for data, color, size, mark in zip(data_points, colors, ss, markers):
        x, y, z = data
        ax.scatter(x, y, z, alpha=0.4, c=color, edgecolors='none', s=size, marker=mark)

    ax.set_xlabel(attribute_x)
    ax.set_ylabel(attribute_y)
    ax.set_zlabel(attribute_z)

    plt.show()


def Scatter_Plot_6D_Mix_Plane(dataf, attribute_x, attribute_y, attribute_s, attribute_cat1, attribute_cat2, category_column):
    # Key:
    #       dataf - the dataframe that holds the entire dataset
    #       attribute_x - the attribute on the x-axis ; numeric
    #       attribute_y - the attribute on the y-axis ; numeric
    #       attribute_s - the attribute represented as varying size ; nummeric
    #       attribute_cat_1 - the attribute represented as color ; categorical
    #       attribute_cat_2 - the attribute represented as hue (color intensity) ; categorical
    #       category_column - the column name in dataframe holding the class labels - this will act as our categorical dimension
    
    # Plot:
    #       Visualizing 6-D mix data using scatter charts
    #       Leveraging the concepts of hue, facets and size

    g = sns.FacetGrid(dataf, row=category_column, col=attribute_cat1, hue=attribute_cat2, size=2.0)
    g.map(plt.scatter, attribute_x, attribute_y, alpha=0.5,
          edgecolor='k', linewidth=0.5, s=dataf[attribute_s] * 2)
    fig = g.fig
    fig.set_size_inches(30, 10)
    fig.subplots_adjust(top=0.85, wspace=0.3)
    fig.suptitle(
        category_column + " - " + attribute_x + " - " + attribute_y + " - " + attribute_s + " - " + attribute_cat1 + " - " + attribute_cat2,
        fontsize=14)
    l = g.add_legend(title=attribute_cat2)

    plt.show()

