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
