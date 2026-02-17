from gestion import submenu_usuarios, submenu_herramientas, limpiar_pantalla, pausar
from j_son1 import cargar_datos_usu, cargar_datos_her, guardar_datos_her, cargar_prestamos, guardar_prestamos

def banner_bienvenida():
    limpiar_pantalla()
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 60 + "║")
    print("║" + " " * 12 + "🏘️  SISTEMA DE GESTIÓN RESIDENCIAL  🏘️" + " " * 12 +  "║")
    print("║" + " " * 60 + "║")
    print("╚" + "═" * 60 + "╝")

def menu_inicio():
    banner_bienvenida()
    print("\n╔" + "═" * 60 + "╗")
    print("║" + " " * 18 + "🔐 INICIO DE SESIÓN 🔐" + " " * 20 + "║")
    print("╠" + "═" * 60 + "╣")
    print("║  1. 👨‍💼 Ingresar como Administrador                       ║")
    print("║  2. 👤 Ingresar como Residente                             ║")
    print("║  3. 🚪 Salir del sistema                                   ║")
    print("╚" + "═" * 60 + "╝")

def menu_administrador():
    limpiar_pantalla()
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 15 + "👨‍💼 PANEL DE ADMINISTRADOR 👨‍💼" + " " * 13 + "║")
    print("╠" + "═" * 60 + "╣")
    print("║  1. 👥 Gestionar Usuarios                                  ║")
    print("║  2. 🔧 Gestionar Herramientas                              ║")
    print("║  3. ✉️ Gestionar Solicitudes de Préstamos                  ║")
    print("║  4. 📊 Ver estadísticas del sistema                        ║")
    print("║  5. 📋 Ver todos los préstamos                             ║")
    print("║  6. ↩️ Cerrar sesión                                       ║")
    print("╚" + "═" * 60 + "╝")

def menu_residente():
    limpiar_pantalla()
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 18 + "👤 PANEL DE RESIDENTE 👤" + " " * 18 + "║")
    print("╠" + "═" * 60 + "╣")
    print("║  1. 🔧 Ver herramientas disponibles                        ║")
    print("║  2. 📝 Solicitar préstamo de herramienta                   ║")
    print("║  3. 📋 Ver mis préstamos activos                           ║")
    print("║  4. ✅ Devolver herramienta                                ║")
    print("║  5. 👤 Ver mi perfil                                       ║")
    print("║  6. ↩️  Cerrar sesión                                       ║")
    print("╚" + "═" * 60 + "╝")

def validar_credenciales(tipo_usuario):
    print("\n" + "─" * 60)
    id_usuario = input("🆔 Ingrese su ID de usuario: ").strip()
    
    usuarios = cargar_datos_usu("usuarios.json")
    
    for usuario in usuarios:
        if usuario["id"] == id_usuario and usuario['tipo'] == tipo_usuario:
            print(f"\n✅ ¡Bienvenido/a {usuario['nombre']} {usuario['apellido']}!")
            pausar()
            return usuario
    
    print(f"\n❌ Error: Usuario no encontrado o no tiene permisos de {tipo_usuario}")
    pausar()
    return None

def validar_fecha(fecha):
    """
    Valida que una fecha tenga formato DD/MM/AAAA y sea válida
    Usa for in para validar caracteres
    """
    # Verificar longitud
    if len(fecha) != 10:
        return False
    
    # Verificar formato con /
    if fecha[2] != '/' or fecha[5] != '/':
        return False
    
    # Extraer día, mes, año
    dia_str = ""
    mes_str = ""
    anio_str = ""
    
    # Extraer día (posiciones 0-1)
    for i in range(2):
        if fecha[i] not in '0123456789':
            return False
        dia_str = dia_str + fecha[i]
    
    # Extraer mes (posiciones 3-4)
    for i in range(3, 5):
        if fecha[i] not in '0123456789':
            return False
        mes_str = mes_str + fecha[i]
    
    # Extraer año (posiciones 6-9)
    for i in range(6, 10):
        if fecha[i] not in '0123456789':
            return False
        anio_str = anio_str + fecha[i]
    
    # Convertir a números
    dia = int(dia_str)
    mes = int(mes_str)
    anio = int(anio_str)
    
    # Validar rangos
    if mes < 1 or mes > 12:
        return False
    
    if dia < 1 or dia > 31:
        return False
    
    if anio < 2000 or anio > 2100:
        return False
    
    # Validar días según mes
    if mes == 2:  # Febrero
        if dia > 29:
            return False
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:  # Meses de 30 días
        if dia > 30:
            return False
    
    return True

