#################### Part 3 ######################################
import seaborn as sns
import matplotlib.pyplot as plt
##################### 1 ##########################################
# Our three questions:
# 1) Does the region born effect female life expectancy?
# 2) Is there a realationshsip between tertaiary education for women and women of parliament?
# 3) Does the presence of physicians effect life expectancy (males, females)?

#################### 2 ###########################################
import pandas as pd

#################### 3 #########################################
# Import data from sheets
data = pd.read_csv("wdi_wide.csv")
# Transform it into a dataframe
our_data = pd.DataFrame(data)
data_physicians = pd.DataFrame(data["Physicians"])
data_population = pd.DataFrame(data["Population"])
data_physicians.info()
data_population.info()
# Since there are 218 entries. We can determine that there are 10 collums for Physicians that are empty and 0 for popualation 

##################### 4 #########################################
#   Seperate all the varaiubles we are using. nunique (tells us how many uniqye values exist)
Regions = our_data["Region"]. nunique()
female_life_expectancy = our_data["Life expectancy, female"]. nunique()
male_life_expectancy = our_data["Life expectancy, male"]. nunique()
tertiary_ed_women = our_data["Tertiary education, female"]. nunique()
female_parliament = our_data["Women in national parliament"]. nunique()
physicians = our_data["Physicians"]. nunique()

################## 5 #############################################
# The describe fuction is used to generate descriptive statistics about your data set (more specific). It give you information such as: the mean, the standard deviation, the maximum, the minimum, the amount of values, the deviation(percentile) etc.
print(our_data.describe())

################## 6 #############################################
#Adding new collum
our_data["GNI_per_capita"] = (our_data["GNI"] / our_data["Population"]). round(2)

################## 7 ###########################################
# a) How many countries are there in each region?
print(our_data["Region"]. value_counts())
# There are: Africa 54/  Asia 50/  Europe 47/ Americas 46 / Oceania 19

# b) How many high income economies are there?
print(our_data["High Income Economy"]. value_counts())
# There a 150 zero's and 67 one's

################# 8 ############################################
# Where are the high income economies? Per region, including Yes and No.
print(pd.crosstab(our_data["High Income Economy"], our_data["Region"]))
# They come from Europe has the highest number for 1)

############### 9 ###############################################
# We can do this without a loop
# Can you tell me how many countries there are where women can expect to live for more than 80 years? And which countries those are?
filtered_data = our_data[our_data["Life expectancy, female"] > 80]
# Count how many countries meet this condition
count_countries = filtered_data["Country Name"].nunique()
print("Number of countries where female life expectancy > 80 years:", count_countries)
print("These countries are:")
print(filtered_data["Country Name"].unique())
# There are 66 countries where woman can expect to live more then 80 years. 

##################################### Part 4 #################################################

############### 1 ##################################################
#1) Is there any association between GNI per capita and Life expectancy?
sns.relplot (data= our_data, 
             x="GNI_per_capita", 
             y="Life expectancy, female",
             hue = "Region",  # gives color  to the points from diffrent regions
)
plt.title("GNI per capita and its realtionship with Life Expectancy")
plt.show()

########### 2 ########################################################
# 2) By adding a third “feature” to your plot using colors to represent it in order to answer the following question: “Does the association between GNI per capita and life expectancy vary by region?
# The third feature is size = population
sns.relplot( data=our_data, 
            x="GNI_per_capita", 
            y="Life expectancy, female", 
            hue="Region",        # gives color to the points from diffrent regions
            size="Population",    # bubble size for population
)
plt.title("GNI per capita hand its realationship with Life Expectancy by Region and Population Sizes")
plt.xlabel("GNI per capita ")
plt.ylabel("Life Expectancy, female")
plt.xscale("log") # this will change our x axis to a logarithmic scale instead of a linear scale to help see the pattern better. When plotting it, the result was very compresed. So with log, it will be less compressed by spreading out the smaller values and compressing thee larger ones.
plt.show()

############ 3 ##############################################################
#3)Generate a the plot from item 2, now using lines along with standard deviation.
# Why can't you see the area representing a standard deviation in the plot? Answer in repport.
sns.lineplot(
    data=our_data,
    x="GNI_per_capita",
    y="Life expectancy, female",
    hue="Region",   
    errorbar="sd", # standard deviation 
)
plt.title("GNI per capita and its realtionship with Life Expectancy (with a Standard Deviation)")
plt.xlabel("GNI per capita")
plt.ylabel("Life expectancy, female")
plt.xscale("log")  # same thing explained at the top 
plt.show()

########## 4 ####################################################################
# 4)  Use the lmplot() function to generate a linear regression for the previous plot.
sns.lmplot (
    data=our_data,
    x="GNI_per_capita",
    y="Life expectancy, female",
    hue="Region",
)
plt.title(" GNI per capita  and its relationship with Life Expectancy (with a linear regression) ")
plt.xlabel("GNI per capita")
plt.ylabel("Life expectancy, female")
plt.xscale("log")  
plt.show()

    