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


BLOGS = {
    "content_improver": MyQuery(purpose="content improver",
                                expected_out_come="improved the content",
                                list_of_fileds=[
                                    ("content", "content", ""),
                                    (target_audience.label, target_audience.slug, target_audience.default_val),
                                    (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
                                    (formality.label, formality.slug, formality.default_val),
                                    (input_language.label, input_language.slug, input_language.default_val),
                                    (output_language.label, output_language.slug, output_language.default_val),
                                    (variation.label, variation.slug, variation.default_val)
                                ]
                                ).get_query_str_fields(),
    "text_summarizer": MyQuery(purpose="text summarizer",
                               expected_out_come="summarized the content",
                               list_of_fileds=[
                                   ("content", "content", ""),
                                   (target_audience.label, target_audience.slug, target_audience.default_val),
                                   (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
                                   (formality.label, formality.slug, formality.default_val),
                                   (input_language.label, input_language.slug, input_language.default_val),
                                   (output_language.label, output_language.slug, output_language.default_val),
                                   (variation.label, variation.slug, variation.default_val)
                               ]
                               ).get_query_str_fields(),
    "paragraph_generator": MyQuery(purpose="paragraph generator",
                                   expected_out_come="generated the paragraph",
                                   list_of_fileds=[
                                       ("paragraph topic", "paragraph_topic", ""),
                                       ("keywords to include", "keywords", ""),
                                       (target_audience.label, target_audience.slug, target_audience.default_val),
                                       (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
                                       (formality.label, formality.slug, formality.default_val),
                                       (input_language.label, input_language.slug, input_language.default_val),
                                       (output_language.label, output_language.slug, output_language.default_val),
                                       (variation.label, variation.slug, variation.default_val)
                                   ]
                                   ).get_query_str_fields()
    ,
    "seo_titles_meta_description": MyQuery(purpose="an SEO blog posts title and meta description generator",
                                           expected_out_come="SEO blog posts titles and meta descriptions",
                                           list_of_fileds=[
                                               ("product name", "product_name", ""),
                                               ("blog post title", "blog_title", ""),
                                               ("blog post description", "blog_description", ""),
                                               ("keywords", "keywords", ""),
                                               (target_audience.label, target_audience.slug,
                                                target_audience.default_val),
                                               (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
                                               (formality.label, formality.slug, formality.default_val),
                                               (input_language.label, input_language.slug, input_language.default_val),
                                               (output_language.label, output_language.slug,
                                                output_language.default_val),
                                               (variation.label, variation.slug, variation.default_val)
                                           ]
                                           ).get_query_str_fields(),
    "blog_post_intro_paragraph": MyQuery(purpose="posts intro paragraph generator",
                                         expected_out_come="a blog post intro paragraph",
                                         list_of_fileds=[
                                             ("blog post title", "blog_title", ""),
                                             ("keywords", "keywords", ""),
                                             (target_audience.label, target_audience.slug, target_audience.default_val),
                                             (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
                                             (formality.label, formality.slug, formality.default_val),
                                             (input_language.label, input_language.slug, input_language.default_val),
                                             (output_language.label, output_language.slug, output_language.default_val),
                                             (variation.label, variation.slug, variation.default_val)
                                         ]
                                         ).get_query_str_fields(),
    "post_conclusion_paragraph": MyQuery(purpose="blog posts conclusion paragraph generator",
                                         expected_out_come="blog post conclusion paragraph",
                                         list_of_fileds=[
                                             ("blog post title", "blog_title", ""),
                                             ("main points of blog post", "main_points", ""),
                                             ("keywords", "keywords", ""),
                                             (target_audience.label, target_audience.slug, target_audience.default_val),
                                             (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
                                             (formality.label, formality.slug, formality.default_val),
                                             (input_language.label, input_language.slug, input_language.default_val),
                                             (output_language.label, output_language.slug, output_language.default_val),
                                             (variation.label, variation.slug, variation.default_val)
                                         ]
                                         ).get_query_str_fields()
    ,
    "blog_post_outline":
        MyQuery(purpose="blog posts outline generator",
                expected_out_come="outline for the blog post",
                list_of_fileds=[
                    ("blog post title", "blog_title", ""),
                    ("keywords", "keywords", ""),
                    (target_audience.label, target_audience.slug, target_audience.default_val),
                    (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
                    (formality.label, formality.slug, formality.default_val),
                    (input_language.label, input_language.slug, input_language.default_val),
                    (output_language.label, output_language.slug, output_language.default_val),
                    (variation.label, variation.slug, variation.default_val)
                ]
                ).get_query_str_fields(),
    "blog_post_topic_ideas":
        MyQuery(purpose="blog posts topic ideas generator",
                expected_out_come="blog posts topic ideas",
                list_of_fileds=[
                    ("product name", "product_name", ""),
                    ("product Description", "product_description", ""),
                    ("number of topics", "number_of_topics", ""),
                    (target_audience.label, target_audience.slug, target_audience.default_val),
                    (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
                    (formality.label, formality.slug, formality.default_val),
                    (input_language.label, input_language.slug, input_language.default_val),
                    (output_language.label, output_language.slug, output_language.default_val),
                    (variation.label, variation.slug, variation.default_val)
                ]
                ).get_query_str_fields(),
    "faq_generator":
        MyQuery(purpose="a FAQ generator",
                expected_out_come="generated frequently asked questions",
                list_of_fileds=[
                    ("product name", "product_name", ""),
                    ("product Description", "product_description", ""),
                    ("number of questions", "number_of_questions", ""),
                    (target_audience.label, target_audience.slug, target_audience.default_val),
                    (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
                    (formality.label, formality.slug, formality.default_val),
                    (input_language.label, input_language.slug, input_language.default_val),
                    (output_language.label, output_language.slug, output_language.default_val),
                    (variation.label, variation.slug, variation.default_val)
                ]
                ).get_query_str_fields(),
    "listicle": MyQuery(purpose="listicle generator",
                        expected_out_come="a numbered list based on the topic",
                        list_of_fileds=[
                            ("topic", "topic", ""),
                            ("product Description", "product_description", ""),
                            ("number of paragraph", "number_of_paragraph", ""),
                            (target_audience.label, target_audience.slug, target_audience.default_val),
                            (tone_of_voice.label, tone_of_voice.slug, tone_of_voice.default_val),
                            (formality.label, formality.slug, formality.default_val),
                            (input_language.label, input_language.slug, input_language.default_val),
                            (output_language.label, output_language.slug, output_language.default_val),
                            (variation.label, variation.slug, variation.default_val)
                        ]
                        ).get_query_str_fields()
}
