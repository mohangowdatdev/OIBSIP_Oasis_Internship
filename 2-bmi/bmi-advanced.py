import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("400x300")
        self.bmi_history_window = None
        self.bmi_trends_window = None

        # Variables for user input
        self.weight_var = tk.DoubleVar()
        self.height_var = tk.DoubleVar()

        # Entry fields for weight and height
        tk.Label(root, text="Weight (kg):").pack()
        tk.Entry(root, textvariable=self.weight_var).pack()

        tk.Label(root, text="Height (m):").pack()
        tk.Entry(root, textvariable=self.height_var).pack()

        # Button to calculate BMI
        tk.Button(root, text="Calculate BMI", command=self.calculate_bmi).pack()

        # Result display area
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        # Buttons for additional features
        tk.Button(root, text="View BMI History", command=self.view_bmi_history).pack()
        tk.Button(
            root, text="Analyze BMI Trends", command=self.analyze_bmi_trends
        ).pack()
        # Schedule periodic update for BMI history
        self.root.after(5000, self.update_bmi_history)

    def calculate_bmi(self):
        weight = self.weight_var.get()
        height = self.height_var.get()

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Please enter valid weight and height.")
            return

        # Calculate BMI
        bmi = weight / (height**2)

        # Get BMI category
        bmi_category = self.get_bmi_category(bmi)

        # Display result
        result_text = f"BMI: {bmi:.2f} - Category: {bmi_category}"
        self.result_label.config(text=result_text)

        # Save data to CSV
        self.save_to_csv(weight, height, bmi)

    def get_bmi_category(self, bmi):
        # Implement your existing BMI category logic here
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def save_to_csv(self, weight, height, bmi):
        # Save user data to CSV
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = [timestamp, weight, height, bmi]

        with open("bmi_history.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)

    def view_bmi_history(self):
        if (
            self.bmi_history_window is None
            or not self.bmi_history_window.winfo_exists()
        ):
            # Create a new window for BMI history
            self.bmi_history_window = tk.Toplevel(self.root)
            self.bmi_history_window.title("BMI History")

            # Create a treeview to display the BMI history
            tree = ttk.Treeview(
                self.bmi_history_window,
                columns=("Timestamp", "Weight", "Height", "BMI"),
                show="headings",
            )
            tree.heading("Timestamp", text="Timestamp")
            tree.heading("Weight", text="Weight (kg)")
            tree.heading("Height", text="Height (m)")
            tree.heading("BMI", text="BMI")

            # Read BMI data from CSV and populate the treeview
            with open("bmi_history.csv", mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    tree.insert("", "end", values=row)

            tree.pack(expand=True, fill=tk.BOTH)
        else:
            # If the window is already open, bring it to the front
            self.bmi_history_window.lift()

    def update_bmi_history(self):
        if self.bmi_history_window and self.bmi_history_window.winfo_exists():
            # Update the BMI history table
            tree = self.bmi_history_window.children["!treeview"]
            tree.delete(*tree.get_children())

            # Read BMI data from CSV and populate the treeview
            with open("bmi_history.csv", mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    tree.insert("", "end", values=row)

        # Schedule the next update
        self.root.after(5000, self.update_bmi_history)

    def analyze_bmi_trends(self):
        # Read BMI data from CSV
        timestamps, weights, heights, bmis = [], [], [], []
        with open("bmi_history.csv", mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                timestamps.append(row[0])
                weights.append(float(row[1]))
                heights.append(float(row[2]))
                bmis.append(float(row[3]))

        if not timestamps:
            messagebox.showinfo("Info", "No BMI data available for analysis.")
            return

        # Create a new window for BMI trends analysis
        trends_window = tk.Toplevel(self.root)
        trends_window.title("BMI Trends Analysis")

        # Plot BMI trends
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(timestamps, bmis, marker="o", linestyle="-", color="b")
        ax.set_xlabel("Timestamp")
        ax.set_ylabel("BMI")
        ax.set_title("BMI Trends Over Time")

        # Embed the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=trends_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(expand=True, fill=tk.BOTH)


root = tk.Tk()
app = BMIApp(root)
root.mainloop()
