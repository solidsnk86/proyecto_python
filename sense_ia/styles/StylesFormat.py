from colorama import Fore, Style

class Styles:
    @staticmethod
    def menu_principal():
        print(f'''{Fore.BLUE}
    ╔═════════════════════════════════════════════════════╗
    ║                                                     ║
    ║       ¡BIENVENIDO A SENSE IA - ADMIN MODE!          ║
    ║                                                     ║
    ╠═════════════════════════════════════════════════════╣
    ║                                                     ║
    ║               1️⃣  👉 Crear usuario                   ║  
    ║               2️⃣  ✍  Editar usuario                  ║
    ║               3️⃣  🔐 Iniciar sesión                  ║
    ║               4️⃣  🗑️  Borrar usuario                  ║
    ║               5️⃣  🚪 Salir                           ║
    ║                                                     ║
    ╚═════════════════════════════════════════════════════╝
    {Style.RESET_ALL}'''
    )
    
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