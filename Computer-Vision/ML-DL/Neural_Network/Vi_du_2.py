import numpy as np

# Định nghĩa vector đầu vào, vector trọng số và bias

input_vector = np.array([2, 1.5])
weights_vector = np.array([1.45, -0.66])
bias = np.array([0.0])

# Định nghĩa hàm kích hoạt là hàm sigmoid
def sigmoid(x):
   return 1 / (1 + np.exp(-x))

# Định nghĩa hàm dự đoán
def make_prediction(input_vector, weights_vector, bias):
   Multi_X_and_W = np.dot(input_vector, weights_vector) + bias
   output = sigmoid(Multi_X_and_W)
   return output

prediction = make_prediction(input_vector, weights_vector, bias)
print("Kết quả dự đoán:",prediction)

actual = 0
MSE = np.square(prediction - actual)
print("Giá trị hàm loss - Độ sai khác:", MSE)