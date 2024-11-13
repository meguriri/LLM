from .wikidata import wikidata
from .wikipedia import wikipedia

knowledgeSource = {
    "wikipedia": wikipedia,
    "wikidata": wikidata,
}


def GetEvidence(subAnswer):
    answerWithEvidenceList = []
    for answer in subAnswer:
        answerWithEvidence = {}
        answerWithEvidence["answer"] = answer
        answerWithEvidence["evidences"] = []
        for knowName, knowFunc in knowledgeSource.items():
            knowl = {}
            evidence = knowFunc(answer)
            knowl["name"] = knowName
            knowl["evidence"] = evidence
            answerWithEvidence["evidences"].append(knowl)
        answerWithEvidenceList.append(answerWithEvidence)
    return answerWithEvidenceList
