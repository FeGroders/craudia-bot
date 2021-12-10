from chatterbot import ChatBot
from chatterbot.conversation import Statement

# Create a new instance of a ChatBot
bot = ChatBot(
    'Craudia',
    storage_adapter='chatterbot.storage.SQLStorageAdapter'
)


def get_feedback():
    text = input()
    if 'sim' in text.lower():
        return True
    elif 'não' or 'nao' in text.lower():
        return False
    else:
        print('Por favor, responda sim ou não.')
        return get_feedback()


while True:
    print('Digite algo...')
    try:
        input_statement = Statement(text=input())
        response = bot.generate_response(
            input_statement
        )

        print('\n"{}" é uma resposta coerente para "{}"? \n'.format(
            response.text,
            input_statement.text
        ))
        if get_feedback() is False:
            print('Por favor digite uma resposta coerente')
            correct_response = Statement(text=input())
            bot.learn_response(correct_response, input_statement)
            print(correct_response)
            print(input_statement)
            print('Resposta adicionada a Jussara!')
        else: 
            print('Obrigada por me ajudar a me aprimorar!')    

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break