def validar_hora(hora):
    """
    Valida que una hora tenga formato HH:MM y sea válida
    Usa for in para validar caracteres
    """
    # Verificar longitud
    if len(hora) != 5:
        return False
    
    # Verificar formato con :
    if hora[2] != ':':
        return False
    
    # Extraer horas y minutos
    horas_str = ""
    minutos_str = ""
    
    # Extraer horas (posiciones 0-1)
    for i in range(2):
        if hora[i] not in '0123456789':
            return False
        horas_str = horas_str + hora[i]
    
    # Extraer minutos (posiciones 3-4)
    for i in range(3, 5):
        if hora[i] not in '0123456789':
            return False
        minutos_str = minutos_str + hora[i]
    
    # Convertir a números
    horas = int(horas_str)
    minutos = int(minutos_str)
    
    # Validar rangos
    if horas < 0 or horas > 23:
        return False
    
    if minutos < 0 or minutos > 59:
        return False
    
    return True

def obtener_fecha_hora_manual():
    """
    Solicita al usuario que ingrese la fecha y hora manualmente
    CON VALIDACIONES ANTIBEBE
    """
    print("\n📅 Ingrese la fecha y hora actual:")
    
    # Validar fecha
    while True:
        fecha = input("Fecha (DD/MM/AAAA): ").strip()
        
        if validar_fecha(fecha):
            break
        else:
            print("❌ Fecha inválida. Use formato DD/MM/AAAA")
            print("   Ejemplo: 14/02/2024")
            print("   Día: 01-31, Mes: 01-12, Año: 2000-2100")
    
    # Validar hora
    while True:
        hora = input("Hora (HH:MM): ").strip()
        
        if validar_hora(hora):
            break
        else:
            print("❌ Hora inválida. Use formato HH:MM (24 horas)")
            print("   Ejemplo: 14:30")
            print("   Horas: 00-23, Minutos: 00-59")
    
    return f"{fecha} {hora}"


def generar_id_prestamo():
    """
    Genera un ID único para un préstamo usando for in
    """
    prestamos = cargar_prestamos()
    
    # Si no hay préstamos, empezar en P001
    if not prestamos:
        return "P001"
    
    # Encontrar el ID más alto usando for in
    numero_mayor = 0
    
    for prestamo in prestamos:
        id_actual = prestamo['id_prestamo']
        # Extraer el número del ID (ejemplo: P001 -> 001 -> 1)
        numero_str = ""
        for caracter in id_actual:
            if caracter in '0123456789':
                numero_str = numero_str + caracter
        
        if numero_str != "":
            numero = int(numero_str)
            if numero > numero_mayor:
                numero_mayor = numero
    
    # Generar el siguiente ID
    nuevo_numero = numero_mayor + 1
    nuevo_id = f"P{nuevo_numero:03d}"  # Formato P001, P002, etc.
    return nuevo_id

