import matplotlib.pyplot as plt
import pandas as pd


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
 # df = pd.read_csv("Data.csv");
  ## read colum
  ## df.columns
  # Date = df.colums["Date"]
  #Time = df.colums["Time"]
  #Count = df.colums["Count"]
  #Velocity = df.columns["Velocity"]
  ## read each column
  ## df.[['Date','Velocity']]
  #data x,y
 # x = df.["Date"]
 # y =
  #bar_chart
 # plt.xlabel("time")
 # plt.ylabel("Count")
 # plt.bar(x,y)
 # plt.show()
 #dtf = pd.to_datime()
 #with open("Data.csv","r") as file :
 #    for line in file:
 #        Data = line.split(",") #line.strip.split()
 #Plot Count
 #plt.plot()
 #plt.show
 #Plot Velocity
 #plt.plot()
# plt.show
 #Plot Round
# plt.plot()
 #plt.show

  df = pd.read_csv("DATA.TXT",sep = ',')
  Date = df["Date"]

  #print(Date)
  date_old = None
  for date in Date:
     if date != date_old :
        #df.set_index("Date")
        Data = df.loc[df["Date"]==date]
        x = Data["Time"]

        y = Data["Count"].astype("int")

        #y = [int(c) for c in Data["Count"]]
        #Group = Data[["Time","Count"]]
        #gx = Group.groupby("Time")
        #x = Data["Time"].unique()
       # print(x)
        #y = []
        #for i in gx:
        #    print(i)
            #y = [y,i.count()]


        #Label
        plt.title(str(date))
        plt.xlabel("time")
        plt.ylabel("Count")
        plt.bar(x, y)
        #plt.scatter(x,y)
       # plt.gcf().autofmt_xdate()
        plt.xticks(rotation = "vertical")
        plt.show()
        date_old = date
  #for date in Date:
   # if date != date_old:
    #  df.set_index("Date", inplace=True)
     # Data = df.loc([str(date)])
     # x = Data.colums["Time"]
     # y = Data.colums["Velocity"]

      # Label
    #  plt.legend[str(date)]
      # bar_chart
    #  plt.xlabel("time")
    #  plt.ylabel("Velocity")
    #  plt.bar(x, y)
   #   plt.show()
    #  date_old = date