from internal import initDataset, Preprocessing
import json

dataset_path = "datasets/simplified_data.json"
model = "gpt-3.5-turbo"

if __name__ == "__main__":
    output = []
    dataset = initDataset(dataset_path)
    datas = dataset.getDataset()
    for i in range(5):
        data = datas[i]
        outputData = Preprocessing(data, model)
        output.append(outputData)

    with open("output.json", "w") as f:
        json.dump(output, f)
