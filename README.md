# Automated Document Summarizer

This project is an advanced Python-based document summarization tool that automatically generates concise summaries from long documents or articles. It utilizes natural language processing (NLP) techniques and machine learning algorithms to extract key information and produce high-quality summaries.

## Features

- **Automatic Summarization**: Generates summaries automatically from long documents or articles.
- **NLP Techniques**: Utilizes natural language processing techniques such as tokenization, sentence segmentation, and part-of-speech tagging.
- **Machine Learning Algorithms**: Implements machine learning algorithms for text summarization, such as TF-IDF (Term Frequency-Inverse Document Frequency) and TextRank.
- **Customizable Summary Length**: Allows customization of summary length to control the level of detail.
- **Multilingual Support**: Supports multiple languages for document summarization.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/anesu398/automated-document-summarizer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd automated-document-summarizer
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your document or article for summarization (e.g., save it in a text file).

2. Run the script:

    ```bash
    python summarize_document.py --input_file document.txt --output_file summary.txt --length 3
    ```

    Replace `document.txt` with the path to your input file, `summary.txt` with the desired output file path for the summary, and `3` with the desired length of the summary (number of sentences).

3. View the generated summary in the specified output file.

## Parameters

- `--input_file`: Path to the input document or article file.
- `--output_file`: Path to save the generated summary.
- `--length`: Length of the summary (number of sentences).

## Example

Suppose we have a lengthy article named `article.txt` that we want to summarize into a concise summary of 5 sentences. We run the following command:

```bash
python app.py --input_file article.txt --output_file summary.txt --length 5
