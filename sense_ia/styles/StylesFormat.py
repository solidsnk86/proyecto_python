from colorama import Fore, Style

class Styles:
    @staticmethod
    def menu_principal():
        print('''
    ╔═════════════════════════════════════════════════════╗
    ║                                                     ║
    ║      ¡BIENVENIDO A SENSE IA - GPT MODEL!            ║
    ║                                                     ║
    ╠═════════════════════════════════════════════════════╣
    ║                                                     ║
    ║               1️⃣  👉 Crear usuario                   ║  
    ║               2️⃣  🗑️  Borrar usuario                  ║
    ║               3️⃣  🔐 Iniciar sesión                  ║
    ║               4️⃣  🚪 Salir                           ║
    ║                                                     ║
    ╚═════════════════════════════════════════════════════╝
    '''
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
    def highlight_code(text):
        """
        Resalta bloques de código en la respuesta.
        Busca patrones que empiezen con ```language y los resalta con letra verde.
        """
        lines = text.split('\n')
        in_code_block = False
        result_lines = []
        
        for line in lines:
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                # Aplicar estilo al marcador de inicio/fin del bloque
                result_lines.append(f"{Fore.GREEN}{line}{Style.RESET_ALL}")
            # Si estamos dentro de un bloque de código
            elif in_code_block:
                result_lines.append(f"{Fore.LIGHTGREEN_EX}{line}{Style.RESET_ALL}")
            # Líneas normales sin formato especial
            else:
                result_lines.append(line)
        
        return '\n'.join(result_lines)