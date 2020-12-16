#Function to receive message input
def emoji_converter(message):

#emoji symbol list 
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😞",
        ":-D":"😄",
        ":-o":"😳",
        ";-)":"😉",
        ":-s":"🤨",
        "(H)or(h)":"😎",
        "(A)or(a)":"😇",
        ":-#":"🤐",
        "8-|":"🤓",
        ":-*":"🤫",
        ":^)":"🤗",
        "<:o)":"🥳",
        "|-)":"👍",
        "(Y)or(y)":"👍",
        "(B)or(b)":"🙎‍♀️",
        "(X)or(x)":"🙎‍♀️",
        ":-P"or":p":"😛",
        ":-|":"😞",
        ":-$":"☺️",
        ":-@":"😡",
        "(6)":"😈",
        "8o|":"😬",
        "^o)":"🤔",
        "+o(":"🤢",
        "*-)":"",
        "8-)":"🤔",
        "(C)or(c)":"☕️",
        "(N)or(n)":"👎🏾",
        "(D)or(d)":"🙎🏾‍♂️",
        "(Z)or(z)":"🙍🏽‍♂️️",
        "(})":"👫",
        "(^)":"🎂",
        "(U)or(u)":"💔",
        "(G)or(g)":"🎁",
        "(W)or(w)":"🥀",
        "(~)":"🎞",
        "(%)":"🐶",
        "(T)or(t)":"☎️",
        "(8)":"🎵",
        "(O)or(o)":"🕰",
        "(I)or(i)":"💡",
        "(S)or(s)":"🌙",
        "(E)or(e)":"📧",
        "(M)or(m)":"💬"


    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
        return output


message = input(">")
print(emoji_converter(message))
