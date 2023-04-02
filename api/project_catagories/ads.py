from api.project_catagories.utils import target_audience, tone_of_voice, formality, input_language, output_language, \
    variation


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


ADS = {
    "captive_facebook_ad_headlines": MyQuery(
        purpose="as facebook ad headline generator",
        expected_out_come="generate attention-grabbing headlines for Facebook ads that entice prospects to click and "
                          "ultimately make a purchase",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product description", "product_description", ""),
            ("Keywords", "keywords", ""),
            ("Number of headlines", "no_of_headlines", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "primary_text_for_facebook_ads": MyQuery(
        purpose="facebook ad primary text generator",
        expected_out_come="compose high-converting copy for the primary text section for Facebook ads",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product description", "product_description", ""),
            ("Keywords", "keywords", ""),
            ("number of primary text", "no_of_primary_text", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "google_ad_description": MyQuery(
        purpose="as Google ad descriptions generator",
        expected_out_come="generate high-converting descriptions for your Google ads",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product description", "product_description", ""),
            ("keywords", "keywords", ""),
            ("number of descriptions", "no_of_descriptions", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "google_ad_headlines": MyQuery(
        purpose="Google ad headline generator",
        expected_out_come="generate igh-converting headlines for your Google ads",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product description", "product_description", ""),
            ("keywords", "keywords", ""),
            ("number of headlines", "no_of_headlines", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "aida_method": MyQuery(
        purpose="as AIDA method expert",
        expected_out_come="utilize  the world's oldest marketing framework: Attention, Interest, Desire, Action to "
                          "create a marketing copy concepts",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product description", "product_description", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "pas_method": MyQuery(
        purpose="as PAS method expert",
        expected_out_come="utilize Problem-Agitate-Solution as a useful framework to create a marketing copy concepts",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product description", "product_description", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]

    ).get_query_str_fields()
}
