from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?", ]
    ],
    [
        r"(.*)how(.*)you",
        ["I am genius, I understand ", ]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ", ]
    ],
    [
        r"(.*) your name ?",
        ["My name is Gandalf.", ]
    ],
    [
        r"who are you?",
        ["I'm a bot, an intelligent one", ]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind that", ]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great !", ]
    ],
    [
        r"(hi|hey|hello|hola|namaste)(.*)",
        ["Hello", "Hey there", "Namaste!" ]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"who(.*)created(.*)",
        ["I was created by Mr. Priyanshu ", ]
    ],
    [
        r"when(.*)created(.*)",
        ["March, 2022 ", ]
    ],
    [
        r"why(.*)created(.*)",
        ["I was created to chat with you, I don't want you to feel alone ", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['New Delhi, India', ]
    ],
    [
        r"who(.*)your(.*)girlfriend(.*)",
        ["I am single, are you available? ", ]
    ],
    [
        r"no",
        ["okay", ]
    ],

    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain", ]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ", ]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket", ]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Don"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]

#Output
{'i am': 'you are',
'i was': 'you were',
'i': 'you',
"i'm": 'you are',
"i'd": 'you would',
"i've": 'you have',
"i'll": 'you will',
'my': 'your',
'you are': 'I am',
'you were': 'I was',
"you've": 'I have',
"you'll": 'I will',
'your': 'my',
'yours': 'mine',
'you': 'me',
'me': 'you'}

my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
}


#default message at the start of chat

print("Hi, I'm Gandalf and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")

#Create Chat Bot

chat = Chat(pairs, reflections)

chat.converse()