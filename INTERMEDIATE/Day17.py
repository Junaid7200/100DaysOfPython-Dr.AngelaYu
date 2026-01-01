# July 1, 2024

# quiz game

# class Users:
    
#     def __init__(self, id, name, age):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.follower = 0
#         self.following = 0
    
#     def follow(self, user):
#         user.follower += 1
#         self.following += 1
#         print (f"{self.name} is now following {user.name}")
        






# user_1 = Users(1, "Junaid", 22)

# user_2 = Users(2, "Jimbo", 21)

# print(user_1.name)
# print(user_2.name)

# user_1.follow(user_2)







question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        
question_bank = []
for x in question_data:
    question = Question(x["text"], x["answer"])
    question_bank.append(question)


class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").capitalize()
        self.check_answer(user_answer)
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    def print_quiz(self):
        while True:
            if self.still_has_questions() == False:
                break
            else:
                self.next_question()
    def check_answer(self, user_answer):
        if self.question_list[self.question_number-1].answer == user_answer:
            print("Good work! you got it right.")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("Sorry, that's wrong.")
            print(f"Your current score is {self.score}/{self.question_number}")





data = [
    {"type":"boolean",
    "difficulty":"easy",
    "category":"Entertainment: Video Games",
    "question":"Valve&#039;s &quot;Portal&quot; and &quot;Half-Life&quot; franchises exist within the same in-game universe.",
    "correct_answer":"True",
    "incorrect_answers":["False"]},
    {"type":"boolean",
    "difficulty":"easy",
    "category":"Entertainment: Video Games",
    "question":"In &quot;Super Mario Bros.&quot;, the clouds and bushes have the same artwork and are just different colors.",
    "correct_answer":"True",
    "incorrect_answers":["False"]},
    {"type":"boolean",
    "difficulty":"easy",
    "category":"Entertainment: Video Games",
    "question":"In &quot;Undertale&quot;, the main character of the game is Sans.",
    "correct_answer":"False",
    "incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"medium","category":"Entertainment: Video Games","question":"During pre-production of &quot;Super Mario Bros.&quot;, Mario originally was meant to shoot bullets.","correct_answer":"True","incorrect_answers":["False"]},
    {"type":"boolean","difficulty":"medium","category":"Entertainment: Video Games","question":"In the Resident Evil series, Leon S. Kennedy is a member of STARS.","correct_answer":"False","incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"Nintendo&#039;s Luigi was originally just called Green Mario?","correct_answer":"False","incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"In Splatoon, the Squid Sisters are named Tako and Yaki.","correct_answer":"False","incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"medium","category":"Entertainment: Video Games","question":"In the game &quot;Subnautica&quot;, a &quot;Cave Crawler&quot; will attack you.","correct_answer":"True","incorrect_answers":["False"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"Solid Snake is actually a clone from the DNA of Big Boss in the Metal Gear Solid series&#039; history.","correct_answer":"True","incorrect_answers":["False"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"The names of Tom Nook&#039;s cousins in the Animal Crossing franchise are named &quot;Timmy&quot; and &quot;Jimmy&quot;.","correct_answer":"False","incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"medium","category":"Entertainment: Video Games","question":"In &quot;Resident Evil&quot;, only Chris has access to the grenade launcher.","correct_answer":"False","incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"Faust is a playable character in &quot;Guilty Gear Xrd Revelator&quot;.","correct_answer":"True","incorrect_answers":["False"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"The shotgun appears in every numbered Resident Evil game.","correct_answer":"True","incorrect_answers":["False"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"The song &quot;Megalovania&quot; by Toby Fox made its third appearence in the 2015 RPG &quot;Undertale&quot;.","correct_answer":"True","incorrect_answers":["False"]},
    {"type":"boolean","difficulty":"medium","category":"Entertainment: Video Games","question":"Super Mario Bros. was released in 1990.","correct_answer":"False","incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"medium","category":"Entertainment: Video Games","question":"The character that would eventually become Dr. Eggman was considered for the role of Sega&#039;s new flagship mascot before Sonic was.","correct_answer":"True","incorrect_answers":["False"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"In &quot;Super Mario 64&quot;, collecting 100 coins on a level will give you a 1-UP.","correct_answer":"False","incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"In Pok&eacute;mon, Bulbasaur is the only starter pokemon that is a Grass\\/Poison type.","correct_answer":"True","incorrect_answers":["False"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"In Kingdom Hearts the Paopu fruit is said to intertwine the destinies for two people forever.","correct_answer":"True","incorrect_answers":["False"]},
    {"type":"boolean","difficulty":"medium","category":"Entertainment: Video Games","question":"The game Garry&#039;s Mod originally took assets and codes from the popular Half Life 2 mod JBmod.","correct_answer":"True","incorrect_answers":["False"]},
    {"type":"boolean","difficulty":"hard","category":"Entertainment: Video Games","question":"The first &quot;Metal Gear&quot; game was released for the PlayStation 1.","correct_answer":"False","incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"The ghosts in &quot;Pac-Man&quot; and &quot;Ms. Pac-Man&quot; have completely different behavior.","correct_answer":"True","incorrect_answers":["False"]},
    {"type":"boolean","difficulty":"medium","category":"Entertainment: Video Games","question":"Shang Tsung is a playable character in Mortal Kombat XL.","correct_answer":"False","incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"In &quot;Sonic Adventure&quot;, you are able to transform into Super Sonic at will after completing the main story.","correct_answer":"False","incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"medium","category":"Entertainment: Video Games","question":"In Rocket League, you can play Basketball.","correct_answer":"True","incorrect_answers":["False"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"Tetris is the #1 best-selling video game of all-time.","correct_answer":"False","incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"Rebecca Chambers does not appear in any Resident Evil except for the original Resident Evil and the Gamecube remake.","correct_answer":"False","incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"In Team Fortress 2, being disguised as a scout or medic results in a speed boost.","correct_answer":"False","incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"medium","category":"Entertainment: Video Games","question":"The first Maxis game to feature the fictional language &quot;Simlish&quot; was The Sims (2000).","correct_answer":"False","incorrect_answers":["True"]},
    {"type":"boolean","difficulty":"easy","category":"Entertainment: Video Games","question":"In &quot;Mario Kart 64&quot;, Waluigi is a playable character.","correct_answer":"False","incorrect_answers":["True"]}
    ]

question_bank2 = []
for x in data:
    question = Question(x["question"], x["correct_answer"])
    question_bank2.append(question)




Quizbrain = QuizBrain(question_bank2)
Quizbrain.print_quiz()