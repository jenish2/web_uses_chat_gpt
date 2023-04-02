class CommonField:
    def __init__(self, label, slug, default_val) -> None:
        self.label = label
        self.slug = slug
        self.default_val = default_val


tone_of_voice = CommonField("Tone of voice", "tone_of_voice", "")

target_audience = CommonField("Target Audience", "target_audience", "")

formality = CommonField("Formality", "formality", "")

input_language = CommonField("Input Language", "input_language", "english")

output_language = CommonField("Output Language", "output_language", "english")

variation = CommonField("Variations", "variations", "")
