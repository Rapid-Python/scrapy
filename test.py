import os
import openai
import pandas as pd


df = pd.read_csv('questions-answer-list.csv', delimiter=';')
df.head()

df.to_json("questions-answer-list.jsonl", orient='records', lines=True)

# create a function to find prime numbers


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

