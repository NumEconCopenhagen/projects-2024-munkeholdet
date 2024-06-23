
# Converts periodically data to yearly, by taking the average over the period. This function only returns 2016 and forward.
def period_to_yearly(location, period=4): 
    yearly_data = []
    sum_period = [] # Used as a placeholder to sum up 4 periods at a time, or however many datapoints there is in your period.

    for i in location:
        sum_period.append(i) # appends the data point. 
        if len(sum_period) == period: # if the amount of data points corresponds to the periods you inputted, then run:
            sum_period = [float(x) for x in sum_period] # make them floats, else throws an int error.
            yearly_data.append(sum(sum_period)) # insert them in the yearly_data list
            sum_period = [] # clean the placeholder and repeat loop
    
    yearly_data = [round(x,2)/period for x in yearly_data] # round the data to two digits in the list, else there are 10 decimal places..

    return yearly_data

# Redefines the new index value by what value you want as base from your given list 
def rebase_index(index_data, base_from_list=0):
    index_list = [] # initialize index list
    base = index_data[base_from_list] # standard is to define your first data point as the yearly index 100, but you can select whatever you want

    for i in range(len(index_data)):
        index_list.append(index_data[i]/base * 100) # all other list values get adjust according to your select base.
    
    index_list = [round(x,2) for x in index_list] # round the data to two digits..
    return index_list
