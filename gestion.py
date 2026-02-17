from j_son1 import cargar_datos_usu, guardar_datos_usu, cargar_datos_her, guardar_datos_her

def limpiar_pantalla():
    """Imprime líneas vacías para 'limpiar' la pantalla"""
    for i in range(50):
        print()

def pausar():
    input("\n🔹 Presione ENTER para continuar...")

def validar_telefono(telefono):
    """
    Valida que el teléfono tenga 10 dígitos y empiece con 3
    Uso básico de for in para recorrer cada carácter
    """
    # Verificar longitud
    if len(telefono) != 10:
        return False
    
    # Verificar que empiece con 3
    if telefono[0] != '3':
        return False
    
    # Verificar que todos sean números usando for in
    for caracter in telefono:
        if caracter not in '0123456789':
            return False
    
    return True

def validar_id_unico(id_buscar, lista_datos):
    """
    Verifica que un ID no exista ya en la lista
    Uso básico de for in
    """
    for elemento in lista_datos:
        if elemento['id'] == id_buscar:
            return False  # ID ya existe
    return True  # ID disponible

def validar_numero_positivo(texto):
    """
    Valida que un texto sea un número positivo
    Uso básico de for in
    """
    if texto == "" or texto == "0":
        return False
    
    for caracter in texto:
        if caracter not in '0123456789':
            return False
    
    return True

def men_principal():
    limpiar_pantalla()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 10 + "🏠 SISTEMA DE GESTIÓN 🏠" + " " * 16 + "║")
    print("╠" + "═" * 50 + "╣")
    print("║  1. 👥 Gestión de Usuarios                      ║")
    print("║  2. 🔧 Gestión de Herramientas                   ║")
    print("║  3. 🚪 Salir                                     ║")
    print("╚" + "═" * 50 + "╝")

def men_ges_usu():
    """Muestra el menú de gestión de usuarios"""
    limpiar_pantalla()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 12 + "👥 GESTOR DE USUARIOS 👥" + " " * 14 + "║")
    print("╠" + "═" * 50 + "╣")
    print("║  1. ➕ Registrar un usuario                      ║")
    print("║  2. 📋 Mostrar usuarios                          ║")
    print("║  3. ❌ Eliminar usuario                          ║")
    print("║  4. ✏️  Editar usuario                           ║")
    print("║  5. ↩️  Regresar al menú principal               ║")
    print("╚" + "═" * 50 + "╝")

def men_ges_her():
    """Muestra el menú de gestión de herramientas"""
    limpiar_pantalla()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 10 + "🔧 GESTOR DE HERRAMIENTAS 🔧" + " " * 10 + "║")
    print("╠" + "═" * 50 + "╣")
    print("║  1. ➕ Registrar una herramienta                 ║")
    print("║  2. 📋 Mostrar herramientas                      ║")
    print("║  3. ❌ Eliminar herramienta                      ║")
    print("║  4. ✏️  Editar herramienta                       ║")
    print("║  5. ↩️  Regresar al menú principal               ║")
    print("╚" + "═" * 50 + "╝")

# ==================== FUNCIONES DE USUARIOS ====================

