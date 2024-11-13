import json
from .prompt import SplitPrompt
from .open_ai import CallOpenAI
import re

class Dataset:
    def __init__(self, filePath):
        with open(filePath, "r") as f:
            self.dataset = json.load(f)

    def getDataset(self):
        return self.dataset

    def getQuestion(self):
        return self.dataset['question']

    def getAnswer(self):
        return self.dataset['answer']


def getPromptQuestion(question):
    return SplitPrompt + question


def getPromptAnswer(model, question):
    answer = CallOpenAI(model, question)
    return answer


def Split2SubQuestion(question):
    return re.findall(r"q\d+:\s*(.*?\?)", question)

def Split2SubAnswer(question):
    return re.findall(r"\ba\d+:\s*([^\n]+)", question, )
