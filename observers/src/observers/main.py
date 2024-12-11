#!/usr/bin/env python
import sys
import warnings

from observers.crew import Observers

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'scene': {
            'user': {
                'position': '(0,0,0)',
                'target': 'plate',
                'movement': 'Pick',
                'action': 'Use'
            },
            'plate': {
                'position': '(0.5, 0.6, 0.5)',
                'QDC': 'touch',
                'QTC': 'stationary',
                'MOS': 'stationary',
                'HOLD': 'no'
            },
            'glass': {
                'position': '(2, 0.6, 2)',
                'QDC': 'far',
                'QTC': 'stationary',
                'MOS': 'stationary',
                'HOLD': 'no',
            }
        }
    }
    Observers().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Observers().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Observers().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Observers().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
