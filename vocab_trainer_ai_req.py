import google.generativeai as genai
import ast

# this programm asks gemini for a vocab dictionary wow

class AIReq():
    def __init__(self, language):
        self.key1 = "AIzaSyBRN5w92gkWuTksJk_uwAz7mwS_3lztYVk"
        self.language = language
        print(self.get_response())

    def get_response(self):
        genai.configure(api_key=self.key1)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"give me a python dictionary with german-{self.language} vocabs (at least 20), but dont give it a name just the values ")
        response_text = response.text[10:]
        response_text = response_text[:-4]
        return ast.literal_eval(response_text)


ai_request = AIReq("french")



