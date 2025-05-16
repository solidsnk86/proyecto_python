from colorama import Fore, Style
import sys
import time
import getpass

class Styles:
    @staticmethod
    def menu_principal():
        menu_string = f"""{Fore.BLUE}
        ╔═════════════════════════════════════════════════════╗
        ║                                                     ║
        ║       ¡BIENVENIDO A SENSE IA - ADMIN MODE!          ║
        ║                                                     ║
        ╠═════════════════════════════════════════════════════╣
        ║                                                     ║
        ║               1️⃣  👉 Crear usuario                   ║  
        ║               2️⃣  ✏️  Editar usuario                  ║
        ║               3️⃣  🔐 Iniciar sesión                  ║
        ║               4️⃣  🚯 Borrar usuario                  ║
        ║               5️⃣  🚪 Salir                           ║
        ║                                                     ║
        ╚═════════════════════════════════════════════════════╝
        {Style.RESET_ALL}"""
        for string in menu_string:
            sys.stdout.write(string)
            sys.stdout.flush()
            time.sleep(0.003)

    @staticmethod
    def option():
        print(f"""{Fore.BLUE}
        ╔═════════════════════════════════════════════════════╗
        ║                                                     ║
        ║   Ingrese una opción: {Style.RESET_ALL}""", end="")
        sys.stdout.flush()
        opt = int(input())
        print(f"""{Fore.BLUE}        ║                                                     ║
        ╚═════════════════════════════════════════════════════╝
        {Style.RESET_ALL}""")

        return opt
    
    @staticmethod
    def menu_chat(username):
        menu_string = f"""
        ╔══════════════════════════════════════════════════════╗
        ║                                                      ║
        ║   🌟 ¡BIENVENIDO A TU ASISTENTE VIRTUAL! 🌟          ║
        ║                                                      ║
        ╠══════════════════════════════════════════════════════╣
        ║                                                      ║
        ║   👋 ¡Hola, {username}!                                   ║
        ║                                                      ║
        ║   💬 Puedes preguntarme lo que quieras               ║
        ║   💡 Estoy aquí para ayudarte                        ║
        ║   🚪 Escribe 'salir' para terminar                   ║
        ║                                                      ║
        ╚══════════════════════════════════════════════════════╝
        """
        for string in menu_string:
            sys.stdout.write(string)
            sys.stdout.flush()
            time.sleep(0.003)
        
    @staticmethod
    def user_login(username):
        print(f'''{Fore.BLUE}
        ╔═════════════════════════════════════════════════════╗
        ║                                                     ║
        ║  {Fore.LIGHTGREEN_EX}Usuario: {Fore.LIGHTRED_EX}{username}{Fore.LIGHTGREEN_EX} creado con éxito 🎉{Fore.BLUE}
        ║ {Fore.LIGHTGREEN_EX}¡Puedes iniciar sesión en la aplicación! {Fore.BLUE}           ║
        ║                                                     ║
        ╚═════════════════════════════════════════════════════╝
        {Style.RESET_ALL}''')

    @staticmethod
    def username_input():
        print(f"""{Fore.BLUE}
        ╔═════════════════════════════════════════════════════╗
        ║                                                     ║
        ║   Nombre del usuario: {Style.RESET_ALL}""", end="")
        sys.stdout.flush()
        username = input()
        print(f"""{Fore.BLUE}        ║                                                     ║
        ╚═════════════════════════════════════════════════════╝
        {Style.RESET_ALL}""")

        return username
    
    @staticmethod
    def password_input():
        print(f"""{Fore.BLUE}
        ╔═════════════════════════════════════════════════════╗
        ║                                                     ║
        ║   Contraseña: {Style.RESET_ALL}""", end="")
        sys.stdout.flush()
        password = getpass.getpass("")
        print(f"""{Fore.BLUE}        ║                                                     ║
        ╚═════════════════════════════════════════════════════╝
        {Style.RESET_ALL}""")

        return password
    
    @staticmethod
    def highlight_code(text: str):
        """
        Resalta bloques de código en la respuesta.
        Busca patrones que empiezen con ```language y los resalta con letra verde.
        """
        in_code_block = False
        
        if text.startswith("```"):
            in_code_block = not in_code_block
            # Aplicar estilo al marcador de inicio/fin del bloque
            return f"{Fore.GREEN}{text}{Style.RESET_ALL}"
            # Si estamos dentro de un bloque de código
        elif in_code_block:
            return f"{Fore.LIGHTGREEN_EX}{text}{Style.RESET_ALL}"
            # Líneas normales sin formato especial
        else:
            text
        
        return '\n'.join(text)