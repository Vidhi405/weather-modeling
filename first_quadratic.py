import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
hours = np.linspace(6, 20, 10)

known_times = np.array([0, 4, 8.55])
known_temps = np.array([20, 32, 22])

coeffs = np.polyfit(known_times, known_temps, 2)
a, b, c = coeffs

y = a * (x**2) + b * x + c

def format_hour(hr):
    hr = int(round(hr))
    if hr == 12:
        return "12 NOON"
    elif hr == 0 or hr == 24:
        return "12 AM"
    elif hr < 12:
        return f"{hr} AM"
    else:
        return f"{hr - 12} PM"

print("Time\tPredicted Temperature (°C)")
for i in range(len(hours)):
    hr = hours[i]
    print(f"{format_hour(hr)}\t\t{y[i]:.2f}")

x_fine = np.linspace(0, 9, 100)
curve = a * x_fine**2 + b * x_fine + c

plt.plot(x_fine, curve, label="Predicted Temperature", color='red')
plt.scatter(known_times, known_temps, color='blue', label="Known Data")

time_labels = [format_hour(hr) for hr in hours]
plt.xticks(ticks=x, labels=time_labels, rotation=45)

plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Prediction Curve (6 AM to 8 PM)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
