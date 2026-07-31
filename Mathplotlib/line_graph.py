import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [30, 32, 31, 33, 35]

plt.plot(days, temperature, marker="o")

plt.title("Temperature Over Days")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

plt.show()