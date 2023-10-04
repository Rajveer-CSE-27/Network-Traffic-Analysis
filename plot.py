import matplotlib.pyplot as plt

x = ["youtube", "instagram", "codeforces", "hackerrank","iitr", "kotaksecurities", "cricbuzz", "primevideo", "mail.google", "irctc"]
y = [4, 2, 1, 4, 3, 1, 2, 1, 4, 1]
plt.plot(x, y)

plt.xlabel('Websites')
plt.ylabel('Number of Employees')
plt.title('Network traffic analysis')
plt.show()
