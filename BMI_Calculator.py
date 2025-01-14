import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import pandas as pd

# data storage
bmi_data = []

# calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# classify BMI
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Add data
def add_data():
    try:
        age = int(age_entry.get())
        gender = gender_entry.get()
        activity = activity_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0 or age <= 0:
            messagebox.showerror("Input Error", "Age, Weight, and Height must be positive numbers.")
            return

        # Calculate BMI and classify
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        # Append to data
        bmi_data.append({
            "Age": age,
            "Gender": gender,
            "Activity Level": activity,
            "Weight (kg)": weight,
            "Height (m)": height,
            "BMI": round(bmi, 2),
            "Category": category
        })

        # Clear input fields
        clear_inputs()

        # Update treeview
        update_treeview()

        messagebox.showinfo("Success", "Record added successfully!")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid data.")

# clear input fields
def clear_inputs():
    age_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    activity_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

# update treeview
def update_treeview():
    for row in tree.get_children():
        tree.delete(row)
    for idx, record in enumerate(bmi_data):
        tree.insert("", tk.END, values=(idx + 1, record["Age"], record["Gender"], record["Activity Level"],
                                        record["Weight (kg)"], record["Height (m)"], record["BMI"], record["Category"]))

# visualize BMI trends
def visualize_bmi_trends():
    if not bmi_data:
        messagebox.showerror("No Data", "No data available to visualize.")
        return

    df = pd.DataFrame(bmi_data)
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["BMI"], marker="o", label="BMI")
    plt.axhline(y=18.5, color="blue", linestyle="--", label="Underweight (18.5)")
    plt.axhline(y=24.9, color="green", linestyle="--", label="Normal weight (24.9)")
    plt.axhline(y=29.9, color="orange", linestyle="--", label="Overweight (29.9)")
    plt.title("BMI Trends")
    plt.xlabel("Record Number")
    plt.ylabel("BMI")
    plt.legend()
    plt.grid(True)
    plt.show()

# Create main Tkinter window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("800x600")

# Input Fields
tk.Label(root, text="Age:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Gender:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
gender_entry = tk.Entry(root)
gender_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Activity Level:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
activity_entry = tk.Entry(root)
activity_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Weight (kg):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
weight_entry = tk.Entry(root)
weight_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Height (m):").grid(row=4, column=0, padx=10, pady=5, sticky="e")
height_entry = tk.Entry(root)
height_entry.grid(row=4, column=1, padx=10, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Data", command=add_data)
add_button.grid(row=5, column=0, columnspan=2, pady=10)

visualize_button = tk.Button(root, text="Visualize Trends", command=visualize_bmi_trends)
visualize_button.grid(row=6, column=0, columnspan=2, pady=10)

# Treeview for displaying data
columns = ("#", "Age", "Gender", "Activity Level", "Weight (kg)", "Height (m)", "BMI", "Category")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.grid(row=7, column=0, columnspan=2, pady=10)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Start Tkinter loop
root.mainloop()