from colorama import init, Fore, Style
import cohere
from styles.StylesFormat import Styles
import time
import sys
import re

init()

class Chat:
    @staticmethod
    def init(username):
        Styles.menu_chat(username)
        client = cohere.ClientV2("lOMI0FvPadsmibCBEQbVXiESdVJgyVRXLXtwUwcQ")

        history = [
            {"role": "system", "content": f'''
                Tu nombre es SenseIA. Eres un asistente amigable, confiable y profesional.
                Hablas de forma clara y respetuosa. Tu objetivo es ayudar a los usuarios con problemas de programación, tecnología,
                seguridad informática y aprendizaje de nuevas herramientas. El nombre del usuario es {username}, dirígite a él por su nombre.
            '''}
        ]

        while True:
            query = input(f"👨 {Fore.MAGENTA}{username}{Style.RESET_ALL}: ").strip()
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

            # Obtener la respuesta completa
            full_response = "".join([chunk.text for chunk in response.message.content if chunk])

            # Dividir la respuesta en bloques de código y texto normal
            blocks = re.split(r"(```[^`]+```)", full_response)

            # Renderizar de manera gradual
            print(f"\n{Fore.BLUE}🤖 SenseIA: {Style.RESET_ALL}", end="")
            for block in blocks:
                if block.startswith("```") and block.endswith("```"):
                    # Bloque de código
                    block.strip("```")
                    for char in block:
                        sys.stdout.write(f"{Fore.GREEN}{char}{Style.RESET_ALL}")
                        sys.stdout.flush()
                        time.sleep(0.01)
                else:
                    # Texto normal
                    for char in block:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.01)
            print("\n")

            # Guardar respuesta en historial para mantener el contexto
            history.append({"role": "assistant", "content": full_response})
