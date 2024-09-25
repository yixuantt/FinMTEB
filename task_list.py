

TASK_LIST_CLASSIFICATION = [
    "FinancialPhraseBankClassification",
    "FinSentClassification",
    "FiQAClassification",
    "SemEva2017Classification",
    "FLSClassification",
    "ESGClassification",
    "FOMCClassification",
    "FinancialFraudClassification",

    # "FinNSPClassification",
    # "FinChinaSentimentClassification",
    # "FinFEClassification",
    # "OpenFinDataSentimentClassification",
    # "Weibo21Classification"
]
TASK_LIST_RETRIEVAL = [
    "FiQA2018Retrieval",
    "FinanceBenchRetrieval",
    "HC3Retrieval",
    "Apple10KRetrieval",
    "FinQARetrieval",
    "TATQARetrieval",
    "USNewsRetrieval",
    "TradeTheEventEncyclopediaRetrieval",
    "TradeTheEventNewsRetrieval",
    "TheGoldmanEnRetrieval",

    # "FinTruthQARetrieval",
    # "FinEvaRetrieval",
    # "AlphaFinRetrieval",
    # "DISCFinLLMRetrieval",
    # "DISCFinLLMComputingRetrieval",
    # "DuEEFinRetrieval",
    # "SmoothNLPRetrieval",
    # "THUCNewsRetrieval",
    # "FinEvaEncyclopediaRetrieval",
    # "TheGoldmanZhRetrieval"

]

TASK_LIST_CLUSTERING = [
    "MInDS14EnClustering",
    "ComplaintsClustering",
    "PiiClustering",
    "FinanceArxivS2SClustering",
    "FinanceArxivP2PClustering",
    "WikiCompany2IndustryClustering",

    "MInDS14ZhClustering",
    "FinNLClustering",
    "CCKS2022Clustering",
    "CCKS2020Clustering",
    "CCKS2019Clustering"

]

TASK_LIST_RERANKING = [
    "FinFactReranking",
    "FiQA2018Reranking",
    "HC3Reranking",

    "FinEvaReranking",
    "DISCFinLLMReranking"
]
TASK_LIST_STS = [
    "FINAL",
    "FinSTS",
    
    "AFQMC",
    "BQCorpus"
]

TASK_LIST_SUM = [
    "Ectsum",
    "FINDsum",
    "FNS2022sum",

    "FiNNAsum",
    "FinEvaHeadlinesum",
    "FinEvasum"
]
TASK_LIST_PAIRCLASSIFICATION = [
    "HeadlineACPairClassification",
    "HeadlinePDDPairClassification",
    "HeadlinePDUPairClassification",
    "AFQMCPairClassification"
]

RUNNING_TASK = (
    TASK_LIST_STS
    + TASK_LIST_RETRIEVAL
    + TASK_LIST_CLUSTERING
    + TASK_LIST_PAIRCLASSIFICATION
    + TASK_LIST_SUM
    + TASK_LIST_CLASSIFICATION
    + TASK_LIST_RERANKING
)
