import os.path
import random
import pandas as pd
import PySimpleGUI as sg


def make_win1():
    layout = [
        [sg.Text("How many tendays have passed? ")],
        [sg.Input(key="-INPUT-")],
        [sg.Text(size=(40, 1), key="-OUTPUT-")],
        [
            sg.Button("Ok"),
            sg.Button("View Spreadsheet"),
            sg.Button("Edit Spreadsheet"),
            sg.Button("Quit"),
        ],
    ]
    return sg.Window("Tavern Gold Tracker", layout, finalize=True)


def make_win2():
    data = []
    header_list = []
    df = pd.read_csv("savings.csv", sep=",", engine="python", header=None)
    data = df.values.tolist()
    header_list = df.iloc[0].tolist()
    data = df[1:].values.tolist()
    layout = [
        [
            sg.Table(
                values=data,
                headings=header_list,
                auto_size_columns=False,
                num_rows=min(25, len(data)),
            )
        ]
    ]
    return sg.Window("Table", layout, finalize=True)


def scribe(gold, gain_loss):
    f = open("savings.csv", "a", encoding="utf8")
    f.write(f"{gold}, {gain_loss}\n")
    f.close()


check = os.path.isfile("./savings.csv")

if check:
    savings = pd.read_csv("savings.csv")
    balance = savings.iloc[-1, 0]
else:
    savings = pd.DataFrame({"Balance": ["0"], "Profit": ["0"]})
    savings.to_csv("savings.csv", index=False)
    balance = 0

window1, window2 = make_win1(), None

while True:
    window, event, days = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == "Quit":
        window.close()
        if window == window2:
            window2 = None
        elif window == window1:
            break
    elif event == "Ok":
        for i in range(int(days["-INPUT-"])):
            rollDice = random.randint(1, 100) + 10
            if 1 <= rollDice <= 20:
                savings = pd.read_csv("savings.csv")
                balance = savings.iloc[-1, 0]
                profit = -90
                balance = balance + profit
                scribe(balance, profit)
            elif 21 <= rollDice <= 30:
                savings = pd.read_csv("savings.csv")
                balance = savings.iloc[-1, 0]
                profit = -60
                balance = balance + profit
                scribe(balance, profit)
            elif 31 <= rollDice <= 40:
                savings = pd.read_csv("savings.csv")
                balance = savings.iloc[-1, 0]
                profit = -30
                balance = balance + profit
                scribe(balance, profit)
            elif 41 <= rollDice <= 60:
                savings = pd.read_csv("savings.csv")
                balance = savings.iloc[-1, 0]
                profit = 0
                balance = balance + profit
                scribe(balance, profit)
            elif 61 <= rollDice <= 80:
                savings = pd.read_csv("savings.csv")
                balance = savings.iloc[-1, 0]
                profit = random.randint(1, 6) * 5
                balance = balance + profit
                scribe(balance, profit)
            elif 81 <= rollDice <= 90:
                savings = pd.read_csv("savings.csv")
                balance = savings.iloc[-1, 0]
                profit = random.randint(2, 16) * 5
                balance = balance + profit
                scribe(balance, profit)
            elif 91 <= rollDice <= 110:
                savings = pd.read_csv("savings.csv")
                balance = savings.iloc[-1, 0]
                profit = random.randint(3, 30) * 5
                balance = balance + profit
                scribe(balance, profit)
        window["-OUTPUT-"].update(f"Current Balance: {balance}")
    elif event == "View Spreadsheet":
        make_win2()
    elif event == "Edit Spreadsheet":
        os.system("savings.csv")

window.close()
