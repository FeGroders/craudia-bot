from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
from chatterbot import ChatBot

bot = ChatBot(
    'Craudia',
    storage_adapter='chatterbot.storage.SQLStorageAdapter')

# Train based on the portuguese corpus
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.portuguese")

# Train using the Ubuntu Dialog Corpus
# trainer = UbuntuCorpusTrainer(bot)
# trainer.train()

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Craudia: ', resposta)
    else:
        print('Craudia: Ainda não sei responder esta pergunta')