def reg_usu(usuarios):
    """Registra un nuevo usuario con validaciones antibebe"""
    limpiar_pantalla()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 12 + "➕ AGREGAR NUEVO USUARIO" + " " * 13 + "║")
    print("╚" + "═" * 50 + "╝\n")

    # Validar ID
    while True:
        id = input("📝 ID del usuario (ej: USU001): ").strip()
        
        if id == "":
            print("❌ El ID no puede estar vacío")
            continue
        
        if not validar_id_unico(id, usuarios):
            print("❌ Error: Ya existe un usuario con ese ID")
            continue
        
        break

    # Validar nombre
    while True:
        nombre = input("📝 Nombre: ").strip()
        if nombre == "":
            print("❌ El nombre no puede estar vacío")
            continue
        break

    # Validar apellido
    while True:
        apellido = input("📝 Apellido: ").strip()
        if apellido == "":
            print("❌ El apellido no puede estar vacío")
            continue
        break

    # Validar teléfono
    while True:
        telefono = input("📞 Teléfono (10 dígitos, debe empezar con 3): ").strip()
        
        if not validar_telefono(telefono):
            print("❌ Teléfono inválido. Debe tener 10 dígitos y empezar con 3")
            print("   Ejemplo: 3001234567")
            continue
        
        break

    # Validar dirección
    while True:
        direccion = input("🏠 Dirección: ").strip()
        if direccion == "":
            print("❌ La dirección no puede estar vacía")
            continue
        break
    
    # Seleccionar tipo
    print("\n🔹 Tipos disponibles:")
    print("  1. Residente")
    print("  2. Administrador")
    
    while True:
        tipo_opcion = input("Seleccione el tipo (1 o 2): ").strip()
        if tipo_opcion == "1":
            tipo = "residente"
            break
        elif tipo_opcion == "2":
            tipo = "administrador"
            break
        else:
            print("❌ Opción inválida. Ingrese 1 o 2")

    nuevo_usuario = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "direccion": direccion,
        "tipo": tipo
    }

    usuarios.append(nuevo_usuario)
    guardar_datos_usu("usuarios.json", usuarios)
    print("\n✅ ¡Usuario agregado correctamente!")
    pausar()

def most_usu(usuarios):
    """Muestra todos los usuarios registrados usando for in"""
    limpiar_pantalla()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 15 + "📋 LISTA DE USUARIOS" + " " * 15 + "║")
    print("╚" + "═" * 50 + "╝\n")
    
    if not usuarios:
        print("⚠️  No hay usuarios registrados.\n")
        pausar()
        return
    
    contador = 1
    for usuario in usuarios:
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"Usuario #{contador}")
        print(f"  🆔 ID:        {usuario['id']}")
        print(f"  👤 Nombre:    {usuario['nombre']} {usuario['apellido']}")
        print(f"  📞 Teléfono:  {usuario['telefono']}")
        print(f"  🏠 Dirección: {usuario['direccion']}")
        print(f"  🔖 Tipo:      {usuario['tipo'].upper()}")
        contador = contador + 1
    
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    print(f"📊 Total de usuarios: {len(usuarios)}")
    pausar()

def elim_usu(usuarios):
    """Elimina un usuario existente usando for in"""
    limpiar_pantalla()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 15 + "❌ ELIMINAR USUARIO" + " " * 16 + "║")
    print("╚" + "═" * 50 + "╝\n")
    
    if not usuarios:
        print("⚠️  No hay usuarios para eliminar.\n")
        pausar()
        return
    
    # Mostrar lista de usuarios usando for in
    print("Usuarios disponibles:")
    for usuario in usuarios:
        print(f"  • ID: {usuario['id']} - {usuario['nombre']} {usuario['apellido']}")
    
    print()
    id_eliminar = input("🆔 Ingrese el ID del usuario a eliminar: ").strip()
    
    # Buscar usuario usando for in
    posicion = 0
    encontrado = False
    
    for usuario in usuarios:
        if usuario['id'] == id_eliminar:
            encontrado = True
            confirmacion = input(f"\n⚠️  ¿Está seguro de eliminar a {usuario['nombre']} {usuario['apellido']}? (s/n): ")
            
            if confirmacion.lower() == 's':
                usuarios.pop(posicion)
                guardar_datos_usu("usuarios.json", usuarios)
                print(f"\n✅ Usuario eliminado correctamente!")
            else:
                print("\n🚫 Operación cancelada.")
            
            pausar()
            return
        
        posicion = posicion + 1
    
    if not encontrado:
        print(f"\n❌ No se encontró ningún usuario con ID: {id_eliminar}")
        pausar()

