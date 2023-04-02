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


VIDEO = {
    "high_impact_mini_vsl": MyQuery(
        purpose="as a High-Impact Mini-VSL generator",
        expected_out_come="craft a compelling 60 seconds video script that piques the interest of your audience and "
                          "drives sales",
        list_of_fileds=[
            ("Your name", "your_name", ""),
            ("Company/Product Name", "product_name", ""),
            ("Who is your ideal buyer audience", "target_audience", ""),
            ("List your key benefits & features", "key_benefits", ""),
            ("What current pain or negative circumstance is your customer-facing now", "biggest_customer_issues", ""),
            ("What's a true negative or scary fact", "negative_fact", ""),
            ("What's the big idea in 2-3 words? What hook makes your product different", "big_idea", ""),
            ("What is your niche? A more narrow focus of your audience", "your_niche", ""),
            ("What are customers' initial goal", "customers_initial_goal", ""),
            ("What are customers' ultimate goal that results from the initial goal", "customers_ultimate_goal", ""),
            ("What is your product's price", "products_price", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val)
        ]

    ).get_query_str_fields(),
    "tik_tok_video_captions": MyQuery(
        purpose="a TikTok captions generator",
        expected_out_come="generated TikTok captions that are both entertaining and shareable",
        list_of_fileds=[
            ("about the video", "about_video", ""),
            ("keywords", "keywords", ""),
            ("numbers of captions", "no_of_captions", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)

        ]
    ).get_query_str_fields()
    ,
    "you_tube_description":
        MyQuery(
            purpose="a youtube video description generator",
            expected_out_come="crafted Engaging Youtube Descriptions That Drive Search Engine Rankings",
            list_of_fileds=[
                ("title of the video", "video_title", ""),
                ("keywords", "keywords", ""),
                ("numbers of descriptions", "no_of_descriptions", ""),
                (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
                (formality.label, formality.slug, formality.default_val),
                (input_language.label, input_language.slug, input_language.default_val),
                (output_language.label, output_language.slug, output_language.default_val),
                (variation.label, variation.slug, variation.default_val)

            ]
        ).get_query_str_fields(),
    "video_hook": MyQuery(
        purpose="a  video script hook and introduction generator",
        expected_out_come="writen engaging hooks with introductions that grab your viewers' attention and keep them "
                          "invested in your video from start to finish",
        list_of_fileds=[
            ("title of the video", "video_title", ""),
            ("numbers of descriptions", "no_of_hooks", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)

        ]
    ).get_query_str_fields()
    ,
    "video_outline": MyQuery(
        purpose="a  video script outline generator",
        expected_out_come="develop a comprehensive script outline that is perfect for \"Listicle\" and \"How-to\" "
                          "style videos",
        list_of_fileds=[
            ("title of the video", "video_title", ""),
            ("numbers of outlines", "no_of_outlines", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)

        ]
    ).get_query_str_fields(),
    "video_title": MyQuery(
        purpose="a  video title generator",
        expected_out_come="generated Attention-Grabbing Video Titles for Maximum Reach on YouTube",
        list_of_fileds=[
            ("about the video", "video_about", ""),
            ("keywords", "keywords", ""),
            ("numbers of titles", "no_of_titles", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)

        ]
    ).get_query_str_fields()
    ,
    "video_topic_ideas": MyQuery(
        purpose="a  video topic idea generator",
        expected_out_come="generate topic ideas that will captivate your audience and climb the ranks on YouTube.",
        list_of_fileds=[
            ("about the video", "video_about", ""),
            ("keywords", "keywords", ""),
            ("numbers of topics", "no_of_topics", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)

        ]
    ).get_query_str_fields()
}
