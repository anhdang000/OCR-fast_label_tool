# OCR Fast Label Tool

## 1. Dependencies
- PyQt5
- Python 3.

## 2. Usage
Run the following command:

`python3 label_imags.py`

When submiting, the tool records all labeled words from the first to the current row. Dupicated submissions do not change the output logs.

To resume previous work, run the following command:

`python3 label_imags.py --curr-row [current working row]`
