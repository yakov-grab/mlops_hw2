import numpy as np
import os

# Создание папок, если они не существуют
os.makedirs("data", exist_ok=True)
os.makedirs("data/train", exist_ok=True)
os.makedirs("data/test", exist_ok=True)

# Генерация и сохранение данных
def generate_data(save_dir, num_samples=1000):
    data = np.random.rand(num_samples, 2)  # Пример случайных данных
    np.savetxt(os.path.join(save_dir, "data.csv"), data, delimiter=",")

generate_data("data/train")
generate_data("data/test")
