from .utils import target_audience, tone_of_voice, formality, CommonField, input_language, output_language


class MyQuery:
    query = """I want you to serve as {purpose},
                I will give you the {fields_name}
                and you will give me an output of {expected_out_come}.
                Fields: {fields}"""

    def __init__(self, purpose, expected_out_come, list_of_fileds) -> None:
        self.list_of_fileds = list_of_fileds
        self.purpose = purpose
        self.expected_out_come = expected_out_come

    def __get_fields(self, list_of_fileds):
        my_str = ""
        for (label, slug, _) in list_of_fileds:
            my_str += f" {label} : {{{slug}}} "
        return my_str

    def __get_name_default_val(self, list_of_fileds):

        my_list = []

        for (_, slug, default_val) in list_of_fileds:
            my_list.append({
                "name": slug,
                "default_value": default_val
            })

        return my_list

    def __get_fields_name(self, list_of_fileds):
        my_str = ""
        for (label, _, _) in list_of_fileds:
            my_str += f" {label}, "
        return my_str

    def get_query_str_fields(self):
        return {
            "query_string": self.query.format_map({
                "purpose": self.purpose,
                "fields_name": self.__get_fields_name(self.list_of_fileds),
                "expected_out_come": self.expected_out_come,
                "fields": self.__get_fields(self.list_of_fileds)
            }),
            "fields": self.__get_name_default_val(self.list_of_fileds)
        }


QUIZZES_PROJECTS = {
    "quiz_title": MyQuery(
        purpose="quiz title generator",
        expected_out_come="compelling quiz titles.",
        list_of_fileds=[
            ("Product description", "product_description", ""),
            ("Quiz type", "quiz_type", ""),
            (target_audience.label, target_audience.slug, target_audience.default_val),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            ("Number of quiz titles", "no_of_titles", ""),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val)
        ]
    ).get_query_str_fields(),

    "quiz_description": MyQuery(
        purpose="quiz description generator",
        expected_out_come="compelling descriptions",
        list_of_fileds=[
            ("Product description", "product_description", ""),
            ("Quiz Title", "quiz_title", ""),
            ("Quiz type", "quiz_type", ""),
            ("Call to action", "call_to_action", ""),
            (target_audience.label, target_audience.slug, target_audience.default_val),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            ("Number of descriptions", "no_of_descriptions", ""),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val)
        ]
    ).get_query_str_fields(),

    "engaging_quiz_results": MyQuery(
        purpose="quiz results generator",
        expected_out_come="engadging quiz results.",
        list_of_fileds=[
            ("Quiz Title", "quiz_title", ""),
            ("Product description", "product_description", ""),
            ("Quiz type", "quiz_type", ""),
            ("Call to action", "call_to_action", ""),
            (target_audience.label, target_audience.slug, target_audience.default_val),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            ("Number of quiz titles", "no_of_titles", ""),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val)
        ]
    ).get_query_str_fields(),

    "question_answer_for_quiz": MyQuery(
        purpose="quiz generator",
        expected_out_come="complete quiz questions with answers",
        list_of_fileds=[
            ("Quiz Title", "quiz_title", ""),
            ("Product description", "product_description", ""),
            ("Quiz type", "quiz_type", ""),
            ("Answer type", "answer_type", ""),
            (target_audience.label, target_audience.slug, target_audience.default_val),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            ("Number of quiz questions", "no_of_questions", ""),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val)
        ]
    ).get_query_str_fields(),

    "scored_question_answer_for_quiz": MyQuery(
        purpose="quiz generator",
        expected_out_come="complete quiz with questions, answers results and the mapping",
        list_of_fileds=[
            ("Quiz Title", "quiz_title", ""),
            ("Product description", "product_description", ""),
            ("Quiz type", "quiz_type", ""),
            ("Answer type", "answer_type", ""),
            (target_audience.label, target_audience.slug, target_audience.default_val),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            ("Number of quiz questions", "no_of_questions", ""),
            ("Number of quiz results", "no_of_results", ""),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val)
        ]
    ).get_query_str_fields()
}
