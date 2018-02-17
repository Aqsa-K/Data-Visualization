import pandas as pd                         # Import pandas to create and deal with dataframes
import VisualizeData                        # Import VisualizeData - this will be used to call the fucntions from the script 'VisualizeData'
from sklearn.datasets import load_iris      # Import the IRIS dataset from sklearn

# We will apply different visualization techniques on the IRIS dataset
# to understand the purpose and output plots of each of the visualization functions in 'VisualizeData'



def preprocess_dataframe(dataframe):
    # create separate dataframes for the three classes
    dataf = dataframe
    cat_0 = dataf[dataf['Category'] == 0]
    cat_1 = dataf[dataf['Category'] == 1]
    cat_2 = dataf[dataf['Category'] == 2]

    # return the separate and combined dataframe 
    return cat_0, cat_1, cat_2, dataf

if __name__ == "__main__":
    Iris = load_iris()

    X = Iris.data           # load the data inputs into X
    Y = Iris.target         # load the data labels into Y

    # Create a pandas dataframe by passing the data(rows - 'X' here) and the columns names
    dataframe = pd.DataFrame(X, columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
    
    # Add the target labels to the dataframe under a new column name('Category')
    dataframe['Category'] = Y


    # Let's create dataframe for each of the three classes as well
    Setosa, Versicolour, Virginica, dataf = preprocess_dataframe(dataframe)

    # Uncomment this to see how the data has been separated out for each of the classes, and the combined data as well 
    # print("Setosa : ", Setosa)
    # print("Versicolor: ", Versicolour)
    # print("Virginica: ", Virginica)
    # print("Dataf: ", dataf)


    # Define list of attributes - you can then pass this list to functions wherever feasible
    subset_attributes = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
    VisualizeData.SubsetAttributes(dataf, subset_attributes)
    VisualizeData.Plot_Histograms(dataf)
    VisualizeData.Plot_Single_Attribute_Hist_Density_Plot(dataf, "Sepal Length")
    VisualizeData.Plot_Single_Categorical_Attribute(dataf, 'Category')


    # TWO DIMENSIONAL PLOTS:

    VisualizeData.Correlation_Matrix_HeatMap(dataf)

    VisualizeData.Pair_Wise_Scatter_Plot(dataf, subset_attributes)
    VisualizeData.Parallel_Coordinates(dataf, subset_attributes, 'Category')
    VisualizeData.Plot_Scatter_Joint(dataf, ['Sepal Length', 'Petal Length'])

    VisualizeData.TwoD_Categorical_Bar_Plots(Setosa, Versicolour,'Category', 'Setosa', 'Versicolour')
    VisualizeData.Categorical_Bar_Plots_3Class_2D(Setosa, Versicolour, Virginica, 'Category', 'Setosa', 'Versicolour', 'Virginica', 'Category Frequency in Each Class')
    VisualizeData.Mixed_Attributes_Hist_Density_Plot(Setosa, Versicolour, 'Sepal Length', 'Setosa', 'Versicolour')

    VisualizeData.Mixed_Attributes_Hist_Density_Plot_3_Classes(Setosa, Versicolour, Virginica, 'Sepal Length', 'Setosa', 'Versicolour', 'Virginica')
    VisualizeData.Multiple_Histogram(dataf, 'Sepal Length', 'Category')

    VisualizeData.Box_Plots(dataf, 'Category', 'Sepal Length')
    VisualizeData.Violin_Plots(dataf, 'Category', 'Sepal Length')



    # THREE DIMENSIONAL PLOTS:

    attributes = ['Sepal Length','Sepal Width', 'Petal Length', 'Petal Width', 'Category']
    VisualizeData.Pair_Wise_Scatter_Plot_3D(dataf, attributes, 'Category')

    VisualizeData.Numeric_Data_3D(dataf, "Sepal Length", "Sepal Width", "Petal Length")

    VisualizeData.Bubble_Chart_3D(dataf, "Sepal Length", "Sepal Width", "Petal Length")

    VisualizeData.Scatter_Plot_3D_Mix_Data(dataf, "Sepal Length", "Petal Length", "Category")

    VisualizeData.Kernel_Density_Plot_3D(Setosa, Versicolour, "Sepal Length", "Petal Length")


    # FOUR DIMENSIONAL DATA:

    VisualizeData.Scatter_Plot_4D_Mix(dataf, "Sepal Length", "Petal Width", "Sepal Width", "Category")

    VisualizeData.Bubble_Plot_4D_Mix(dataf, "Sepal Length", "Petal Width", "Sepal Width", "Category")


    # FIVE DIMENSIONAL DATA:

    VisualizeData.Bubble_Chart_5D_Mix(dataf, "Sepal Length", "Petal Width", "Sepal Width", "Petal Length", "Category")

