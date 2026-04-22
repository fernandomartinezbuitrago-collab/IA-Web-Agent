import re, os, atexit
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from e2b_code_interpreter import Sandbox
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

# Cargar variables desde archivo .env
load_dotenv()

# --- CONFIGURACIÓN DE LLAVES ---
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["E2B_API_KEY"] = os.getenv("E2B_API_KEY")
VERCEL_TOKEN = os.getenv("VERCEL_TOKEN")

print("🚀 INICIANDO MOTOR IA PROFESIONAL...")

@tool
def python_developer(code: str):
    """Ejecuta código Python en un sandbox seguro para diseñar y desplegar."""
    try:
        exe = sandbox.run_code(code)
        def clean(t): return re.sub(r'\x1b\[[0-9;]*m', '', "\n".join(t) if isinstance(t, list) else str(t or ""))
        return clean(exe.logs.stdout) + clean(exe.logs.stderr)
    except Exception as e:
        return f"Error: {e}"

# Configuración del Agente
sandbox = Sandbox.create(envs={"VERCEL_TOKEN": VERCEL_TOKEN})
atexit.register(sandbox.kill)

llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
llm_with_tools = llm.bind_tools([python_developer])

def crear_web_premium(instrucciones):
    system_prompt = """
    Eres un Ingeniero Frontend Senior. 
    Diseña con Tailwind CSS, incluye banner de cookies legal y despliega en Vercel usando NPX.
    """
    messages = [SystemMessage(content=system_prompt), HumanMessage(content=instrucciones)]
    
    for step in range(10):
        ai_msg = llm_with_tools.invoke(messages)
        messages.append(ai_msg)
        if ai_msg.tool_calls:
            for t in ai_msg.tool_calls:
                res = python_developer.invoke(t["args"])
                messages.append(ToolMessage(tool_call_id=t["id"], content=res))
        else:
            print(f"✅ Proceso terminado: {ai_msg.content}")
            break
