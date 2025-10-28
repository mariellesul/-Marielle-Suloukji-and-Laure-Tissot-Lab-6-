#################### Part 3 ######################################
import seaborn as sns

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

                         ######## PART 4 #########
import matplotlib.pyplot as plt                         
                         
############### 1 ##################################################
#1) Is there any association between GNI per capita and Life expectancy?
sns.relplot (data= our_data, 
             x="GNI_per_capita", 
             y="Life expectancy, female",
             hue = "Region",  # gives color  to the points from diffrent regions
)
plt.title("GNI per capita vs Life Expectancy")
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
plt.title("GNI per Capita vs Life Expectancy by Region and Population Sizes")
plt.xlabel("GNI per capita ")
plt.ylabel("Life Expectancy, female")
plt.xscale("log") # this will change our x axis to a logarithmic scale instead of a linear scale to help see the pattern better. When plotting it, the result was very compresed. So with log, it will be less compressed by spreading out the smaller values and compressing thee larger ones.
plt.show()

############ 3 ##############################################################
#3)Generate a the plot from item 2, now using lines along with standard deviation.
sns.lineplot(
    data=our_data,
    x="GNI_per_capita",
    y="Life expectancy, female",
    hue="Region",   
    errorbar="sd", # standard deviation 
)
plt.title("GNI per Capita vs Life Expectancy with a Standard Deviation")
plt.xlabel("GNI per capita")
plt.ylabel("Life expectancy, female")
plt.xscale("log")  # same thing explained at the top 
plt.show()

############ 4 ##############################################################
# 4)  Use the lmplot() function to generate a linear regression for the previous plot.
sns.lmplot (
    data=our_data,
    x="GNI_per_capita",
    y="Life expectancy, female",
    hue="Region",
)
plt.title("Linear Regression: GNI per Capita vs Life Expectancy ")
plt.xlabel("GNI per capita")
plt.ylabel("Life expectancy, female")
plt.xscale("log")  
plt.show()

############ 5 ##############################################################

####Relationship life expectancy and greenhouse gas (male and female life expectancy)
sns.relplot(data=our_data , 
            x="Life expectancy, female" , 
            y="Greenhouse gas emissions" , 
            col="Region" ,kind="scatter")
plt.title("Female life expectancy vs Greenhouse gas emissions")
plt.show()
sns.relplot(data=our_data , 
            x="Life expectancy, male" , 
            y="Greenhouse gas emissions" , 
            col="Region" , kind="scatter")
plt.title("Male life expectancy vs Greenhouse gas emissions")
plt.show()

###5 questions
##Does the amount of physicians present per region affect the female life expectancy
sns.relplot(data=our_data , 
            x="Life expectancy, female" , 
            y="Physicians" , 
            col="Region" ,kind="scatter")
plt.title("Female life expectancy vs Greenhouse gas emissions")
plt.show()

##Does the GNI in each reagion affect the female life expectancy (do they have enough money for the ressources they need)
sns.relplot(data=our_data , 
            x="Life expectancy, female" , 
            y="GNI" , col="Region" , 
            kind="scatter")
plt.title("Female life expectancy vs Greenhouse gas emissions")
plt.show()

##Does the education of women affect the life expectancy of women since they might have other more dangerous positions open
sns.relplot(data=our_data , 
            x="Life expectancy, female" , 
            y="Tertiary education, female" , 
            size="Population" , 
            col="Region" ,kind="scatter")
plt.title("Female life expectancy vs Greenhouse gas emissions")
plt.show()

##Is female life expectancy linked to greenhouse gas emissions that could be a result of international tourism
sns.relplot(data=our_data , 
            x="Life expectancy, female" , 
            y="Greenhouse gas emissions" , 
            size="International tourism" , 
            col="Region" , 
            kind="scatter")
plt.title("Female life expectancy vs Greenhouse gas emissions")
plt.show()

##
sns.relplot(data=our_data , 
            x="Life expectancy, female" , 
            y="Greenhouse gas emissions" , 
            col="Region" , 
            kind="scatter")
plt.title("Female life expectancy vs Greenhouse gas emissions")
plt.show()


############ 6 ##############################################################

##a)
our_data["emissions_per_capita"] = (our_data["Greenhouse gas emissions"] / our_data["Population"])

sns.lmplot(data=our_data , 
           x="emissions_per_capita" , 
           y="Internet use") #to look at a linear regression relationship

sns.relplot(data=our_data , 
            x="emissions_per_capita" , 
            y="Internet use" , 
            kind="scatter") #only a scatter plot relationship

plt.title("Emissions per capita vs Internet use")

##b)
filtered_values_for_emissions= our_data[our_data['emissions_per_capita'] > 0.03]
print(filtered_values_for_emissions ['Country Name'] )


##c)


##d)