def ver_estadisticas():
    limpiar_pantalla()
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 18 + "📊 ESTADÍSTICAS DEL SISTEMA" + " " * 14 + "║")
    print("╚" + "═" * 60 + "╝\n")
    
    usuarios = cargar_datos_usu("usuarios.json")
    herramientas = cargar_datos_her("herramientas.json")
    prestamos = cargar_prestamos()
    
    # Contar tipos de usuarios usando for in
    administradores = 0
    residentes = 0
    
    for usuario in usuarios:
        if usuario['tipo'] == 'administrador':
            administradores = administradores + 1
        elif usuario['tipo'] == 'residente':
            residentes = residentes + 1
    
    # Contar préstamos por estado usando for in
    pendientes = 0
    aprobados = 0
    rechazados = 0
    devueltos = 0
    
    for prestamo in prestamos:
        if prestamo['estado'] == 'pendiente':
            pendientes = pendientes + 1
        elif prestamo['estado'] == 'aprobado':
            aprobados = aprobados + 1
        elif prestamo['estado'] == 'rechazado':
            rechazados = rechazados + 1
        elif prestamo['estado'] == 'devuelto':
            devueltos = devueltos + 1
    
    # Calcular cantidad total de herramientas usando for in
    cantidad_total = 0
    for herramienta in herramientas:
        cantidad_total = cantidad_total + int(herramienta['cantidad'])
    
    print("👥 USUARIOS:")
    print(f"  • Total de usuarios:    {len(usuarios)}")
    print(f"  • Administradores:      {administradores}")
    print(f"  • Residentes:           {residentes}")
    print()
    print("🔧 HERRAMIENTAS:")
    print(f"  • Total de herramientas: {len(herramientas)}")
    print(f"  • Unidades totales:      {cantidad_total}")
    print()
    print("📋 PRÉSTAMOS:")
    print(f"  • Total de solicitudes:  {len(prestamos)}")
    print(f"  • Pendientes:            {pendientes}")
    print(f"  • Aprobados (activos):   {aprobados}")
    print(f"  • Rechazados:            {rechazados}")
    print(f"  • Devueltos:             {devueltos}")
    
    pausar()

# ==================== FUNCIONES PARA RESIDENTES ====================

def ver_herramientas_disponibles():
    """Muestra todas las herramientas disponibles para préstamo usando for in"""
    limpiar_pantalla()
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 15 + "🔧 HERRAMIENTAS DISPONIBLES 🔧" + " " * 15 + "║")
    print("╚" + "═" * 60 + "╝\n")
    
    herramientas = cargar_datos_her("herramientas.json")
    
    if not herramientas:
        print("⚠️  No hay herramientas registradas en el sistema.\n")
        pausar()
        return
    
    # Filtrar herramientas disponibles usando for in
    disponibles = []
    for herramienta in herramientas:
        cantidad = int(herramienta.get('cantidad', 0))
        if cantidad > 0:
            disponibles.append(herramienta)
    
    if not disponibles:
        print("⚠️  No hay herramientas disponibles en este momento.\n")
        pausar()
        return
    
    contador = 1
    for herramienta in disponibles:
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"Herramienta #{contador}")
        print(f"  🆔 ID:        {herramienta['id']}")
        print(f"  🔧 Nombre:    {herramienta['nombre']}")
        print(f"  📦 Categoría: {herramienta['categoria']}")
        print(f"  🔢 Disponible: {herramienta['cantidad']} unidades")
        print(f"  📊 Estado:    {herramienta['estado']}")
        contador = contador + 1
    
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    print(f"📊 Total disponibles: {len(disponibles)} herramientas")
    pausar()

