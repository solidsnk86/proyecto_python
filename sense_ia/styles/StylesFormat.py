from colorama import init, Fore, Style, Back

init(autoreset=True)
class Styles:
    @staticmethod
    def menu_principal():
        print(f'''{Fore.BLUE + Back.BLACK}
        ╔═════════════════════════════════════════════════════╗
        ║                                                     ║
        ║ {Fore.CYAN}👾 ¡BIENVENIDO A SENSE IA - ADMIN MODE! {Fore.BLUE}            ║
        ║                                                     ║
        ╠═════════════════════════════════════════════════════╣
        ║                                                     ║
        ║ {Fore.GREEN}🚀  [1] Crear usuario{Fore.BLUE}                               ║
        ║ {Fore.YELLOW}🛠️   [2] Editar usuario{Fore.BLUE}                             ║
        ║ {Fore.RED}🗑️   [3] Borrar usuario{Fore.BLUE}                             ║
        ║ {Fore.MAGENTA}🔐  [4] Iniciar sesión{Fore.BLUE}                              ║
        ║ {Fore.WHITE}🚪  [5] Salir{Fore.BLUE}                                       ║
        ║                                                     ║
        ╚═════════════════════════════════════════════════════╝
        {Style.RESET_ALL}''')
    
    @staticmethod
    def menu_chat(username):
        print("""
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║   🌟 ¡BIENVENIDO A TU ASISTENTE VIRTUAL! 🌟          ║
    ║                                                      ║
    ╠══════════════════════════════════════════════════════╣
    ║                                                      ║
    ║   👋 ¡Hola, {}!                                   ║
    ║                                                      ║
    ║   💬 Puedes preguntarme lo que quieras               ║
    ║   💡 Estoy aquí para ayudarte                        ║
    ║   🚪 Escribe 'salir' para terminar                   ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
    """.format(username))
        
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