from ask_confluence.model_predictor import ModelPredictor

def get_answer_from_confluence(question):
    return ModelPredictor().get_answer(question)