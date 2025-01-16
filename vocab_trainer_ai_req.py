import google.generativeai as genai
import ast

# this programm asks gemini for a vocab dictionary wow

class AIReq():
    def __init__(self, language):
        self.key1 = "AIzaSyAHWeLtdZ0vxt8wT-DuHJTyzxF9BRkwhP4"
        self.key_recovery = "AIzaSyAmOteH9Z6BBc93pV5HYAEoIQz5GdwF2NA"
        self.language = language
        print(self.get_response())

    def get_response(self):
        try:
            genai.configure(api_key=self.key1)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(f"Is {self.language} a language except from german? if not reply with Error. If it is give me a python dictionary with german-{self.language} vocabs (at least 20), but dont give it a name just the values")
            print("Key worked")
        except:
            genai.configure(api_key=self.key_recovery)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(f"Is {self.language} a language except from german? if not reply with Error. If it is give me a python dictionary with german-{self.language} vocabs (at least 20), but dont give it a name just the values")
            print("recovery key used")
   
        response_text = response.text[10:]
        response_text = response_text[:-4]
        try:
            self.dic = ast.literal_eval(response_text)
            #print(self.dic)
        except:
            self.dic = {"Error":"Error"}


dictionary = AIReq(str(input("Please type in Language: "))).dic