def solicitar_prestamo(usuario_actual):
    """Permite a un residente solicitar el préstamo de una herramienta usando for in"""
    limpiar_pantalla()
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 15 + "📝 SOLICITAR PRÉSTAMO 📝" + " " * 20 + "║")
    print("╚" + "═" * 60 + "╝\n")
    
    herramientas = cargar_datos_her("herramientas.json")
    
    # Mostrar herramientas disponibles usando for in
    disponibles = []
    for herramienta in herramientas:
        if int(herramienta.get('cantidad', 0)) > 0:
            disponibles.append(herramienta)
    
    if not disponibles:
        print("⚠️  No hay herramientas disponibles para préstamo.\n")
        pausar()
        return
    
    print("Herramientas disponibles:")
    for herramienta in disponibles:
        print(f"  • ID: {herramienta['id']} - {herramienta['nombre']} (Disponibles: {herramienta['cantidad']})")
    
    print()
    id_herramienta = input("🆔 Ingrese el ID de la herramienta a solicitar: ").strip()
    
    # Buscar la herramienta usando for in
    herramienta_encontrada = None
    posicion_herramienta = 0
    
    for i in range(len(herramientas)):
        if herramientas[i]['id'] == id_herramienta and int(herramientas[i].get('cantidad', 0)) > 0:
            herramienta_encontrada = herramientas[i]
            posicion_herramienta = i
            break
    
    if not herramienta_encontrada:
        print("\n❌ Herramienta no disponible o ID incorrecto.")
        pausar()
        return
    
    # Confirmar préstamo
    confirmacion = input(f"\n¿Confirma la solicitud de préstamo de '{herramienta_encontrada['nombre']}'? (s/n): ")
    
    if confirmacion.lower() != 's':
        print("\n🚫 Solicitud cancelada.")
        pausar()
        return
    
    # NO reducir la cantidad - se reduce cuando el admin apruebe
    # Obtener fecha y hora manual
    fecha_hora = obtener_fecha_hora_manual()
    
    # Crear registro del préstamo PENDIENTE
    prestamos = cargar_prestamos()
    
    nuevo_prestamo = {
        "id_prestamo": generar_id_prestamo(),
        "id_usuario": usuario_actual['id'],
        "nombre_usuario": f"{usuario_actual['nombre']} {usuario_actual['apellido']}",
        "id_herramienta": herramienta_encontrada['id'],
        "nombre_herramienta": herramienta_encontrada['nombre'],
        "fecha_solicitud": fecha_hora,
        "fecha_aprobacion": None,
        "fecha_devolucion": None,
        "estado": "pendiente"
    }
    
    prestamos.append(nuevo_prestamo)
    guardar_prestamos("prestamos.json", prestamos)
    
    print("\n✅ ¡Solicitud de préstamo enviada!")
    print(f"📋 ID de solicitud: {nuevo_prestamo['id_prestamo']}")
    print(f"📅 Fecha: {nuevo_prestamo['fecha_solicitud']}")
    print("⏳ Espera a que un administrador apruebe tu solicitud.")
    pausar()

def ver_mis_prestamos(usuario_actual):
    """Muestra las solicitudes y préstamos del usuario actual usando for in"""
    limpiar_pantalla()
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 18 + "📋 MIS SOLICITUDES Y PRÉSTAMOS" + " " * 12 + "║")
    print("╚" + "═" * 60 + "╝\n")
    
    prestamos = cargar_prestamos()
    
    # Filtrar por pendientes, aprobados y rechazados
    pendientes = []
    aprobados = []
    rechazados = []
    
    for prestamo in prestamos:
        if prestamo['id_usuario'] == usuario_actual['id']:
            if prestamo['estado'] == 'pendiente':
                pendientes.append(prestamo)
            elif prestamo['estado'] == 'aprobado':
                aprobados.append(prestamo)
            elif prestamo['estado'] == 'rechazado':
                rechazados.append(prestamo)
    
    # Mostrar solicitudes pendientes
    if pendientes:
        print("⏳ SOLICITUDES PENDIENTES DE APROBACIÓN:")
        print("━" * 60)
        contador = 1
        for prestamo in pendientes:
            print(f"#{contador}")
            print(f"  📋 ID: {prestamo['id_prestamo']}")
            print(f"  🔧 Herramienta: {prestamo['nombre_herramienta']}")
            print(f"  📅 Fecha solicitud: {prestamo['fecha_solicitud']}")
            print()
            contador = contador + 1
    
    # Mostrar préstamos aprobados
    if aprobados:
        print("\n✅ PRÉSTAMOS APROBADOS (ACTIVOS):")
        print("━" * 60)
        contador = 1
        for prestamo in aprobados:
            print(f"#{contador}")
            print(f"  📋 ID: {prestamo['id_prestamo']}")
            print(f"  🔧 Herramienta: {prestamo['nombre_herramienta']}")
            print(f"  📅 Fecha aprobación: {prestamo['fecha_aprobacion']}")
            print()
            contador = contador + 1
    
    # Mostrar rechazados
    if rechazados:
        print("\n❌ SOLICITUDES RECHAZADAS:")
        print("━" * 60)
        contador = 1
        for prestamo in rechazados:
            print(f"#{contador}")
            print(f"  📋 ID: {prestamo['id_prestamo']}")
            print(f"  🔧 Herramienta: {prestamo['nombre_herramienta']}")
            print(f"  📅 Fecha rechazo: {prestamo.get('fecha_rechazo', 'N/A')}")
            print()
            contador = contador + 1
    
    if not pendientes and not aprobados and not rechazados:
        print("⚠️  No tienes solicitudes ni préstamos.\n")
    
    pausar()