def editar_usu(usuarios):
    """Edita un usuario existente"""
    limpiar_pantalla()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 15 + "✏️  EDITAR USUARIO" + " " * 17 + "║")
    print("╚" + "═" * 50 + "╝\n")
    
    if not usuarios:
        print("⚠️  No hay usuarios para editar.\n")
        pausar()
        return
    
    # Mostrar usuarios
    print("Usuarios disponibles:")
    for usuario in usuarios:
        print(f"  • ID: {usuario['id']} - {usuario['nombre']} {usuario['apellido']}")
    
    print()
    id_editar = input("🆔 Ingrese el ID del usuario a editar: ").strip()
    
    # Buscar usuario
    posicion = 0
    encontrado = False
    
    for usuario in usuarios:
        if usuario['id'] == id_editar:
            encontrado = True
            
            print(f"\n📝 Editando: {usuario['nombre']} {usuario['apellido']}")
            print("(Presione ENTER para mantener el valor actual)\n")
            
            # Editar nombre
            nuevo_nombre = input(f"Nombre [{usuario['nombre']}]: ").strip()
            if nuevo_nombre != "":
                usuarios[posicion]['nombre'] = nuevo_nombre
            
            # Editar apellido
            nuevo_apellido = input(f"Apellido [{usuario['apellido']}]: ").strip()
            if nuevo_apellido != "":
                usuarios[posicion]['apellido'] = nuevo_apellido
            
            # Editar teléfono
            while True:
                nuevo_telefono = input(f"Teléfono [{usuario['telefono']}]: ").strip()
                if nuevo_telefono == "":
                    break
                if validar_telefono(nuevo_telefono):
                    usuarios[posicion]['telefono'] = nuevo_telefono
                    break
                else:
                    print("❌ Teléfono inválido. Debe tener 10 dígitos y empezar con 3")
            
            # Editar dirección
            nueva_direccion = input(f"Dirección [{usuario['direccion']}]: ").strip()
            if nueva_direccion != "":
                usuarios[posicion]['direccion'] = nueva_direccion
            
            # Editar tipo
            print(f"\nTipo actual: {usuario['tipo']}")
            print("1. Residente")
            print("2. Administrador")
            nuevo_tipo = input("¿Cambiar tipo? (1/2 o ENTER para mantener): ").strip()
            if nuevo_tipo == "1":
                usuarios[posicion]['tipo'] = "residente"
            elif nuevo_tipo == "2":
                usuarios[posicion]['tipo'] = "administrador"
            
            guardar_datos_usu("usuarios.json", usuarios)
            print("\n✅ Usuario actualizado correctamente!")
            pausar()
            return
        
        posicion = posicion + 1
    
    if not encontrado:
        print(f"\n❌ No se encontró ningún usuario con ID: {id_editar}")
        pausar()

# ==================== FUNCIONES DE HERRAMIENTAS ====================

def reg_her(herramientas):
    """Registra una nueva herramienta con validaciones"""
    limpiar_pantalla()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 10 + "➕ AGREGAR NUEVA HERRAMIENTA" + " " * 11 + "║")
    print("╚" + "═" * 50 + "╝\n")

    # Validar ID
    while True:
        id = input("📝 ID de la herramienta (ej: H001): ").strip()
        
        if id == "":
            print("❌ El ID no puede estar vacío")
            continue
        
        if not validar_id_unico(id, herramientas):
            print("❌ Error: Ya existe una herramienta con ese ID")
            continue
        
        break

    # Validar nombre
    while True:
        nombre = input("📝 Nombre de la herramienta: ").strip()
        if nombre == "":
            print("❌ El nombre no puede estar vacío")
            continue
        break

    # Validar categoría
    while True:
        categoria = input("📦 Categoría (ej: Eléctrica, Manual, Jardín): ").strip()
        if categoria == "":
            print("❌ La categoría no puede estar vacía")
            continue
        break

    # Validar cantidad
    while True:
        cantidad = input("🔢 Cantidad disponible: ").strip()
        if validar_numero_positivo(cantidad):
            break
        else:
            print("❌ Debe ingresar un número positivo válido")

    # Validar estado
    print("\n📊 Estados disponibles:")
    print("  1. Nuevo")
    print("  2. Usado")
    print("  3. Dañado")
    
    while True:
        estado_opcion = input("Seleccione el estado (1, 2 o 3): ").strip()
        if estado_opcion == "1":
            estado = "Nuevo"
            break
        elif estado_opcion == "2":
            estado = "Usado"
            break
        elif estado_opcion == "3":
            estado = "Dañado"
            break
        else:
            print("❌ Opción inválida. Ingrese 1, 2 o 3")

    # Validar ubicación
    while True:
        ubicacion = input("📍 Ubicación de almacenamiento: ").strip()
        if ubicacion == "":
            print("❌ La ubicación no puede estar vacía")
            continue
        break

    nueva_herramienta = {
        "id": id,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "estado": estado,
        "ubicacion": ubicacion
    }

    herramientas.append(nueva_herramienta)
    guardar_datos_her("herramientas.json", herramientas)
    print("\n✅ ¡Herramienta agregada correctamente!")
    pausar()

