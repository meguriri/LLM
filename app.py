import utils as ut


if __name__ == "__main__":
    dataset_path = "datasets/simplified_data.json"
    model = "gpt-3.5-turbo"

    dataset = ut.Dataset(dataset_path)
    datas = dataset.getDataset()
    output = []
    for i in range(5):
        outputData = {}
        data = datas[i]
        trueAnswer = data["answer"]
        rawQuestion = data["question"]
        question = ut.getPromptQuestion(rawQuestion)
        newQuestion = ut.getPromptAnswer(model, question)
        subQuestionList = ut.Split2SubQuestion(newQuestion)
        print(subQuestionList, end='\n\n')

