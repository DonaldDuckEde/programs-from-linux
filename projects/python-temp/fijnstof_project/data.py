import pandas as pd
import matplotlib.pyplot as plt
import shutil

def fileCopie():
    shutil.copyfile('./data/main.csv', './data/data.csv')

def changeData():
    df = pd.read_csv('./data/data.csv')

    df['Time'] = df['Time'].str.split().str[1]

    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')

    df['Time'] = df['Time'].dt.round('10min')

    df.to_csv('data.csv', index=False)

    df = pd.read_csv('./data/data.csv')

    df.iloc[:, 0] = df.iloc[:, 0].apply(lambda x: x.split()[-1])

    df.to_csv('./data/data.csv', index=False)

def getId():
    try:
        print("loading data...")
    except:
        print("Something went terribly wrong")

def main():
    fileCopie()
    getId()
    changeData()
    
    user_input = input("Enter an ID: ")
    
    data = pd.read_csv('./data/data.csv')
    
    filtered_data = data[data['id'] == user_input]

    plt.plot(filtered_data['Time'], filtered_data['pm1'], label='pm 1')
    plt.plot(filtered_data['Time'], filtered_data['pm2.5'], label='pm 2.5')
    plt.plot(filtered_data['Time'], filtered_data['pm4'], label='pm 4')
    plt.plot(filtered_data['Time'], filtered_data['pm10'], label='pm 10')

    plt.xlabel('Time')
    plt.ylabel('Amount')
    plt.legend()

    plt.show()

main()