def most_her(herramientas):
    """Muestra todas las herramientas registradas usando for in"""
    limpiar_pantalla()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 12 + "📋 LISTA DE HERRAMIENTAS" + " " * 13 + "║")
    print("╚" + "═" * 50 + "╝\n")
    
    if not herramientas:
        print("⚠️  No hay herramientas registradas.\n")
        pausar()
        return
    
    contador = 1
    for herramienta in herramientas:
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"Herramienta #{contador}")
        print(f"  🆔 ID:        {herramienta['id']}")
        print(f"  🔧 Nombre:    {herramienta['nombre']}")
        print(f"  📦 Categoría: {herramienta['categoria']}")
        print(f"  🔢 Cantidad:  {herramienta['cantidad']}")
        print(f"  📊 Estado:    {herramienta['estado']}")
        print(f"  📍 Ubicación: {herramienta['ubicacion']}")
        contador = contador + 1
    
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    print(f"📊 Total de herramientas: {len(herramientas)}")
    pausar()

def elim_her(herramientas):
    """Elimina una herramienta existente usando for in"""
    limpiar_pantalla()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 13 + "❌ ELIMINAR HERRAMIENTA" + " " * 14 + "║")
    print("╚" + "═" * 50 + "╝\n")
    
    if not herramientas:
        print("⚠️  No hay herramientas para eliminar.\n")
        pausar()
        return
    
    # Mostrar lista de herramientas usando for in
    print("Herramientas disponibles:")
    for herramienta in herramientas:
        print(f"  • ID: {herramienta['id']} - {herramienta['nombre']}")
    
    print()
    id_eliminar = input("🆔 Ingrese el ID de la herramienta a eliminar: ").strip()
    
    # Buscar herramienta usando for in
    posicion = 0
    encontrado = False
    
    for herramienta in herramientas:
        if herramienta['id'] == id_eliminar:
            encontrado = True
            confirmacion = input(f"\n⚠️  ¿Está seguro de eliminar {herramienta['nombre']}? (s/n): ")
            
            if confirmacion.lower() == 's':
                herramientas.pop(posicion)
                guardar_datos_her("herramientas.json", herramientas)
                print(f"\n✅ Herramienta eliminada correctamente!")
            else:
                print("\n🚫 Operación cancelada.")
            
            pausar()
            return
        
        posicion = posicion + 1
    
    if not encontrado:
        print(f"\n❌ No se encontró ninguna herramienta con ID: {id_eliminar}")
        pausar()

