import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load training data from Excel files
X_df = pd.read_excel("X_data.xlsx")  # Input variables
Y_df = pd.read_excel("Y_data.xlsx")  # ROM output variables

# Convert to numpy arrays
X_data = X_df.to_numpy()  # Shape: (num_samples, 5 features)
Y_data = Y_df.to_numpy()  # Shape: (num_samples, 3 output features)

# Convert data into sequences for LSTM training
def create_sequences(data, labels, seq_length=3):
    X, Y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])  # Take previous 3 time steps
        Y.append(labels[i+seq_length])  # Predict the next ROM
    return np.array(X), np.array(Y)

seq_length = 3  # Using past 3 steps to predict the next
X_train, Y_train = create_sequences(X_data, Y_data, seq_length)

# Reshape X_train for LSTM: (samples, timesteps, features)
X_train = X_train.reshape(X_train.shape[0], seq_length, X_train.shape[2])

# Define LSTM Model
model = Sequential([
    LSTM(50, activation='relu', return_sequences=True, input_shape=(seq_length, 5)),
    LSTM(50, activation='relu'),
    Dense(3)  # Predicting Hip, Knee, Ankle ROM
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, Y_train, epochs=100, verbose=0)

# Real-Time Visualization
def plot_results(hip_rom, knee_rom, ankle_rom):
    plt.clf()  # Clear the previous plot
    labels = ['Hip ROM', 'Knee ROM', 'Ankle ROM']
    values = [hip_rom, knee_rom, ankle_rom]

    plt.bar(labels, values, color=['blue', 'red', 'green'])
    plt.ylim(1, 10)  # Adjust y-axis range (1-10 degrees)
    plt.ylabel("ROM (degrees)")
    plt.title("Predicted Range of Motion (ROM)")
    plt.pause(0.5)  # Pause for visualization update

# Accept user input
def get_user_input():
    try:
        height = float(input("Enter Subject Height (cm): "))
        speed = float(input("Enter Subject Speed (m/s): "))
        knee_length = float(input("Enter Subject Knee Length (cm): "))
        tread = float(input("Enter Staircase Tread Length (cm): "))
        riser = float(input("Enter Staircase Riser Height (cm): "))
        return [height, speed, knee_length, tread, riser]
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return get_user_input()

# Run real-time prediction
plt.ion()  # Enable interactive mode
while True:
    user_input = np.array(get_user_input()).reshape(1, 1, 5)  # Reshape for LSTM
    predicted_rom = model.predict(user_input)

    print(f"\nPredicted ROM: Hip: {predicted_rom[0][0]:.2f}, Knee: {predicted_rom[0][1]:.2f}, Ankle: {predicted_rom[0][2]:.2f}")

    # Update real-time visualization
    plot_results(predicted_rom[0][0], predicted_rom[0][1], predicted_rom[0][2])

plt.ioff()  # Disable interactive mode after exiting loop
plt.show()
