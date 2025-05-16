import psycopg2
import uuid
from dsn import DSN
from colorama import Fore, Style
import getpass

conn = psycopg2.connect(**DSN)

class Model:
    @staticmethod
    def create_user():
        try:
            with conn:
                with conn.cursor() as cursor:
                    query = "INSERT INTO public.user (id, username, password) VALUES (%s, %s, %s)"
                    username = input("\nIngrese nombre de usuario:")
                    password = getpass.getpass("Ingrese la contraseña: ")
                    random_id = uuid.uuid4()
                    converted_values = (
                        str(random_id),
                        username.strip(),
                        password.strip(),
                    )

                    cursor.execute(query, converted_values)
                    print(f"{Fore.CYAN}{cursor.rowcount} Registro insertado: {username}{Style.RESET_ALL}")
        except psycopg2.Error as e:
            print(f"Acá algo huele mal...💩: {e}")

    @staticmethod
    def delete_user():
        try:
            with conn:
                with conn.cursor() as cursor:
                    query = "DELETE FROM public.user WHERE username = %s AND password = %s"
                    username = input(
                        "\nIngrese el nombre del usuario que desea eliminar: "
                    )
                    password = getpass.getpass("Ingrese la contraseña: ")
                    cursor.execute(query, (username, password))
                    print(f"Se ha eliminado el usuario: {username}")
        except psycopg2.Error as e:
            print(f"No se pudo eliminar el usuario: {e}")
            
    @staticmethod
    def update_user(username):
        try:
            with conn:
                with conn.cursor() as cursor:
                    query = "UPDATE public.user SET username = %s WHERE username = %s"
                    new_user = input(f"\n{Fore.LIGHTRED_EX}Editar el nombre de usuario:{Style.RESET_ALL} ")
                    cursor.execute(query, (new_user, username))
                    print(f"{Fore.GREEN}Se ha actualizado el nombre de usuario: {username} -> {new_user}{Style.re}")
        except psycopg2.Error as e:
            print(f"No se pudo actualizar el usuario: {e}")
            
    @staticmethod
    def login():
        try:
            with conn:
                with conn.cursor() as cursor:
                    query = "SELECT id, username FROM public.user WHERE username = %s AND password = %s"

                    print("Credenciales\n")
                    username = input("Ingrese el nombre: ").strip()
                    password = getpass.getpass("Ingrese la contraseña: ").strip()

                    cursor.execute(
                        query, (username, password)
                    ) 

                    user_data = cursor.fetchone()

                    if user_data:
                        user_id, username = user_data
                        print(f"✅ Usuario autenticado: {str(username)}")

                        user = {
                            "id": user_id,
                            "username": username,
                            "is_authenticated": True,
                        }

                        return user
                    else:
                        print("❌ Usuario o contraseña incorrectos.")
                        return None
        except psycopg2.Error as e:
            print(f"Error en la base de datos: {e}")
            return None