def editar_her(herramientas):
    """Edita una herramienta existente"""
    limpiar_pantalla()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 13 + "✏️  EDITAR HERRAMIENTA" + " " * 15 + "║")
    print("╚" + "═" * 50 + "╝\n")
    
    if not herramientas:
        print("⚠️  No hay herramientas para editar.\n")
        pausar()
        return
    
    # Mostrar herramientas
    print("Herramientas disponibles:")
    for herramienta in herramientas:
        print(f"  • ID: {herramienta['id']} - {herramienta['nombre']}")
    
    print()
    id_editar = input("🆔 Ingrese el ID de la herramienta a editar: ").strip()
    
    # Buscar herramienta
    posicion = 0
    encontrado = False
    
    for herramienta in herramientas:
        if herramienta['id'] == id_editar:
            encontrado = True
            
            print(f"\n📝 Editando: {herramienta['nombre']}")
            print("(Presione ENTER para mantener el valor actual)\n")
            
            # Editar nombre
            nuevo_nombre = input(f"Nombre [{herramienta['nombre']}]: ").strip()
            if nuevo_nombre != "":
                herramientas[posicion]['nombre'] = nuevo_nombre
            
            # Editar categoría
            nueva_categoria = input(f"Categoría [{herramienta['categoria']}]: ").strip()
            if nueva_categoria != "":
                herramientas[posicion]['categoria'] = nueva_categoria
            
            # Editar cantidad
            while True:
                nueva_cantidad = input(f"Cantidad [{herramienta['cantidad']}]: ").strip()
                if nueva_cantidad == "":
                    break
                if validar_numero_positivo(nueva_cantidad):
                    herramientas[posicion]['cantidad'] = nueva_cantidad
                    break
                else:
                    print("❌ Debe ingresar un número positivo válido")
            
            # Editar estado
            print(f"\nEstado actual: {herramienta['estado']}")
            print("1. Nuevo")
            print("2. Usado")
            print("3. Dañado")
            nuevo_estado = input("¿Cambiar estado? (1/2/3 o ENTER para mantener): ").strip()
            if nuevo_estado == "1":
                herramientas[posicion]['estado'] = "Nuevo"
            elif nuevo_estado == "2":
                herramientas[posicion]['estado'] = "Usado"
            elif nuevo_estado == "3":
                herramientas[posicion]['estado'] = "Dañado"
            
            # Editar ubicación
            nueva_ubicacion = input(f"Ubicación [{herramienta['ubicacion']}]: ").strip()
            if nueva_ubicacion != "":
                herramientas[posicion]['ubicacion'] = nueva_ubicacion
            
            guardar_datos_her("herramientas.json", herramientas)
            print("\n✅ Herramienta actualizada correctamente!")
            pausar()
            return
        
        posicion = posicion + 1
    
    if not encontrado:
        print(f"\n❌ No se encontró ninguna herramienta con ID: {id_editar}")
        pausar()

# ==================== SUBMENÚ USUARIOS ====================

def submenu_usuarios():
    while True:
        usuarios = cargar_datos_usu("usuarios.json")
        men_ges_usu()
        opcion = input("\n🔹 Seleccione una opción: ")

        if opcion == "1":
            reg_usu(usuarios)
        elif opcion == "2":
            most_usu(usuarios)
        elif opcion == "3":
            elim_usu(usuarios)
        elif opcion == "4":
            editar_usu(usuarios)
        elif opcion == "5":
            break
        else:
            print("\n❌ Opción inválida. Intente nuevamente.")
            pausar()

# ==================== SUBMENÚ HERRAMIENTAS ====================

def submenu_herramientas():
    """Maneja el submenú de gestión de herramientas"""
    while True:
        herramientas = cargar_datos_her("herramientas.json")
        men_ges_her()
        opcion = input("\n🔹 Seleccione una opción: ")

        if opcion == "1":
            reg_her(herramientas)
        elif opcion == "2":
            most_her(herramientas)
        elif opcion == "3":
            elim_her(herramientas)
        elif opcion == "4":
            editar_her(herramientas)
        elif opcion == "5":
            break
        else:
            print("\n❌ Opción inválida. Intente nuevamente.")
            pausar()

# ==================== MENÚ PRINCIPAL ====================

def main():
    while True:
        men_principal()
        opcion = input("\n🔹 Seleccione una opción: ")

        if opcion == "1":
            submenu_usuarios()
        elif opcion == "2":
            submenu_herramientas()
        elif opcion == "3":
            limpiar_pantalla()
            print("\n👋 ¡Gracias por usar el sistema! ¡Hasta pronto!\n")
            break
        else:
            print("\n❌ Opción inválida. Intente nuevamente.")
            pausar()

if __name__ == "__main__":
    main()
