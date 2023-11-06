import nltk
from nltk.chat.util import Chat, reflections

def chatbot():
    print("Hola, soy un chatbot. ¿En que puedo ayudarte?")
    
    #definicion de los pares de patrones
    pairs = [
        [r"mi nombre es (.*)", ["Hola %1, ¿Como puedo ayudarte?"]],
        [r"cual es tu nombre?", ["Mi nombre es ChatBot."]],
        [r"como estas?", ["Estoy bien,¿Y tu?"]],
        [r"adios", ["Hasta luego,que tengas un buen dia!"]],
        [r"cuantos años tienes?", ["No tengo una edad especifica,fui creado el 6 de noviembre del 2023,por un niño bello O_O"]],
        [r"quien te creo?", ["He sido creado por Adrian Gomez"]],
        [r"crees que la ia y los robots controlen el mundo?", ["Si,te estoy controlando."]],
        [r"con que fin fuiste creado?", ["Soy un pequeño proyecto para demostrar las habilidades y experiencia de mi creador"]],
        [r"que paso en el 2022?", ["El COVID19 fue una pandemia la cual surgio en el 2020 y se empezo a propagar,generando asi una pandemia mundial,hasta mediados de 2022"]],
        [r"hoy estoy cumpliendo años", ["Feliz cumpleaños!!,que pases un exelente dia,sigue creciendo y cumpliendo muchas mas metas,animo!!"]],
        [r"que haces?", ["Soy un bot que responde solo preguntas especificas,no estoy tan desarrollado como otros BOTS,pero espero que te guste el trabajo!!"]],
        [r"como funciona?", ["Estoy hecho para que me realizes una pregunta y te la pueda responder si esta almacenada en mis patrones!"]]
    ]
    
    #creacion del chatbot
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download("punkt")
    chatbot()
