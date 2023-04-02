from .utils import target_audience, tone_of_voice, formality, CommonField, input_language, output_language, variation


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


WEBSITE = {
    "improve_sub_headline": MyQuery(
        purpose="as a website sub-headline generator",
        expected_out_come="Craft Engaging and Informative Sub-Headlines (H2) for Your Website and Landing Pages",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product description", "product_description", ""),
            ("headline", "headline", ""),
            ("keywords", "keywords", ""),
            ("numbers of titles", "no_of_titles", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "unique_value_proposition": MyQuery(
        purpose="a unique value proposition generator",
        expected_out_come="Craft a value proposition that clearly conveys the Benefits",
        list_of_fileds=[
            ("product description", "product_description", ""),
            ("numbers of value propositions", "no_of_value_propositions", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields()
    ,
    "persuasive_bullet_points": MyQuery(
        purpose="persuasive bullet points generator",
        expected_out_come="craft impactful bullet points that persuade your audience and drive conversions",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product description", "product_description", ""),
            ("numbers of points", "no_of_points", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "company_profile": MyQuery(
        purpose="company profile generator",
        expected_out_come="craft a lengthy captivating narrative that brings your company's story to life",
        list_of_fileds=[
            ("company name", "company_name", ""),
            ("company information", "company_info", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "perfect_headline": MyQuery(
        purpose="a perfect headline generator",
        expected_out_come="Craft headlines that grab attention, communicate value, and drive results with the "
                          "power of proven copywriting formulas",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product description", "product_description", ""),
            ("numbers of headlines", "no_of_headlines", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields()
}