def devolver_herramienta(usuario_actual):
    """Permite al usuario devolver una herramienta prestada usando for in"""
    limpiar_pantalla()
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 18 + "✅ DEVOLVER HERRAMIENTA" + " " * 18 + "║")
    print("╚" + "═" * 60 + "╝\n")
    
    prestamos = cargar_prestamos()
    
    # Filtrar préstamos APROBADOS del usuario usando for in
    mis_prestamos_aprobados = []
    for prestamo in prestamos:
        if prestamo['id_usuario'] == usuario_actual['id'] and prestamo['estado'] == 'aprobado':
            mis_prestamos_aprobados.append(prestamo)
    
    if not mis_prestamos_aprobados:
        print("⚠️  No tienes préstamos aprobados para devolver.\n")
        pausar()
        return
    
    print("Tus préstamos aprobados:")
    for prestamo in mis_prestamos_aprobados:
        print(f"  • ID: {prestamo['id_prestamo']} - {prestamo['nombre_herramienta']} (Aprobado: {prestamo['fecha_aprobacion']})")
    
    print()
    id_prestamo = input("📋 Ingrese el ID del préstamo a devolver: ").strip()
    
    # Buscar el préstamo usando for in
    prestamo_encontrado = None
    posicion_prestamo = 0
    
    for i in range(len(prestamos)):
        if (prestamos[i]['id_prestamo'] == id_prestamo and 
            prestamos[i]['id_usuario'] == usuario_actual['id'] and 
            prestamos[i]['estado'] == 'aprobado'):
            prestamo_encontrado = prestamos[i]
            posicion_prestamo = i
            break
    
    if not prestamo_encontrado:
        print("\n❌ Préstamo no encontrado o no está aprobado.")
        pausar()
        return
    
    # Confirmar devolución
    confirmacion = input(f"\n¿Confirma la devolución de '{prestamo_encontrado['nombre_herramienta']}'? (s/n): ")
    
    if confirmacion.lower() != 's':
        print("\n🚫 Devolución cancelada.")
        pausar()
        return
    
    # Obtener fecha y hora de devolución manual
    fecha_hora_devolucion = obtener_fecha_hora_manual()
    
    # Actualizar el préstamo
    prestamos[posicion_prestamo]['estado'] = 'devuelto'
    prestamos[posicion_prestamo]['fecha_devolucion'] = fecha_hora_devolucion
    guardar_prestamos("prestamos.json", prestamos)
    
    # Aumentar la cantidad de la herramienta usando for in
    herramientas = cargar_datos_her("herramientas.json")
    
    for i in range(len(herramientas)):
        if herramientas[i]['id'] == prestamo_encontrado['id_herramienta']:
            cantidad_actual = int(herramientas[i]['cantidad'])
            herramientas[i]['cantidad'] = str(cantidad_actual + 1)
            guardar_datos_her("herramientas.json", herramientas)
            break
    
    print("\n✅ ¡Herramienta devuelta exitosamente!")
    print(f"📅 Fecha de devolución: {prestamos[posicion_prestamo]['fecha_devolucion']}")
    print("¡Gracias por devolver la herramienta a tiempo!")
    pausar()

