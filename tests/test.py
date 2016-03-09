# -*- coding: utf8 -*-
import tracery

test_grammar = {
    'deepHash': ["\\#00FF00", "\\#FF00FF"],
    'deeperHash': ["#deepHash#"],
    'animal': ["bear", "cat", "dog", "fox", "giraffe", "hippopotamus"],
    'mood': ["quiet", "morose", "gleeful", "happy", "bemused", "clever",
        "jovial", "vexatious", "curious", "anxious", "obtuse", "serene",
        "demure"],
    'nonrecursiveStory': ["The #pet# went to the beach."],
    'recursiveStory': [
        "The #pet# opened a book about[pet:#mood# #animal#] #pet.a#. #story#[pet:POP] The #pet# closed the book."],
    'svgColor': ["rgb(120,180,120)", "rgb(240,140,40)", "rgb(150,45,55)",
        "rgb(150,145,125)", "rgb(220,215,195)", "rgb(120,250,190)"],
    'svgStyle': ['style="fill:#svgColor#;stroke-width:3;stroke:#svgColor#"'],
    "name" : ["Cheri", "Fox", "Morgana", "Jedoo", "Brick", "Shadow", "Krox",
        "Urga", "Zelph"],
    "story" : ["#hero.capitalize# was a great #occupation#, and this song tells of #heroTheir# adventure. #hero.capitalize# #didStuff#, then #heroThey# #didStuff#, then #heroThey# went home to read a book."],
    "monster" : ["dragon", "ogre", "witch", "wizard", "goblin", "golem",
        "giant", "sphinx", "warlord"],
    "setPronouns" : ["[heroThey:they][heroThem:them][heroTheir:their][heroTheirs:theirs]", "[heroThey:she][heroThem:her][heroTheir:her][heroTheirs:hers]", "[heroThey:he][heroThem:him][heroTheir:his][heroTheirs:his]"],
    "setOccupation" : ["[occupation:baker][didStuff:baked bread,decorated cupcakes,folded dough,made croissants,iced a cake]", "[occupation:warrior][didStuff:fought #monster.a#,saved a village from #monster.a#,battled #monster.a#,defeated #monster.a#]"],
    "origin" : ["#[#setPronouns#][#setOccupation#][hero:#name#]story#"]
    }

tests = (
    ("plaintextShort", {
        "src": "a",
    }),
    ("plaintextLong", {
        "src": "Emma Woodhouse, handsome, clever, and rich, with a comfortable home and happy disposition, seemed to unite some of the best blessings of existence; and had lived nearly twenty-one years in the world with very little to distress or vex her.",
    }),
    # Escape chars
    ("escapeCharacter", {
        "src": "\\#escape hash\\# and escape slash\\\\"
    }),
    ("escapeDeep", {
        "src": "#deepHash# [myColor:#deeperHash#] #myColor#",
    }),
    ("escapeQuotes", {
        "src": "\"test\" and \'test\'"
    }),
    ("escapeBrackets", {
        "src": "\\[\\]"
    }),
    ("escapeHash", {
        "src": "\\#"
    }),
    ("unescapeCharSlash", {
        "src": "\\\\"
    }),
    ("escapeMelange1", {
        "src": "An action can have inner tags: \[key:\#rule\#\]"
    }),
    ("escapeMelange2", {
        "src": "A tag can have inner actions: \"\\#\\[myName:\\#name\\#\\]story\\[myName:POP\\]\\#\""
    }),
    # Web-specifics
    ("emoji", {
        "src": u"💻🐋🌙🏄🍻"
    }),
    ("unicode", {
        "src": "&\\#x2665; &\\#x2614; &\\#9749; &\\#x2665;"
    }),
    ("svg", {
        "src": '<svg width="100" height="70"><rect x="0" y="0" width="100" height="100" #svgStyle#/> <rect x="20" y="10" width="40" height="30" #svgStyle#/></svg>'
    }),
    # Push
    ("pushBasic", {
        "src": "[pet:#animal#]You have a #pet#. Your #pet# is #mood#."
    }),
    ("pushPop", {
        "src": "[pet:#animal#]You have a #pet#. [pet:#animal#]Pet:#pet# [pet:POP]Pet:#pet#"
    }),
    ("tagAction", {
        "src": "#[pet:#animal#]nonrecursiveStory# post:#pet#"
    }),
    ("testComplexGrammar", {
        "src": "#origin#"
    }),
    ("missingModifier", {
        "src": "#animal.foo#"
    }),
    ("modifierWithParams", {
        "src": "[pet:#animal#]#nonrecursiveStory# -> #nonrecursiveStory.replace(beach,mall)#"
    }),
    ("recursivePush", {
        "src": "[pet:#animal#]#recursiveStory#"
    }),
    # Errors
    ("unmatchedHash", {
        "src": "#unmatched"
    }),
    ("missingSymbol", {
        "src": "#unicorns#"
    }),
    ("missingRightBracket", {
        "src": "[pet:unicorn"
    }),
    ("missingLeftBracket", {
        "src": "pet:unicorn]"
    }),
    ("justALotOfBrackets", {
        "src": "[][]][][][[[]]][[]]]]"
    }),
    ("bracketTagMelange", {
        "src": "[][#]][][##][[[##]]][#[]]]]"
    }),
)

from tracery.modifiers.baseenglish import modifiers
for test_name, test in tests:
    grammar = tracery.Grammar(test_grammar)
    grammar.add_modifiers(modifiers)
    print "testing ", test_name, "..."
    #print tracery.parse(test['src'])
    print grammar.flatten(test['src'])
    print grammar.errors
