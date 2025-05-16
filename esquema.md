### Esquema de la Base de Datos

#### Tabla: `Herramientas`
Esta tabla almacenará información básica sobre cada herramienta.

```sql
CREATE TABLE Herramientas (
    ID_Herramienta INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Tipo VARCHAR(50) NOT NULL,
    Descripcion TEXT,
    Marca VARCHAR(50),
    Modelo VARCHAR(50),
    Fecha_Adquisicion DATE,
    Ubicacion VARCHAR(100),
    Estado VARCHAR(20)  -- Por ejemplo: "En uso", "Almacenado", "Mantenimiento"
);
```

#### Tabla: `Categorias`
Esta tabla almacenará las categorías de las herramientas (por ejemplo, "Eléctricas", "Manuales", "De medición").

```sql
CREATE TABLE Categorias (
    ID_Categoria INT AUTO_INCREMENT PRIMARY KEY,
    Nombre_Categoria VARCHAR(50) NOT NULL
);
```

#### Tabla: `Herramientas_Categorias`
Esta tabla es una tabla de unión para manejar la relación muchos a muchos entre herramientas y categorías.

```sql
CREATE TABLE Herramientas_Categorias (
    ID_Herramienta INT,
    ID_Categoria INT,
    PRIMARY KEY (ID_Herramienta, ID_Categoria),
    FOREIGN KEY (ID_Herramienta) REFERENCES Herramientas(ID_Herramienta),
    FOREIGN KEY (ID_Categoria) REFERENCES Categorias(ID_Categoria)
);
```

#### Tabla: `Mantenimientos`
Esta tabla almacenará el historial de mantenimientos de las herramientas.

```sql
CREATE TABLE Mantenimientos (
    ID_Mantenimiento INT AUTO_INCREMENT PRIMARY KEY,
    ID_Herramienta INT,
    Fecha_Mantenimiento DATE NOT NULL,
    Descripcion TEXT,
    Costo DECIMAL(10, 2),
    FOREIGN KEY (ID_Herramienta) REFERENCES Herramientas(ID_Herramienta)
);
```

### Ejemplo de Inserción de Datos

#### Insertar Categorías
```sql
INSERT INTO Categorias (Nombre_Categoria) VALUES ('Eléctricas'), ('Manuales'), ('De medición');
```

#### Insertar Herramientas
```sql
INSERT INTO Herramientas (Nombre, Tipo, Descripcion, Marca, Modelo, Fecha_Adquisicion, Ubicacion, Estado)
VALUES ('Taladro', 'Eléctrica', 'Taladro inalámbrico de 18V', 'DeWalt', 'DCD791D2', '2023-01-15', 'Almacén 1', 'En uso');

INSERT INTO Herramientas (Nombre, Tipo, Descripcion, Marca, Modelo, Fecha_Adquisicion, Ubicacion, Estado)
VALUES ('Martillo', 'Manual', 'Martillo de clavos de 16 oz', 'Stanley', 'STHT51546', '2022-11-10', 'Taller 2', 'Almacenado');
```

#### Asignar Categorías a Herramientas
```sql
INSERT INTO Herramientas_Categorias (ID_Herramienta, ID_Categoria)
VALUES (1, 1);  -- Taladro es de categoría Eléctricas

INSERT INTO Herramientas_Categorias (ID_Herramienta, ID_Categoria)
VALUES (2, 2);  -- Martillo es de categoría Manuales
```

#### Registrar Mantenimiento
```sql
INSERT INTO Mantenimientos (ID_Herramienta, Fecha_Mantenimiento, Descripcion, Costo)
VALUES (1, '2023-06-01', 'Cambio de batería y limpieza general', 50.00);
```

### Consultas de Ejemplo

1. **Obtener todas las herramientas y sus categorías:**
```sql
SELECT h.Nombre, h.Tipo, h.Marca, h.Modelo, c.Nombre_Categoria
FROM Herramientas h
JOIN Herramientas_Categorias hc ON h.ID_Herramienta = hc.ID_Herramienta
JOIN Categorias c ON hc.ID_Categoria = c.ID_Categoria;
```

2. **Obtener el historial de mantenimientos de una herramienta específica:**
```sql
SELECT m.Fecha_Mantenimiento, m.Descripcion, m.Costo
FROM Mantenimientos m
WHERE m.ID_Herramienta = 1;
```

3. **Obtener herramientas que están en uso y su ubicación:**
```sql
SELECT Nombre, Ubicacion
FROM Herramientas
WHERE Estado = 'En uso';
```

Espero que este ejemplo te sea útil, Ceci. Si necesitas algo más específico o tienes alguna pregunta, no dudes en decírmelo. ¡Buena suerte con tu proyecto!