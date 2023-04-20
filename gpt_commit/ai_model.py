from typing import List
from transformers import GPT2Tokenizer
from langchain import PromptTemplate, OpenAI, LLMChain

class AIModel:
    def __init__(self) -> None:
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    def count_tokens(self, example_string: str) -> int:
        tokens = self.tokenizer.tokenize(example_string)
        return len(tokens)

    def generate_message(self, diff: str) -> str:
        template = """
        Instruction:
        Generate 1 appropriate commit messages using the following diff.
        The output commit message must be composed of a single line.
        Additionally, the commit messages must be in the following format.
        output language: Japanese

        Diff:
        {diff}

        Output:
        """
        prompt = PromptTemplate(template=template, input_variables=["diff"])
        llm_chain = LLMChain(
            llm=OpenAI(temperature=0), 
            prompt=prompt, 
        )

        # gpt3 has a limit of 4,096 tokens per request
        if self.count_tokens(diff) > 4000:
            raise Exception("The diff is too long.")
        
        message = llm_chain.predict(diff=diff)
        return message

def generate_commit_message(diff: str) -> str:
    ai_model = AIModel()
    try:
        commit_message = ai_model.generate_message(diff)
    except Exception as e:
        raise e
    return commit_message

def handle_ai_exception(e: Exception) -> str:
    error_message = f"An error occurred while generating commit messages: {str(e)}"
    return error_message