def ver_mi_perfil(usuario_actual):
    """Muestra la información del perfil del usuario actual"""
    limpiar_pantalla()
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 22 + "👤 MI PERFIL 👤" + " " * 23 + "║")
    print("╚" + "═" * 60 + "╝\n")
    
    print(f"🆔 ID:        {usuario_actual['id']}")
    print(f"👤 Nombre:    {usuario_actual['nombre']} {usuario_actual['apellido']}")
    print(f"📞 Teléfono:  {usuario_actual['telefono']}")
    print(f"🏠 Dirección: {usuario_actual['direccion']}")
    print(f"🔖 Tipo:      {usuario_actual['tipo'].upper()}")
    
    # Estadísticas de préstamos usando for in
    prestamos = cargar_prestamos()
    
    total_solicitudes = 0
    pendientes = 0
    aprobados = 0
    rechazados = 0
    devueltos = 0
    
    for prestamo in prestamos:
        if prestamo['id_usuario'] == usuario_actual['id']:
            total_solicitudes = total_solicitudes + 1
            if prestamo['estado'] == 'pendiente':
                pendientes = pendientes + 1
            elif prestamo['estado'] == 'aprobado':
                aprobados = aprobados + 1
            elif prestamo['estado'] == 'rechazado':
                rechazados = rechazados + 1
            elif prestamo['estado'] == 'devuelto':
                devueltos = devueltos + 1
    
    print("\n📊 ESTADÍSTICAS DE SOLICITUDES Y PRÉSTAMOS:")
    print(f"  • Total de solicitudes:  {total_solicitudes}")
    print(f"  • Pendientes:            {pendientes}")
    print(f"  • Aprobados (activos):   {aprobados}")
    print(f"  • Rechazados:            {rechazados}")
    print(f"  • Devueltos:             {devueltos}")
    
    pausar()

# ==================== FUNCIONES PARA ADMINISTRADORES ====================

def gestionar_solicitudes_prestamos():
    """Permite al administrador aprobar o rechazar solicitudes de préstamos"""
    limpiar_pantalla()
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 12 + "✉️ GESTIONAR SOLICITUDES DE PRÉSTAMOS" + " " * 10 + "║")
    print("╚" + "═" * 60 + "╝\n")
    
    prestamos = cargar_prestamos()
    
    # Filtrar solo solicitudes pendientes usando for in
    pendientes = []
    for prestamo in prestamos:
        if prestamo['estado'] == 'pendiente': 
            pendientes.append(prestamo)
    
    if not pendientes:
        print("⚠️  No hay solicitudes pendientes.\n")
        pausar()
        return
    
    print("📋 SOLICITUDES PENDIENTES DE APROBACIÓN:")
    print("━" * 60)
    
    contador = 1
    for prestamo in pendientes:
        print(f"\nSolicitud #{contador}")
        print(f"  📋 ID Solicitud:    {prestamo['id_prestamo']}")
        print(f"  👤 Usuario:         {prestamo['nombre_usuario']} (ID: {prestamo['id_usuario']})")
        print(f"  🔧 Herramienta:     {prestamo['nombre_herramienta']} (ID: {prestamo['id_herramienta']})")
        print(f"  📅 Fecha solicitud: {prestamo['fecha_solicitud']}")
        contador = contador + 1
    
    print("\n" + "━" * 60)
    print(f"\n📊 Total de solicitudes pendientes: {len(pendientes)}")
    
    # Preguntar si quiere gestionar alguna
    print("\n¿Deseas gestionar alguna solicitud?")
    opcion = input("(s/n): ").strip().lower()
    
    if opcion != 's':
        return
    
    # Pedir ID de solicitud
    id_solicitud = input("\n📋 Ingrese el ID de la solicitud a gestionar: ").strip()
    
    # Buscar la solicitud usando for in
    solicitud_encontrada = None
    posicion_solicitud = 0
    
    for i in range(len(prestamos)):
        if prestamos[i]['id_prestamo'] == id_solicitud and prestamos[i]['estado'] == 'pendiente':
            solicitud_encontrada = prestamos[i]
            posicion_solicitud = i
            break
    
    if not solicitud_encontrada:
        print("\n❌ Solicitud no encontrada o ya fue procesada.")
        pausar()
        return
    
    # Verificar disponibilidad de la herramienta
    herramientas = cargar_datos_her("herramientas.json")
    herramienta_disponible = False
    posicion_herramienta = 0
    
    for i in range(len(herramientas)):
        if herramientas[i]['id'] == solicitud_encontrada['id_herramienta']:
            if int(herramientas[i]['cantidad']) > 0:
                herramienta_disponible = True
                posicion_herramienta = i
            break
    
    # Mostrar información de la solicitud
    print("\n" + "═" * 60)
    print("INFORMACIÓN DE LA SOLICITUD:")
    print(f"  👤 Usuario:     {solicitud_encontrada['nombre_usuario']}")
    print(f"  🔧 Herramienta: {solicitud_encontrada['nombre_herramienta']}")
    print(f"  📅 Solicitado:  {solicitud_encontrada['fecha_solicitud']}")
    
    if herramienta_disponible:
        print(f"  ✅ Disponible:  SÍ (cantidad: {herramientas[posicion_herramienta]['cantidad']})")
    else:
        print("  ❌ Disponible:  NO (sin existencias)")
    
    print("═" * 60)
    
    # Decidir acción
    print("\n¿Qué deseas hacer?")
    print("1. ✅ Aprobar solicitud")
    print("2. ❌ Rechazar solicitud")
    print("3. 🔙 Cancelar")
    
    accion = input("\nSeleccione una opción (1/2/3): ").strip()
    
    if accion == "1":
        # APROBAR
        if not herramienta_disponible:
            print("\n❌ No se puede aprobar: herramienta sin existencias.")
            pausar()
            return
        
        # Pedir fecha de aprobación
        fecha_aprobacion = obtener_fecha_hora_manual()
        
        # Actualizar préstamo
        prestamos[posicion_solicitud]['estado'] = 'aprobado'
        prestamos[posicion_solicitud]['fecha_aprobacion'] = fecha_aprobacion
        guardar_prestamos("prestamos.json", prestamos)
        
        # Reducir cantidad de herramienta
        cantidad_actual = int(herramientas[posicion_herramienta]['cantidad'])
        herramientas[posicion_herramienta]['cantidad'] = str(cantidad_actual - 1)
        guardar_datos_her("herramientas.json", herramientas)
        
        print("\n✅ ¡Solicitud APROBADA exitosamente!")
        print(f"📅 Fecha de aprobación: {fecha_aprobacion}")
        print(f"🔧 Herramienta asignada a {solicitud_encontrada['nombre_usuario']}")
        
    elif accion == "2":
        # RECHAZAR
        fecha_rechazo = obtener_fecha_hora_manual()
        
        prestamos[posicion_solicitud]['estado'] = 'rechazado'
        prestamos[posicion_solicitud]['fecha_rechazo'] = fecha_rechazo
        guardar_prestamos("prestamos.json", prestamos)
        
        print("\n❌ Solicitud RECHAZADA.")
        print(f"📅 Fecha de rechazo: {fecha_rechazo}")
        
    else:
        print("\n🔙 Operación cancelada.")
    
    pausar()

