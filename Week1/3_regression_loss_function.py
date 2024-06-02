import random
import math

def calculate_loss(num_samples, loss_name):
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return
    
    num_samples = int(num_samples)
    if num_samples <= 0:
        print("number of samples must be greater than zero")
        return

    def mae(predict, target):
        return abs(predict - target)
    
    def mse(predict, target):
        return (predict - target) ** 2
    
    def rmse(predict, target):
        return math.sqrt(mse(predict, target))

    loss_functions = {
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse
    }
    
    if loss_name not in loss_functions:
        print(f"{loss_name} is not a valid loss function")
        return

    total_loss = 0
    for sample in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        loss = loss_functions[loss_name](predict, target)
        total_loss += loss
        print(f"loss name: {loss_name}, sample: {sample}, pred: {predict}, target: {target}, loss: {loss}")

    if loss_name == "RMSE":
        total_loss = math.sqrt(total_loss / num_samples)
    else:
        total_loss = total_loss / num_samples

    print(f"final {loss_name}: {total_loss}")

calculate_loss("5", "RMSE")
calculate_loss("aa", "MSE")
calculate_loss("3", "MAE")
