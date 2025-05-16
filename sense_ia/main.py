from user.services.Model import Model
from styles.StylesFormat import Styles
from ai.cohere_chat import Chat
from colorama import Fore, Style

option = 0
while option != 5:
    try:
        Styles.menu_principal()
        option = Styles.option()
        if option == 1:
            Model.create_user()
        elif option == 2:
            while True:
                print(f"\n{Fore.LIGHTYELLOW_EX}------ Zona de edición nombre usuario ------{Style.RESET_ALL}")
                print("\nDebe autenticarse para editar\n")
                query = input("Presione enter para seguir de lo contrario digite 'salir': ")
                if query == "salir":
                    print("Volviendo al menú principal..")
                    break
                else:
                    user_data = Model.login()
                    if user_data:
                        Model.update_user(user_data["username"])
        elif option == 3:
            try:
                user_data = Model.login()        
                if user_data:
                    print('Redirigiendo al chat..')
                    Chat.init(user_data['username'].capitalize())
                else:
                    print("No se pudo iniciar sesión.")
            except Exception as e:
                print(f"Error durante el inicio de sesión: {e}")    
        elif option == 4:
             Model.delete_user()
        elif option == 5:
            print("Saliendo del sistema...")
    except Exception as e:
        print(f"\n{Fore.YELLOW}⚠ Error en el ingreso de datos, ingrese una de las opciones disponibles!{Style.RESET_ALL}")