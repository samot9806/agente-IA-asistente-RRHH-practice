import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from tools import obtener_salario, calcular_bono

# Cargar las variables seguras desde el archivo .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la GEMINI_API_KEY en el archivo .env. Por favor, configúrala.")

# Inicializar el cliente oficial con el nuevo SDK
client = genai.Client(api_key=api_key)

# Definir las herramientas disponibles para el agente
tools_list = [obtener_salario, calcular_bono]

# Instrucciones de sistema para el comportamiento del agente
system_instruction = "Eres un asistente de recursos humanos amable y preciso. Utiliza las herramientas disponibles para responder consultas sobre salarios y calcular bonos de los empleados."

def iniciar_agente():
    print("==================================================")
    print("🤖 Asistente de Recursos Humanos (IA Agéntica) listo.")
    print("Escribe tu pregunta o escribe 'salir' para terminar.")
    print("==================================================\n")
    
    # Crear una sesión de chat con el nuevo SDK utilizando gemini-3.7-flash
    chat = client.chats.create(
        model="gemini-3.7-flash",
        config=types.GenerateContentConfig(
            tools=tools_list,
            system_instruction=system_instruction,
            temperature=0.3
        )
    )

    while True:
        try:
            user_input = input("Tú: ")
            if user_input.lower() in ["salir", "exit", "quit"]:
                print("¡Hasta luego!")
                break
            
            if not user_input.strip():
                continue

            # Enviar el mensaje al chat (el SDK maneja las herramientas automáticamente)
            response = chat.send_message(user_input)
            print(f"\nAgente: {response.text}\n")
            
        except Exception as e:
            print(f"\n[Error inesperado]: {e}\n")

if __name__ == "__main__":
    iniciar_agente()