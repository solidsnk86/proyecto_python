from colorama import init, Fore, Style
import cohere
from styles.StylesFormat import Styles

init()

class Chat:
    @staticmethod
    def init(username):
        Styles.menu_chat(username)
        client = cohere.ClientV2("<<tu_apikey_de_cohere>>")

        history = [
            {"role": "system", "content": f'''
                Tu nombre es SenseIA. Eres un asistente amigable, confiable y profesional.
                Hablas de forma clara y respetuosa. Tu objetivo es ayudar a los usuarios con problemas de programación, tecnología,
                seguridad informática y aprendizaje de nuevas herramientas. El nombre del usuario es {username}, dirígite a él por su nombre.
            '''}
        ]

        while True:
            query = input(f"👨 {username}: ").strip()
            if query.lower() in ["salir", "exit", "quit"]:
                print("🔚 Sesión de chat finalizada.\n")
                break

            history.append({"role": "user", "content": query})

            response = client.chat(
                model="command-a-03-2025",
                messages=history,
                temperature=0.7,
                stop_sequences=["User:", "SenseIA"],
                frequency_penalty=0.3
            )

            # Acceder al contenido de la respuesta
            text_output = "\n".join([item.text for item in response.message.content])
            print(f"\n{Fore.BLUE}🤖 SenseIA: {Style.RESET_ALL}{Styles.highlight_code(text_output)}\n")

            # Guardar respuesta en historial para mantener el contexto
            history.append({"role": "assistant", "content": text_output})