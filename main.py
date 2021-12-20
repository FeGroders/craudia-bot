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
    question = input("Usuário: ").capitalize()
    answer = bot.get_response(question)
    if float(answer.confidence) > 0.5:
        print('Craudia: ', question)
    else:
        print('Craudia: Ainda não sei responder esta pergunta')
        correct_response = Statement(text=input('Por favor digite uma resposta coerente: ').capitalize())
        bot.learn_response(correct_response, question)
        print('Obrigada por me ajudar a melhorar!')
