import os
from dotenv import load_dotenv
import google.generativeai as genai
from tools import obtener_salario, calcular_bono

# Cargar las variables seguras desde el archivo .env
load_dotenv()

# Obtener y configurar la API Key de Gemini
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la GEMINI_API_KEY en el archivo .env. Por favor, configúrala.")

genai.configure(api_key=api_key)

# Definir las herramientas que el agente tiene permitido usar
tools = [obtener_salario, calcular_bono]

# Configurar el modelo de Gemini pasando las herramientas disponibles
# Usamos gemini-1.5-flash por su velocidad y eficiencia en llamadas a herramientas
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    tools=tools,
    system_instruction="Eres un asistente de recursos humanos amable y preciso. Utiliza las herramientas disponibles para responder consultas sobre salarios y calcular bonos de los empleados."
)

def iniciar_agente():
    print("==================================================")
    print("🤖 Asistente de Recursos Humanos (IA Agéntica) listo.")
    print("Escribe tu pregunta o escribe 'salir' para terminar.")
    print("==================================================\n")
    
    # Iniciamos una sesión de chat que maneja automáticamente las herramientas
    chat = model.start_chat(enable_automatic_function_calling=True)

    while True:
        try:
            user_input = input("Tú: ")
            if user_input.lower() in ["salir", "exit", "quit"]:
                print("¡Hasta luego!")
                break
            
            if not user_input.strip():
                continue

            # El agente procesa el mensaje, decide si necesita una herramienta y responde
            response = chat.send_message(user_input)
            print(f"\nAgente: {response.text}\n")
            
        except Exception as e:
            print(f"\n[Error inesperado]: {e}\n")

if __name__ == "__main__":
    iniciar_agente()