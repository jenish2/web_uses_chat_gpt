from api.project_catagories.utils import target_audience, tone_of_voice, formality, input_language, output_language


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


OFFERS_PROJECTS = {
    "offer_headline": MyQuery(
        purpose="as a offer headlines generator",
        expected_out_come="give me an output of compelling offers headline",
        list_of_fileds=[
            ("company name", "company_name", ""),
            ("product description", "product_description", ""),
            ("call to action", "call_to_action", ""),
            ("number of offers", "no_of_offers", ""),
            (target_audience.label, target_audience.slug, target_audience.default_val),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
        ]
    ).get_query_str_fields(),
    "engaging_offer_description": MyQuery(
        purpose="as a offer description generator",
        expected_out_come="give me an output of engaging offers description",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product description", "product_description", ""),
            ("call to action", "call_to_action", ""),
            ("number of descriptions", "no_of_descriptions", ""),
            (target_audience.label, target_audience.slug, target_audience.default_val),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
        ]).get_query_str_fields()
}
