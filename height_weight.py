import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import pandas as pd

df = pd.read_csv('height-weight.csv')
height_list = df['Height'].to_list()
weight_list = df['Weight'].to_list()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_stdev = statistics.stdev(height_list)
weight_stdev = statistics.stdev(weight_list)

print("mean, median & mode of height is: {},{} & {} respectively".format(height_mean, height_median, height_mode))
print("mean, median & mode of weight is: {},{} & {} respectively".format(weight_mean, weight_median, weight_mode))

height_1_stdev_start,height_1_stdev_end = height_mean-height_stdev, height_mean+height_stdev
height_2_stdev_start,height_2_stdev_end = height_mean-(2*height_stdev), height_mean+(2*height_stdev)
height_3_stdev_start,height_3_stdev_end = height_mean-(3*height_stdev), height_mean+(3*height_stdev)

weight_1_stdev_start,weight_1_stdev_end = weight_mean-weight_stdev, weight_mean+weight_stdev
weight_2_stdev_start,weight_2_stdev_end = weight_mean-(2*weight_stdev), weight_mean+(2*weight_stdev)
weight_3_stdev_start,weight_3_stdev_end = weight_mean-(3*weight_stdev), weight_mean+(3*weight_stdev)

height_listofdata_within_1_std = [result for result in height_list if result>height_1_stdev_start and result<height_1_stdev_end]
weight_listofdata_within_1_std = [result for result in weight_list if result>weight_1_stdev_start and result<weight_1_stdev_end]

height_listofdata_within_2_std = [result for result in height_list if result>height_2_stdev_start and result<height_2_stdev_end]
weight_listofdata_within_2_std = [result for result in weight_list if result>weight_2_stdev_start and result<weight_2_stdev_end]

height_listofdata_within_3_std = [result for result in height_list if result>height_3_stdev_start and result<height_3_stdev_end]
weight_listofdata_within_3_std = [result for result in weight_list if result>weight_3_stdev_start and result<weight_3_stdev_end]

print("{}% of data for height lies within 1 standard deviation".format(len(height_listofdata_within_1_std)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(height_listofdata_within_2_std)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(height_listofdata_within_3_std)*100.0/len(height_list)))

print("{}% of data for weight lies within 1 standard deviation".format(len(weight_listofdata_within_1_std)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard deviation".format(len(weight_listofdata_within_2_std)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard deviation".format(len(weight_listofdata_within_3_std)*100.0/len(weight_list)))