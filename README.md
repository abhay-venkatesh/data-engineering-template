# data-engineering-template

A template repository for engineering any dataset.

## Structure

```bash
configs/
    dataset_config.yml
lib/
    agent/
        dataset_agent.py
    builder/
        dataset_builder.py
    analyzer/
        dataset_analyzer.py
main.py
```

## Installation

### Windows

```bash
conda env create -f windows_env.yml
pip install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"
```
