# 🚀 AI Modular Agency Architecture (V5)

![Version](https://img.shields.io/badge/version-5.0-blue.svg)
![Architecture](https://img.shields.io/badge/architecture-Full--Stack-success.svg)

Este proyecto es un motor avanzado de Inteligencia Artificial diseñado para agencias web. Permite construir y desplegar aplicaciones web Full-Stack (Frontend, Backend Serverless y Base de Datos) de forma 100% autónoma utilizando procesamiento de lenguaje natural y arquitectura modular.

## 🌟 La Evolución: De Landing Pages a Ecosistemas Completos

Hemos superado la generación de webs estáticas. La versión V5 ensambla negocios digitales listos para facturar, incluyendo:

- **Frontend Premium:** Diseños de alta conversión inyectando clases precisas de Tailwind CSS (Layouts complejos, transiciones, iframes).
- **Backend Serverless:** Creación automática de endpoints en Node.js (`/api/reservas`, `/api/noticias`).
- **Base de Datos (Supabase):** Integración nativa con PostgreSQL mediante peticiones REST para gestionar citas y contenido.
- **CMS Privado:** Generación de un panel de administración (`/admin.html`) blindado mediante inyección de contraseñas por *Headers* HTTP (`x-admin-pass`), sin necesidad de pesados sistemas de autenticación.
- **Despliegue Cero-Clics:** Integración directa con Vercel CLI.

---

## 🏗️ El Paradigma: Motor vs. Blueprint

La magia de esta arquitectura radica en su separación estricta:

1. **El Motor (`motor_v5.py`):** El "obrero". Un script inmutable de Python impulsado por LangChain y GPT-4o a temperatura 0 (máxima precisión). Intercepta la consola y obliga a la IA a escribir y desplegar código físico sin resúmenes ni atajos.
2. **El Blueprint (`plantilla_cliente.py`):** El "plano del arquitecto". Variables en texto plano donde el usuario define colores, precios, reglas de negocio y credenciales de base de datos. Para cambiar de cliente, solo cambias el Blueprint; el motor nunca se toca.

---

## ⚙️ Instalación y Requisitos

### 1. Clonar e Instalar Dependencias

```bash
git clone [https://github.com/TU_USUARIO/IA-Web-Agent.git](https://github.com/TU_USUARIO/IA-Web-Agent.git)
cd IA-Web-Agent
pip install -r requirements.txt
npm install -g vercel

2. Variables de Entorno (.env)
Necesitarás configurar tus claves de acceso:

OPENAI_API_KEY=tu_clave_de_openai
VERCEL_TOKEN=tu_token_de_vercel

3. Setup de Supabase (Base de Datos)
Para que los módulos dinámicos funcionen, crea un proyecto en Supabase y configura dos tablas:

Tabla Reservas (Columnas: nombre, fecha, hora)

Tabla Noticias (Columnas: titulo, contenido, imagen_url)

Importante: Debes hacer clic en Disable RLS en ambas tablas desde el Table Editor para permitir la lectura/escritura a través de nuestra API ligera.

🚀 Uso Rápido (En Google Colab o Local)

1. Ejecuta primero el núcleo del sistema cargando el archivo motor_v5.py. Esto inicializará el agente LangChain y la herramienta de fabricación.

2. Edita plantilla_cliente.py introduciendo la API URL y la API KEY pública de tu proyecto de Supabase, así como los colores deseados de Tailwind.

3. Ejecuta el ensamblaje pasándole el Blueprint al motor:

construir_proyecto(blueprint)

El agente creará los archivos físicos, generará las rutas de la API, se conectará a Vercel y devolverá el enlace de producción directamente por consola.

💡 Ejemplos de Casos de Uso
Barberías / Salones: Web premium + Módulo de Reservas + Módulo de Novedades.

Clínicas Dentales: Landing corporativa + Formulario de Captación blindado.

Restaurantes: Carta digital + Motor de reservas de mesas.

Construido para automatizar agencias. Diseñado para escalar.
