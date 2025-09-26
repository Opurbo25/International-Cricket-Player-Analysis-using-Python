#import libraries
import pandas as pd
import matplotlib.pyplot as plt

#reading the csv file
df=pd.read_csv("ODI.csv")

#Checking the DataFrame
df.head()

#Checking the columns
df.columns

#Dropping unnecessary columns
df.drop(["Unnamed: 0","Unnamed: 13"],axis=1,inplace=True)

#Checking data type
df.dtypes

#converting string to numeric data
columns=["Inns","NO","Runs","HS","Ave","BF","SR"]
for col in columns:
    df[col]=pd.to_numeric(df[col],errors="coerce")

#Determining how many player are here
player=df["Player"].nunique()
print(player)

#Determining whice palyer scores most run
player=df.loc[df["Runs"].idxmax()]["Player"]
print(player)

#Determining whice palyer scores most century
player=df.loc[df["100"].idxmax()]["Player"]
print(player)

#Determining whice player has scored most 50+ run
player=df.loc[df["50"].idxmax()]["Player"]
print(player)

#Determining top 5 player with longest career span
df["Start_year"]=df["Span"].str.split("-").str[0].astype("int")
df["End_year"]=df["Span"].str.split("-").str[1].astype("int")
df["Career_lenght"]=df["End_year"]-df["Start_year"]
longest=df.nlargest(5,"Career_lenght")[["Player","Career_lenght"]]
print(longest)

#determining top 10 batsman based on strike rate
top=df.nlargest(10,"SR")[["SR","Player"]]
print(top)

#Creating a scatter plot of total run vs innings
plt.scatter(df["Inns"],df["Runs"])
plt.xlabel("Innings")
plt.ylabel("Runs")
plt.title("Runs vs Innings")
plt.show()

#determing the average batting score
avg=df["Ave"].mean()
print(avg)

#Calculate the average runs according to career length
avg=df.groupby("Career_lenght")["Ave"].mean()
print(avg)

#Creating a scatter plot of 100s vs 50s
plt.scatter(df["50"],df["100"])
plt.xlabel("50")
plt.ylabel("100s")
plt.title("100s vs 50s")
plt.show()

#determing player with most no out(NO)
player=df.loc[df["NO"].idxmax()]["Player"]
print(player)

#determining the top 5 batsmen based on balls faced (BF)
players=df.nlargest(5,"BF")[["Player","BF"]]
print(players)

# determing during which decade did the most players start their careers
df["decade"]=(df["Start_year"]//10)*10
dec=df.loc[df["decade"].idxmax()]["decade"]
print(dec)

#creating a bar chart of top 10 batsman based on run
top10=df.nlargest(10,"Runs")
plt.bar(top10["Player"],top10["Runs"])
plt.xlabel("Player")
plt.ylabel("Runs")
plt.title("Top 10 player with most runs")
plt.show()

#determining 100s + 50s total and show the top 5 players
df["t100_50"]=df["100"]+df["50"]
df["t100_50"]=pd.to_numeric(df["t100_50"],errors="coerce")
players=df.nlargest(5,"t100_50")[["Player","t100_50"]]
print(players)

#Creating a “Runs per Innings” column and show the top 10 batsmen
df["RpI"]=df["Runs"]/df["Inns"]
players=df.nlargest(5,"RpI")[["Player","RpI"]]
print(players)

#Creating a scatter plot of Strike Rate vs. Batting Average
plt.scatter(df["Ave"],df["SR"])
plt.xlabel("Batting Average")
plt.ylabel("Strike Rate")
plt.title("Strike Rate vs Batting Average")
plt.show()

#Creating a histogram of total runs
plt.hist(df["Runs"],bins=10)
plt.xlabel("Number of Players")
plt.ylabel("Runs")
plt.title("A histogram of total runs")
plt.show()
