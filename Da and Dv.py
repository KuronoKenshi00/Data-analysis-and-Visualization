import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

def get_screen_resolution():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

def plot_histogram(column_name, screen_width, screen_height):
    plt.figure(figsize=(screen_width / 100, screen_height / 100), dpi=100)
    plt.hist(data[column_name], bins=10, color='skyblue', edgecolor='black')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {column_name}')
    plt.xticks(rotation=45)
    plt.show()

data = pd.read_csv('Students_data.csv')
screen_width, screen_height = get_screen_resolution()

while True:
    print("Select a histogram to display:")
    for i, column in enumerate(data.columns[2:]):
        print(f"{i+1}. {column}")

    choice = int(input("Enter the number of the histogram to display (0 to exit): "))
    if choice == 0:
        break
    elif 1 <= choice <= len(data.columns[2:]):
        column_name = data.columns[choice + 1]
        plot_histogram(column_name, screen_width, screen_height)
    else:
        print("Invalid choice. Please enter a number between 1 and", len(data.columns[2:]))
