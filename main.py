from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
from chatterbot import ChatBot

bot = ChatBot(
    'Craudia',
    storage_adapter='chatterbot.storage.SQLStorageAdapter')

# Train based on the portuguese corpus
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.portuguese")

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Craudia: ', resposta)
    else:
        print('Craudia: Ainda não sei responder esta pergunta.')
        print('Craudia: Você pode me ajudar a ficar mais sábia, basta me dizer uma resposta coerente')
        correct_response = Statement(text=input())
        bot.learn_response(correct_response, pergunta)