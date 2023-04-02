import openai


class ChatGpt:

    def __init__(self, api_key, model="text-davinci-003"):
        self.api_key = api_key
        self.model = model

    def get_suggestions(self, query, number_of_responses):
        openai.api_key = self.api_key

        response = openai.Completion.create(
            model=self.model,
            prompt=query,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            n=number_of_responses
        )

        response_list = []
        for text in response["choices"]:
            response_list.append(text["text"].replace("\n"," "))
        return response_list, int(response["usage"]["total_tokens"])
