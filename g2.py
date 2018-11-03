import matplotlib.pyplot as plt

# x-coordinates of left sides of bars 
left=[1,2,3,4,5,6]

#heights of bars 
height=[10, 20, 30 ,40, 50, 60]

#table for bar chart
tick_label=['one','two','three','four','five','six']

#plotting a bar chart 
plt.bar(left. height, tick_label=tick_label
		width=o.8, color=[ 'blue' , 'yellow'])

#naming the x-axis
plt.xlabel('x-axis')
#naming the y-axis
plt.ylabel('y-axis')
#plot title
plt.title("My bar chart.")

#function to show the plot 
plt.show()