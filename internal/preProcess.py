import utils as ut
from knowledge import GetEvidence


def initDataset(dataset_path):
    dataset = ut.Dataset(dataset_path)
    return dataset


def Preprocessing(data, model):
    outputData = {}
    trueAnswer = data["answer"]
    rawQuestion = data["question"]
    question = ut.getPromptQuestion(rawQuestion)
    newQuestion = ut.getPromptAnswer(model, question)
    subQuestionList = ut.Split2SubQuestion(newQuestion)

    outputData["question"] = rawQuestion
    outputData["answer"] = trueAnswer
    outputData["subQuestions"] = subQuestionList

    subAnswerList = ut.Split2SubAnswer(newQuestion)
    answerWithEvidenceList = GetEvidence(subAnswerList)
    outputData["subAnswer"] = answerWithEvidenceList
    return outputData
