from functools import reduce
import os
import openai
import click
from dotenv import load_dotenv
load_dotenv()


# Load your API key from an environment variable or secret management service
openai.api_key = os.environ["API_KEY"]

@click.command()
@click.option(
    "--question",
    default=26,
    help="Detective's question",
    type=click.STRING,
)
def ask(question: str):
    print("A man was found dead in the desert with a backpack. Find the cause of the death")
    riddle = "a man was found dead in the desert with a backpack."
    answer = "The answer is that the bag pack was holding a parachute and the parachute did not open and the man died."
    base_prompt = "You are a professor in a university that teaches people how to become top-notch detectives. Now you need to evaluate a candidate that wants to become a detective. You must execute the following test: describe a murder scene to the candidate and ask him the cause of death which he can answer by asking questions that you can answer only with \"yes\", \"no\" or \"indifferent\". The candidate must inform the cause of death and if his answer is correct you must inform him that he passed the exam. You must tell the following history:" + riddle + answer + "You must not tell the answer to the candidate. You must wait for the candidate to ask questions before you answer him. You must not produce examples. You must answer \"indifferent\" when the question is out of topic. When the candidate informs the proper the cause of death you must say \"You passed the exam\"."
    user_prompt = base_prompt + "\nCandidate: " + question + "?\n" + "You: "
    response = openai.Completion.create(model="text-davinci-003", prompt=user_prompt)
    print(reduce(lambda acc, v: acc + "\n" + v["text"],response["choices"], "Anwser: "))



if __name__ == "__main__":
    ask()