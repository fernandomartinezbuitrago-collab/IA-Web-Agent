frontend_web = """
- ARCHIVO: index.html
Reemplaza todo index.html EXACTAMENTE con este código, sin resumir:

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Gentlemen's Club</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-slate-300 font-sans relative">

    <header class="bg-[url('https://images.unsplash.com/photo-1503951914875-452162b0f3f1?q=80&w=1920')] bg-cover bg-center h-screen relative">
        <div class="absolute inset-0 bg-black/80 flex flex-col items-center justify-center">
            <h1 class="text-5xl md:text-7xl text-amber-500 font-bold mb-4 tracking-widest uppercase text-center">The Gentlemen's Club</h1>
            <p class="text-xl text-slate-400 tracking-widest uppercase">Barbería Premium</p>
        </div>
    </header>

    <section class="py-20 px-6 max-w-7xl mx-auto">
        <h2 class="text-3xl text-amber-500 text-center mb-12 font-bold uppercase tracking-widest">Nuestros Servicios</h2>
        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-slate-800 p-8 rounded-2xl shadow-2xl border border-slate-700 transition-all duration-500 hover:scale-105 hover:bg-slate-700 hover:border-amber-500/50">
                <h3 class="text-2xl text-white font-bold mb-2">Corte Real</h3>
                <p class="text-amber-500 text-3xl font-bold mb-4">15€</p>
                <p class="text-slate-400">Degradado a navaja y lavado.</p>
            </div>
            <div class="bg-slate-800 p-8 rounded-2xl shadow-2xl border border-slate-700 transition-all duration-500 hover:scale-105 hover:bg-slate-700 hover:border-amber-500/50">
                <h3 class="text-2xl text-white font-bold mb-2">Barba VIP</h3>
                <p class="text-amber-500 text-3xl font-bold mb-4">10€</p>
                <p class="text-slate-400">Perfilado y toalla caliente.</p>
            </div>
            <div class="bg-slate-800 p-8 rounded-2xl shadow-2xl border border-slate-700 transition-all duration-500 hover:scale-105 hover:bg-slate-700 hover:border-amber-500/50">
                <h3 class="text-2xl text-white font-bold mb-2">Combo Jefe</h3>
                <p class="text-amber-500 text-3xl font-bold mb-4">22€</p>
                <p class="text-slate-400">Corte + Barba + Masaje facial.</p>
            </div>
        </div>
    </section>

    <section class="py-20 px-6 bg-slate-950">
        <h2 class="text-3xl text-amber-500 text-center mb-12 font-bold uppercase tracking-widest">Reseñas de Clientes</h2>
        <div class="grid md:grid-cols-3 gap-8 max-w-7xl mx-auto">
            <div class="bg-slate-800 p-8 rounded-2xl border border-slate-700">
                <div class="text-amber-500 text-2xl mb-4">★★★★★</div>
                <p class="text-slate-300 italic">"Excelente servicio y atención al detalle. ¡Volveré pronto!"</p>
            </div>
            <div class="bg-slate-800 p-8 rounded-2xl border border-slate-700">
                <div class="text-amber-500 text-2xl mb-4">★★★★★</div>
                <p class="text-slate-300 italic">"El mejor corte que he tenido en años. Muy recomendado."</p>
            </div>
            <div class="bg-slate-800 p-8 rounded-2xl border border-slate-700">
                <div class="text-amber-500 text-2xl mb-4">★★★★★</div>
                <p class="text-slate-300 italic">"Ambiente acogedor y profesionales de primera."</p>
            </div>
        </div>
    </section>

    <section class="py-20 px-6 max-w-7xl mx-auto">
        <h2 class="text-3xl text-amber-500 text-center mb-12 font-bold uppercase tracking-widest">Últimas Novedades</h2>
        <div id="blog-container" class="grid md:grid-cols-3 gap-8">
            <p class="text-center text-slate-500 col-span-3">Cargando noticias...</p>
        </div>
    </section>

    <section class="py-20 px-6 bg-slate-950">
        <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-stretch">
            <div class="bg-slate-800 p-10 rounded-2xl border border-slate-700 shadow-2xl">
                <h2 class="text-3xl text-amber-500 mb-8 font-bold uppercase tracking-widest">Reserva tu cita</h2>
                <form id="formReserva" class="space-y-6">
                    <input type="text" id="nombre" placeholder="Tu Nombre" class="w-full bg-slate-900 border border-slate-600 text-white p-4 rounded-xl focus:border-amber-500 focus:outline-none" required>
                    <input type="date" id="fecha" class="w-full bg-slate-900 border border-slate-600 text-slate-400 p-4 rounded-xl focus:border-amber-500 focus:outline-none" required>
                    <select id="hora" class="w-full bg-slate-900 border border-slate-600 text-slate-400 p-4 rounded-xl focus:border-amber-500 focus:outline-none" required>
                        <option value="" disabled selected>Selecciona tu hora</option>
                        <option value="10:00">10:00</option>
                        <option value="11:30">11:30</option>
                        <option value="17:00">17:00</option>
                    </select>
                    <button type="submit" id="btnSubmit" class="w-full bg-amber-500 text-slate-900 font-bold py-4 rounded-xl hover:bg-amber-400 transition-colors uppercase tracking-widest">Confirmar Reserva</button>
                    <div id="mensaje" class="hidden mt-4 p-4 rounded-xl text-center font-bold"></div>
                </form>
            </div>
            <div class="rounded-2xl overflow-hidden border border-slate-700 shadow-2xl min-h-[450px]">
                <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3037.6042371905867!2d-3.706001084600134!3d40.41703666350819!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNDDCsDI1JzAxLjMiTiAzwrA0MicyMS42Ilc!5e0!3m2!1ses!2ses!4v1620000000000!5m2!1ses!2ses" class="w-full h-full border-0" allowfullscreen="" loading="lazy"></iframe>
            </div>
        </div>
    </section>

    <footer class="bg-black py-8 text-center border-t border-slate-800">
        <p class="text-slate-500 text-sm">© 2026 The Gentlemen's Club. Todos los derechos reservados.</p>
    </footer>

    <a href="https://wa.me/34600000000?text=Hola,%20me%20gustaría%20saber%20más%20sobre%20la%20barbería." target="_blank" class="fixed bottom-6 right-6 bg-[#25D366] text-white p-4 rounded-full shadow-2xl hover:bg-[#1ebd5a] transition-all duration-300 hover:scale-110 z-50 flex items-center justify-center group">
        <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M12.031 0C5.405 0 0 5.405 0 12.031c0 2.106.55 4.156 1.581 5.96L.505 23.49l5.632-1.487A11.96 11.96 0 0012.031 24c6.626 0 12.031-5.405 12.031-12.031S18.657 0 12.031 0zm3.626 17.208c-.147.41-1.306.945-1.745.945-.438 0-1.077-.16-3.031-1.282-2.39-1.371-3.926-3.861-4.043-4.018-.117-.156-.963-1.282-.963-2.443 0-1.16.604-1.733.818-1.966.214-.233.468-.291.624-.291.156 0 .312 0 .448.006.142.006.333-.054.518.396.195.468.663 1.616.721 1.733.058.117.097.253.02.41-.078.156-.117.253-.233.389-.117.136-.243.291-.35.41-.117.117-.243.243-.107.477.136.233.604.992 1.296 1.606.895.792 1.645 1.031 1.878 1.148.233.117.37.097.506-.058.136-.156.584-.681.74-.915.156-.233.253-.41.487-.292h.02c.233.117 1.48.697 1.734.825.253.128.428.195.487.311.058.117.058.681-.088 1.09z"/>
        </svg>
        <span class="absolute right-16 bg-slate-800 text-white text-sm px-4 py-2 rounded-xl opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap shadow-xl border border-slate-700 pointer-events-none">
            ¡Chatea con nosotros!
        </span>
    </a>

    <script>
        // Lógica de reservas
        document.getElementById('formReserva').addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = document.getElementById('btnSubmit');
            const msg = document.getElementById('mensaje');
            btn.innerText = 'Procesando...'; btn.disabled = true;
            
            const payload = {
                nombre: document.getElementById('nombre').value,
                fecha: document.getElementById('fecha').value,
                hora: document.getElementById('hora').value
            };

            try {
                const res = await fetch('/api/reservas', {
                    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload)
                });
                const data = await res.json();
                
                msg.classList.remove('hidden', 'bg-green-500/20', 'text-green-400', 'bg-red-500/20', 'text-red-400');
                if(data.success) {
                    msg.classList.add('bg-green-500/20', 'text-green-400');
                    msg.innerText = data.message;
                    document.getElementById('formReserva').reset();
                } else {
                    msg.classList.add('bg-red-500/20', 'text-red-400');
                    msg.innerText = data.message;
                }
            } catch(e) {
                msg.classList.remove('hidden');
                msg.classList.add('bg-red-500/20', 'text-red-400');
                msg.innerText = "Error de conexión.";
            }
            btn.innerText = 'Confirmar Reserva'; btn.disabled = false;
        });

        // Lógica del Blog
        async function cargarNoticias() {
            try {
                const res = await fetch('/api/noticias');
                const data = await res.json();
                const container = document.getElementById('blog-container');
                
                if(data.success && data.data.length > 0) {
                    container.innerHTML = data.data.map(n => `
                        <div class="bg-slate-800 rounded-2xl overflow-hidden shadow-2xl border border-slate-700 hover:border-amber-500/50 transition-colors">
                            <img src="${n.imagen_url || 'https://images.unsplash.com/photo-1593702275687-f8b402bf1fb5?q=80&w=800'}" class="w-full h-48 object-cover" alt="Noticia">
                            <div class="p-6">
                                <h3 class="text-xl font-bold text-white mb-3">${n.titulo}</h3>
                                <p class="text-slate-400 text-sm line-clamp-3">${n.contenido}</p>
                            </div>
                        </div>
                    `).join('');
                } else {
                    container.innerHTML = '<p class="text-center text-slate-500 col-span-3 italic">Aún no hay noticias publicadas.</p>';
                }
            } catch(e) {
                document.getElementById('blog-container').innerHTML = '<p class="text-center text-red-400 col-span-3">Error al cargar noticias.</p>';
            }
        }
        cargarNoticias();
    </script>
</body>
</html>
"""

panel_admin = """
- ARCHIVO: admin.html
(Mantén exactamente el mismo HTML del panel de la oficina que hicimos en el paso anterior).
"""

motor_reservas = """
- ARCHIVO 1: api/reservas.js
(Mantén exactamente el mismo código de reservas).
"""

motor_noticias = """
- ARCHIVO 2: api/noticias.js
(Mantén exactamente el mismo código de noticias).
"""

blueprint = f"""
Nombre de la carpeta obligatoria a crear: 'barberia-gold-premium'

1. FRONTEND: {frontend_web}
2. ADMIN: {panel_admin}
3. BACKEND RESERVAS: {motor_reservas}
4. BACKEND NOTICIAS: {motor_noticias}
"""

construir_proyecto(blueprint)