def ver_todos_prestamos():
    """Muestra todos los préstamos del sistema usando for in"""
    limpiar_pantalla()
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 18 + "📋 TODOS LOS PRÉSTAMOS" + " " * 19 + "║")
    print("╚" + "═" * 60 + "╝\n")
    
    prestamos = cargar_prestamos()
    
    if not prestamos:
        print("⚠️  No hay préstamos registrados.\n")
        pausar()
        return

    # Separar por estados usando for in
    pendientes = []
    aprobados = []
    rechazados = []
    devueltos = []
    
    for prestamo in prestamos:
        if prestamo['estado'] == 'pendiente':
            pendientes.append(prestamo)
        elif prestamo['estado'] == 'aprobado':
            aprobados.append(prestamo)
        elif prestamo['estado'] == 'rechazado':
            rechazados.append(prestamo)
        elif prestamo['estado'] == 'devuelto':
            devueltos.append(prestamo)
    
    # Mostrar pendientes
    if pendientes:
        print("⏳ SOLICITUDES PENDIENTES:")
        print("━" * 60)
        contador = 1
        for prestamo in pendientes:
            print(f"#{contador}")
            print(f"  📋 ID: {prestamo['id_prestamo']}")
            print(f"  👤 Usuario: {prestamo['nombre_usuario']} (ID: {prestamo['id_usuario']})")
            print(f"  🔧 Herramienta: {prestamo['nombre_herramienta']} (ID: {prestamo['id_herramienta']})")
            print(f"  📅 Fecha solicitud: {prestamo['fecha_solicitud']}")
            print()
            contador = contador + 1
    
    # Mostrar aprobados
    if aprobados:
        print("\n✅ PRÉSTAMOS APROBADOS (ACTIVOS):")
        print("━" * 60)
        contador = 1
        for prestamo in aprobados:
            print(f"#{contador}")
            print(f"  📋 ID: {prestamo['id_prestamo']}")
            print(f"  👤 Usuario: {prestamo['nombre_usuario']} (ID: {prestamo['id_usuario']})")
            print(f"  🔧 Herramienta: {prestamo['nombre_herramienta']} (ID: {prestamo['id_herramienta']})")
            print(f"  📅 Aprobado: {prestamo['fecha_aprobacion']}")
            print()
            contador = contador + 1
    
    # Mostrar rechazados
    if rechazados:
        print("\n❌ SOLICITUDES RECHAZADAS:")
        print("━" * 60)
        contador = 1
        for prestamo in rechazados:
            print(f"#{contador}")
            print(f"  📋 ID: {prestamo['id_prestamo']}")
            print(f"  👤 Usuario: {prestamo['nombre_usuario']}")
            print(f"  🔧 Herramienta: {prestamo['nombre_herramienta']}")
            print(f"  📅 Rechazado: {prestamo.get('fecha_rechazo', 'N/A')}")
            print()
            contador = contador + 1
    
    # Mostrar devueltos
    if devueltos:
        print("\n🔄 PRÉSTAMOS DEVUELTOS:")
        print("━" * 60)
        contador = 1
        for prestamo in devueltos:
            print(f"#{contador}")
            print(f"  📋 ID: {prestamo['id_prestamo']}")
            print(f"  👤 Usuario: {prestamo['nombre_usuario']}")
            print(f"  🔧 Herramienta: {prestamo['nombre_herramienta']}")
            print(f"  📅 Aprobado: {prestamo['fecha_aprobacion']}")
            print(f"  🔄 Devuelto: {prestamo['fecha_devolucion']}")
            print()
            contador = contador + 1
    
    print("━" * 60)
    print(f"📊 Total: {len(prestamos)} | Pendientes: {len(pendientes)} | Aprobados: {len(aprobados)} | Rechazados: {len(rechazados)} | Devueltos: {len(devueltos)}")
    pausar()

