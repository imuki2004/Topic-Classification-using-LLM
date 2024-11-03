# Project Write-Up: Text Classification System

## Approach

In this project, I developed a simple AI-powered text analysis system that classifies input text based on its topic using the `mistralai/Mixtral-8x7B-Instruct-v0.1` model from `Together AI` implemented through `LangChain` and the `ChatTogether model`. The primary goal was to create a command-line interface (CLI) that allows users to input text and receive structured tagging information, specifically the topic of the text.

### Algorithm and Model

I chose the **Mixtral model** (specifically `mistralai/Mixtral-8x7B-Instruct-v0.1`) for this task due to its capabilities in natural language understanding and generation. The primary reasons for selecting this model include:

- **Large Context Window**: The Mixtral model has a relatively `large context window size` of `32k tokens`, allowing it to process larger input texts effectively. This feature is particularly beneficial for applications that require understanding of extensive content. I could considered developing `chunking strategies` for even larger texts, but the model is enough to support paragraph classification.

- **Support for Essential Functions**: The model supports various needed functions, including `structured output`, `tool calling`, and `JSON mode`. This versatility enables us to implement a wide range of functionalities within our classification system.

- **Cost-Effectiveness**: `mistralai/Mixtral-8x7B-Instruct-v0.1` offers relatively cheaper pricing compared to other models available on Together AI, with a cost of $0.18 per 1 million tokens. This affordability makes it an attractive option for projects with budget constraints.

- **Seamless Integration with LangChain**: The Mixtral model can be easily integrated with the `LangChain framework` through the `ChatTogether model`. This integration simplifies the development process and allows for rapid deployment of the classification system.

The tagging process involves a prompt that instructs the model to classify the input text and return the results in a structured output format. The output is then returned containing the relevant classification information.


## Potential Improvements and Extensions

While the current system functions effectively, there are several potential improvements and extensions that could enhance its performance and usability:

1. **Input Processing**: Implementing preprocessing steps to clean and normalize input text could lead to better classification results. Techniques such as `removing stop words`, `stemming`, or `lemmatization` could be applied.

2. **Multi-Topic Support**: Expanding the system to classify multiple topics within a single text input would increase its usability. This could involve `training the model` to recognize overlapping topics or doing simple `few-shot prompting`.


## Evaluation of the System

To evaluate the performance of the tagging system, there are few points I would make:

1. **Accuracy Metrics**: We could `measure the accuracy` of the model's classifications against a `labeled dataset`. Metrics such as `precision`, `recall`, and `F1-score` would provide insights into the model's performance in identifying topics correctly.

2. **User Studies**: Conducting `user studies` to gather qualitative feedback on the system's usability and the relevance of the tagging results would be valuable. This could involve `surveys` or `interviews` with users to understand their experiences and gather suggestions for improvement.

