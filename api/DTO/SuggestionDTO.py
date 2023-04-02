class SuggestionDTO:
    def __init__(self, suggestion_dict):
        self.suggestion = suggestion_dict['suggestion']
        self.user_project_id = suggestion_dict['user_project_id']

    def give_basic_dict(self):
        return self.__dict__

    def get_suggestion_dto(self):
        return self.give_basic_dict()

    def get_suggestion_without_project_id(self):
        suggestion = self.give_basic_dict()
        suggestion.pop('user_project_id')
        return suggestion
