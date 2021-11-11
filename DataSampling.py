import random
import pandas as pd
import statistics as st
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

# Base Graph Code from line10 to line 13.

fig = ff.create_distplot([data], ["Reading Time"], show_hist=False)
# fig.show()
populationMean = st.mean(data)
print("Population Mean is", populationMean)


def randomSetOfMean(counter):
    dataset = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean


def showFig(meanList):
    df = meanList
    mean = st.mean(df)
    fig = ff.create_distplot([df], ["Reading Time"], show_hist=False)
    fig.show()


def setup():
    meanList = []
    for i in range(0, 100):
        setOfMean = randomSetOfMean(30)
        meanList.append(setOfMean)
    showFig(meanList)
    mean = st.mean(meanList)
    print("Sampling Mean is", mean)


setup()
