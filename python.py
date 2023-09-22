import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını oku
df = pd.read_csv('veriler.csv')

# Verileri grafik olarak göster
plt.plot(df['x'], df['y'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Veriler')
plt.show()
