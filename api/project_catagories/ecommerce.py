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


ECOMMERCE = {
    "amazon_product_description": MyQuery(
        purpose="an Amazon Product Description generator",
        expected_out_come="generate a paragraph of persuasive product descriptions for Amazon listings that highlight "
                          "key features and benefits ",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("key features/benefits", "key_features", ""),
            ("number of descriptions", "number_of_descriptions", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),

    "amazon_product_features_bullet": MyQuery(
        purpose="an Amazon Product Features generator",
        expected_out_come="compose bullet points that clearly articulate the key features and benefits of the "
                          "product for Amazon listings under the \"About This Item\" section",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product description", "product_description", ""),
            ("key benefit/features", "key_features", ""),
            ("keywords", "keywords", ""),
            ("number of points", "number_of_points", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "one_shot_landing_page": MyQuery(
        purpose="a Landing Page generator",
        expected_out_come="compose and Generate a complete landing page with H1, H2, and H3 headings that effectively "
                          "convey the intended message. It must also include a CTA, social proof, and a list of "
                          "benefits",
        list_of_fileds=[
            ("background information", "background_information", ""),
            ("product description", "product_description", ""),
            ("key benefits", "key_benefits", ""),
            ("keywords", "keywords", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "product_description": MyQuery(
        purpose="a Product Description generator",
        expected_out_come="craft paragraphs of product descriptions that are appealing, engaging, and relevant for "
                          "use on websites, emails, and social media platforms",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("product description", "product_description", ""),
            ("Number of descriptions", "number_of_descriptions", ""),
            (target_audience.label, target_audience.slug, target_audience.default_val),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "seo_product_page": MyQuery(
        purpose="an SEO Product Page generator",
        expected_out_come="develop SEO-optimized title tags and meta descriptions to achieve top Google rankings for "
                          "company services pages",
        list_of_fileds=[
            ("product name", "product_name", ""),
            ("service description", "service_description", ""),
            ("keywords", "keywords", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields()
}
