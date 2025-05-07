from user.services.Model import Model
from styles.StylesFormat import Styles
from ai.cohere_chat import Chat

option = 0
while option != 4:
    Styles.menu_principal()
    option = int(input("\nIngrese una opción: "))
    if option == 1:
        Model.create_user()
    elif option == 2:
        Model.delete_user()
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
        print("Saliendo del sistema...")
    
    

