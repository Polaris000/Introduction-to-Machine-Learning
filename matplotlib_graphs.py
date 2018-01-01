import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]
y = [10, 15, 30, 41, 32]


# LINE GRAPH #  
# plt.plot(X, y)
# plt.show()  # without the show(), the plot will not be displayed
# _____________________________________________________________

# SCATTER PLOT #
# plt.scatter(X, y) displays a scatter plot

# plt.xscale('log') displays the x axis on a log scale
# ______________________________________________________________

# HISTOGRAM #
# plt.hist(X, bins=10)  # the bins argument divides X into sections
                     # and then graphs the number of datapoints falling
                     # in each section or bins
# plt.show()

# plt.clf() clears a graph
# ______________________________________________________________

# ENHANCEMENTS #

# The axes can be labeled using the: plt.xlabel() and plt.ylabel() functions
# plt.title() gives title aat the top of the graph.
# ______________________________________________________________

# Ticks
# you can change the marks on the scale using ticks
# use plt.xticks() and plt.yticks()

# first arg is the tick_list, second is the tick_var
# eg.
# tick_val = [1000,10000,100000]
# tick_lab = ['1k','10k','100k'] --> these are displayed on the plot
# ______________________________________________________________

# Size
# you can specify the size of plots on a scatter plot by using a third variable,
# substituted as a np_array, using np.array() func in np lib.

# plt.scatter(X, y, s=np_array) -->syntax
# ______________________________________________________________

# Colours
# plt.scatter(X, y, s=np_array, c=col) --> syntax
# here col is a list that is generated before the plt is made.
# ______________________________________________________________

#Opacity
# alpha is the parameter used
# alpha = 1 is opague and 0 is transparent
# plt.scatter(X, y, s=np_array, c=col, alpha=0.8) --> syntax
# ______________________________________________________________

# Text
# Can be used to add labels to datapoints
# Eg. plt.text(1550, 71, 'India') --> text(X, y, text)
# plt.text(5700, 80, 'China')
# ______________________________________________________________

# Gridlines
# plt.grid(True)
# ______________________________________________________________


#** Detailed study can be done using the official matplotlib documentation
