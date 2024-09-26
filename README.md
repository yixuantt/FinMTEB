<div align="center">
    <img src="source/main.png" alt="Logo" width="60%" />
</div>

# FinMTEB: Finance Massive Text Embedding Benchmark
Finance Massive Text Embedding Benchmark (FinMTEB), a counterpart to MTEB that consists of financial domain-specific text datasets. In summary, FinMTEB consists of a total of 64 datasets, spanning seven different tasks. The key difference between MTEB and FinMTEB is that all datasets in FinMTEB are finance-domain specific, either previously used in financial NLP research or newly developed by the authors.  

## Usage 
* The basic pipeline is the same with [MTEB](https://github.com/embeddings-benchmark/mteb). 
  
### Install

```
conda create -n finmteb python=3.10
git clone https://github.com/yixuantt/FinMTEB.git
cd FinMTEB
pip install -r requirements.txt
```

### Task selection
FinMTEB offers 7 tasks and 64 datasets, which you can choose according to your needs.

```
import finance_mteb 

tasks = finance_mteb.get_tasks(task_types=["Clustering", "Retrieval","PairClassification","Reranking","STS","Summarization","Classification"]) # All 7 Tasks
```

### Running a Benchmark

```
from finance_mteb import MTEB
task = "FinSTS"
evaluation = MTEB(tasks=[task])
evaluation.run(model, output_folder=f"results/{model_name_or_path.split('/')[-1]}")
```

## Example Usage
* There is an example Python script for your reference:
```
python eval_FinanceMTEB.py --model_name_or_path BAAI/bge-en-icl --pooling_method last
```

## Citation

--------
Thanks to the [MTEB](https://github.com/embeddings-benchmark/mteb) Benchmark.
