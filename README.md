# LSTM_ASCEND
☑️Trains an LSTM model on past subject + staircase parameters and corresponding joint Range of Motion (ROM) values.

☑️Takes new inputs from the user (subject measurements + staircase dimensions).

☑️Predicts the hip, knee, and ankle ROM.

☑️Visualizes the results in real time using a live bar chart.


![26-deg](https://github.com/user-attachments/assets/d5de277a-5c0a-49f2-b4f7-f8d79660ec0b) ![32-deg](https://github.com/user-attachments/assets/495ffd36-1cac-4865-b11d-a3bf9cd5f5aa)  ![38-deg](https://github.com/user-attachments/assets/8814a245-867b-46c4-9bf2-aa63807ed289)





![Untitled video - Made with Clipchamp (1)](https://github.com/user-attachments/assets/50ba781c-3222-45b9-88f6-db517cea39e4) ![Untitled video - Made with Clipchamp](https://github.com/user-attachments/assets/db990fca-e294-48ba-9499-491ebfaef660)


________________________________________________________________________________________________
✅ Uses & Applications


🧠 Use Cases

Biomechanical research

Gait analysis

Rehabilitation assessment

Ergonomic or stair design optimization

Predictive modeling in motion science

🧪 Who Can Use This?

Biomechanists

Physiotherapists

Sports scientists

Engineers working with motion or prosthetics

Researchers using motion capture data

____________________________________________________________________________________________________________________________
📥 Inputs

There are two types of inputs:

1️⃣ Training Inputs (from Excel file X_data.xlsx)
   
Each row is a data sample:

Subject Height (cm)

Subject Speed (m/s)

Knee Length (cm)

Staircase Tread (cm)

Staircase Riser (cm)

2️⃣ User Input for Prediction
   
During execution, the user is prompted to enter:

text

Copy

Edit

Enter Subject Height (cm):

Enter Subject Speed (m/s):

Enter Subject Knee Length (cm):

Enter Staircase Tread Length (cm):

Enter Staircase Riser Height (cm):

📤 Outputs

1️⃣ Predicted Outputs
   
The LSTM model outputs:

Hip ROM (degrees)

Knee ROM (degrees)

Ankle ROM (degrees)

These are predicted based on the input subject + stair features.

2️⃣ Live Visualization
   
The predicted ROMs are shown in a bar chart, with:

Y-axis: Range of Motion (degrees, scaled 1–10)

Bars: Hip ROM, Knee ROM, Ankle ROM