# ==================== SESIONES ====================

def sesion_administrador(usuario):
    """Maneja la sesión del administrador"""
    while True:
        menu_administrador()
        opcion = input("\n🔹 Seleccione una opción: ")

        if opcion == "1":
            submenu_usuarios()
        elif opcion == "2":
            submenu_herramientas()
        elif opcion == "3":
            gestionar_solicitudes_prestamos()
        elif opcion == "4":
            ver_estadisticas()
        elif opcion == "5":
            ver_todos_prestamos()
        elif opcion == "6":
            print("\n👋 Cerrando sesión de administrador...")
            pausar()
            break
        else:
            print("\n❌ Opción inválida. Intente nuevamente.")
            pausar()

def sesion_residente(usuario):
    """Maneja la sesión del residente"""
    while True:
        menu_residente()
        opcion = input("\n🔹 Seleccione una opción: ")

        if opcion == "1":
            ver_herramientas_disponibles()
        elif opcion == "2":
            solicitar_prestamo(usuario)
        elif opcion == "3":
            ver_mis_prestamos(usuario)
        elif opcion == "4":
            devolver_herramienta(usuario)
        elif opcion == "5":
            ver_mi_perfil(usuario)
        elif opcion == "6":
            print("\n👋 Cerrando sesión...")
            pausar()
            break
        else:
            print("\n❌ Opción inválida. Intente nuevamente.")
            pausar()

# ==================== MAIN ====================

def main_inicio():
    while True:
        menu_inicio()
        opcion = input("\n🔹 Seleccione una opción: ")

        if opcion == "1":
            # Login como administrador
            usuario = validar_credenciales("administrador")
            if usuario:
                sesion_administrador(usuario)
                
        elif opcion == "2":
            # Login como residente
            usuario = validar_credenciales("residente")
            if usuario:
                sesion_residente(usuario)
                
        elif opcion == "3":
            limpiar_pantalla()
            print("\n" + "═" * 60)
            print("   👋 ¡Gracias por usar el Sistema de Gestión Residencial!")
            print("   🏘️  ¡Hasta pronto!")
            print("═" * 60 + "\n")
            break
        else:
            print("\n❌ Opción inválida. Intente nuevamente.")
            pausar()
main_inicio()
