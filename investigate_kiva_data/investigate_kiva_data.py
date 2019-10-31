# Investigate a Kiva Lending Datas.
loan_amount = [1250.0, 500.0, 1450.0, 200.0, 700.0, 100.0, 250.0, 225.0, 1200.0, 150.0, 600.0, 300.0, 700.0, 125.0, 650.0, 175.0, 1800.0, 1525.0, 575.0, 700.0, 1450.0, 400.0, 200.0, 1000.0, 350.0]
country_name = ['Azerbaijan', 'El Salvador', 'Bolivia', 'Paraguay', 'El Salvador', 'Philippines', 'Philippines', 'Nicaragua', 'Guatemala', 'Philippines', 'Paraguay', 'Philippines', 'Bolivia', 'Philippines', 'Philippines', 'Madagascar', 'Georgia', 'Uganda', 'Kenya', 'Tajikistan', 'Jordan', 'Kenya', 'Philippines', 'Ecuador', 'Kenya']
time_to_raise = [193075.0, 1157108.0, 1552939.0, 244945.0, 238797.0, 1248909.0, 773599.0, 116181.0, 2288095.0, 51668.0, 26717.0, 48030.0, 1839190.0, 71117.0, 580401.0, 800427.0, 1156218.0, 1166045.0, 2924705.0, 470622.0, 24078.0, 260044.0, 445938.0, 201408.0, 2370450.0]
num_lenders_total = [38, 18, 51, 3, 21, 1, 10, 8, 42, 1, 18, 6, 28, 5, 16, 7, 54, 1, 18, 22, 36, 12, 8, 24, 8]

# Compute the total amount of money loaned and store it in the variable loan_total.
def sum_list(lst):
    lst_total=0
    for x in lst:
        lst_total+=x
    return lst_total

loan_total = sum_list(loan_amount)

# Compute the average amount of money loaned and store it in the variable loan_average.
def sum_list(yourlist):
    list_total = 0
    for item in yourlist:
        list_total += item
    return list_total

loan_average = sum_list(loan_amount)/len(loan_amount)

# Find out the minimum loan and maximum loan and the countries that received those loans.
min_loan = min(loan_amount)
max_loan = max(loan_amount)
max_country = country_name[loan_amount.index(max_loan)]
min_country = country_name[loan_amount.index(min_loan)]

# Compute the average number of lenders per loan and store it in a variable average_lenders.
lenders_sum = 0
for item in num_lenders_total:
    lenders_sum += item
average_lenders = lenders_sum/len(num_lenders_total)

# Compute the total number of loans made to the Philippines and store it in a variable philippines_count.
philippines_count = country_name.count("Philippines")

# For each unique country name, print a line that shows the name of the country and then the number of loans made in that country.
unique_countries = ['Guatemala', 'Paraguay', 'Tajikistan', 'Kenya', 'Azerbaijan', 'El Salvador', 'Bolivia', 'Ecuador', 'Georgia', 'Philippines', 'Uganda', 'Madagascar', 'Nicaragua', 'Jordan']
for country in unique_countries:
    print(country, country_name.count(country))

# Find the index positions for the Phillipines. 
# Use that information to compute the average loan amount for the Phillipines. Store your result in the variable p_average.
loan_amount_sum = 0
index_positions = []

for n in range(len(country_name)):
    if country_name[n] == "Philippines":
        index_positions.append(n)

for i in index_positions:
    loan_amount_sum += loan_amount[i]
p_average = loan_amount_sum/len(index_positions)

# Find the name of the country with the loan that took the longest to raise.
# Store your result in the variable longest_to_fund.
longest_to_fund = country_name[time_to_raise.index(max(time_to_raise))]
print(longest_to_fund)

# What is the arithmetic mean of the time / dollar it takes to fund a loan?
# Store your result in the variable a_mean.
arithmetic_sum = 0

for i in range(len(loan_amount)):
    arithmetic_sum += time_to_raise[i]/loan_amount[i]

a_mean = arithmetic_sum/len(loan_amount)

# Calculate the standard deviation of the loan_amount variable and store the variance in loan_var and the standard deviation in loan_stdev.
def var_stdev(yourlist):
    mean = sum(yourlist)/len(yourlist)
    var = 0
    for x in yourlist:
        var += ((x - mean)**2)/len(yourlist)
    stdev = var**0.5
    return var, stdev

loan_var, loan_stdev = var_stdev(loan_amount)

# Calculate the pearson correlation between the loan_amount and the num_lenders_total or between time_to_raise and the loan_amount or between num_lenders_total and time_to_raise. 
# If you divide up the class you can compare values to see which pair has the strongest correlation.
loan_amount_num_lenders = 0
loan_amount_ttr = 0
num_lenders_ttr = 0

def var_stdev(yourlist):
    mean = sum(yourlist)/len(yourlist)
    var = 0
    for x in yourlist:
        var += ((x - mean)**2)/len(yourlist)
    stdev = var**0.5
    return var, stdev

def covar(list1, list2):
    n = len(list1) #both list1 and list 2 have the same length
    covar = 0
    mean1 = sum(list1)/len(list1)
    mean2 = sum(list2)/len(list2)
    for i in range(n):
        covar += (list1[i] - mean1)*(list2[i] - mean2)/n
    return covar

def pearson(list1, list2):
    pearson = covar(list1, list2)/(var_stdev(list1)[1]*var_stdev(list2)[1])
    return pearson
    
pearson1 = pearson(loan_amount, num_lenders_total)
pearson2 = pearson(time_to_raise, loan_amount)
pearson3 = pearson(num_lenders_total, time_to_raise)
print("The pair that has the strongest correlation is", max(pearson1, pearson2, pearson3))

