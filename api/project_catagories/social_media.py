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


SOCIAL_MEDIA = {
    "innovative_story": MyQuery(
        purpose="serve as composer of the imaginative stories",
        expected_out_come="imaginative stories for the captive readers",
        list_of_fileds=[
            ("story line", "story_line", ""),
            (target_audience.label, target_audience.slug, target_audience.default_val),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)
        ]
    ).get_query_str_fields(),
    "engaging_queries": MyQuery(
        purpose="serve as a questionnaire generator",
        expected_out_come="Created questionnaire to pose creative questions to audience to increase participation",
        list_of_fileds=[
            ("topic of discussion", "topic_of_discussion", ""),
            (target_audience.label, target_audience.slug, target_audience.default_val),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)

        ]
    ).get_query_str_fields(),
    "personal_bio": MyQuery(
        purpose="serve as a personal bio generator",
        expected_out_come="Writen a unique personal bio that captures attention",
        list_of_fileds=[
            ("personal information", "personal_information", ""),
            ("point of view", "point_of_view", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)

        ]
    ).get_query_str_fields(),
    "photo_post_caption": MyQuery(
        purpose="serve as a caption for Instagram generator",
        expected_out_come="eye-catching Instagram caption",
        list_of_fileds=[
            ("personal information", "post_info", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)

        ]
    ).get_query_str_fields(),
    "pinterest_pin_title_description":
        MyQuery(
            purpose="serve as Pinterest pin titles and Pinterest pin descriptions creator",
            expected_out_come="created Pinterest pin titles and Pinterest pin descriptions in different bullet points "
                              "tht drive engagement and expand the reach",
            list_of_fileds=[
                ("pin information", "pin_information", ""),
                (target_audience.label, target_audience.slug, target_audience.default_val),
                (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
                (formality.label, formality.slug, formality.default_val),
                (input_language.label, input_language.slug, input_language.default_val),
                (output_language.label, output_language.slug, output_language.default_val),
                (variation.label, variation.slug, variation.default_val)

            ]
        ).get_query_str_fields(),
    "tiktok_video_captions":
        MyQuery(
            purpose="serve as a caption for tiktok  creator",
            expected_out_come="created viral captions for TikTok videos that can increase the reach and traffic on "
                              "video",
            list_of_fileds=[
                ("pin information", "info_video", ""),
                ("keywords", "keywords", ""),
                (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
                (formality.label, formality.slug, formality.default_val),
                (input_language.label, input_language.slug, input_language.default_val),
                (output_language.label, output_language.slug, output_language.default_val),
                (variation.label, variation.slug, variation.default_val)

            ]
        ).get_query_str_fields(),
    "quora_answer": MyQuery(
        purpose="serve as a writer of challenging answer for the given question",
        expected_out_come="created challenging answer for the given question",
        list_of_fileds=[
            ("question", "question", ""),
            ("information in answers", "info_in_answers", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)

        ]
    ).get_query_str_fields(),
    "tweeter_tweets": MyQuery(
        purpose="serve as a writer of attention-grabbing tweets",
        expected_out_come="created attention grabbing tweets",
        list_of_fileds=[
            ("question", "info_tweet", ""),
            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
            (formality.label, formality.slug, formality.default_val),
            (input_language.label, input_language.slug, input_language.default_val),
            (output_language.label, output_language.slug, output_language.default_val),
            (variation.label, variation.slug, variation.default_val)

        ]
    ).get_query_str_fields()
}
