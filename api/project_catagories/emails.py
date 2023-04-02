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


EMAILS = {
    "subject_line": MyQuery(
        purpose="an email subject lines generator",
        expected_out_come="give me email subject lines that grab attention",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("email content", "email_content", ""),
            ("number_of_subject_lines", "number_of_subject_lines", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "effective_cold_email": MyQuery(
        purpose="as a cold email generator",
        expected_out_come="write me an engaging cold email with a subject line and sections where CTAs should be added",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product information", "product_information", ""),
            ("keywords", "keywords", ""),
            ("email type", "email_type", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "persuasive_writing_points": MyQuery(
        purpose="a persuaive writing points generato",
        expected_out_come="generate persuasive writing points for incorporation into landing pages, emails, and more",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product information", "product_information", ""),
            ("number of points", "no_of_points", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "feature_into_benefit": MyQuery(
        purpose="as a business professional",
        expected_out_come="convert the product's features into benefits that drive action",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product description", "product_description", ""),
            ("product features", "product_features", ""),
            ("Number of benefits", "no_of_benefits", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields()
}
