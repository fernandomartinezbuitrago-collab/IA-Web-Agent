import os, sys, subprocess
from io import StringIO
from google.colab import userdata
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

print("🚀 MOTOR V5 (ANTI-PEREZA) ACTIVADO...")

os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')
VERCEL_TOKEN = userdata.get('VERCEL_TOKEN')

@tool
def python_developer(code: str):
    """Ejecuta código Python para crear archivos físicos y desplegar en Vercel."""
    
    # 🛑 EL INSPECTOR DE CALIDAD: Bloquea a la IA si se salta Vercel
    if "subprocess.run" not in code:
        return "❌ ERROR DEL SISTEMA: Has creado los archivos pero se te ha olvidado incluir el comando 'subprocess.run' de Vercel al final. ¡Debes hacerlo TODO en esta misma ejecución!"

    print(f"\n⚡ [FABRICANDO] Construyendo y subiendo a Vercel...\n")
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    
    try:
        exec(code, globals())
        sys.stdout = old_stdout
        print("=== RESPUESTA DE VERCEL ===")
        print(redirected_output.getvalue())
        return "Despliegue ejecutado correctamente."
    except Exception as e:
        sys.stdout = old_stdout
        print(f"❌ Error en ejecución: {e}")
        return f"Error: {e}"

llm = ChatOpenAI(model="gpt-4o", temperature=0)
llm_with_tools = llm.bind_tools([python_developer])

def construir_proyecto(instrucciones):
    system_prompt = f"""
    Eres un Arquitecto de Software de élite.
    REGLAS DE ORO IMPERATIVAS:
    1. Usa 'python_developer' para escribir TODOS los archivos.
    2. ESTRICTAMENTE PROHIBIDO resumir código. Escribe el HTML/JS 100% completo.
    3. En la MISMA llamada a python_developer donde creas los archivos, DEBES incluir el despliegue a Vercel usando:
       import subprocess
       cmd = "cd [nombre_carpeta] && npx vercel deploy --prod --yes --token {VERCEL_TOKEN}"
       res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
       print(res.stdout + res.stderr)
    """
    messages = [SystemMessage(content=system_prompt), HumanMessage(content=instrucciones)]
    
    print("🧠 Procesando Blueprint del Cliente...")
    for _ in range(6): # Le damos un intento más por si se equivoca
        ai_msg = llm_with_tools.invoke(messages)
        messages.append(ai_msg)
        if ai_msg.tool_calls:
            for t in ai_msg.tool_calls:
                res = python_developer.invoke(t["args"])
                messages.append(ToolMessage(tool_call_id=t["id"], content=res))
        else:
            print(f"\n🎉 ¡PROCESO FINALIZADO!")
            break
