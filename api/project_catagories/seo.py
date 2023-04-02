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


SEO = {
    "seo_home_page": MyQuery(
        purpose="an SEO homepage title and meta description generator",
        expected_out_come="give me SEO-friendly title tags and meta descriptions for homepages to achieve high "
                          "rankings on Google",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("Homepage description", "homepage_description", ""),
            ("keywords", "keywords", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val)
        ]
    ).get_query_str_fields(),
    "seo_service_page": MyQuery(
        purpose="an SEO service page title and meta description generator",
        expected_out_come="develop SEO-optimized title tags and meta descriptions to achieve top Google rankings for "
                          "company services pages",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("Service description", "service_description", ""),
            ("keywords", "keywords", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val)
        ]
    ).get_query_str_fields()
}
