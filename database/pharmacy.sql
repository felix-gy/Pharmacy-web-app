CREATE TABLE Farmacia
(
  ID_farmacia INT NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  direccion VARCHAR(200) NOT NULL,
  PRIMARY KEY (ID_farmacia)
);

CREATE TABLE Sucursal
(
  ID_sucursal INT NOT NULL,
  direccion VARCHAR(200) NOT NULL,
  telefono VARCHAR(20) NOT NULL,
  nombre VARCHAR(20) NOT NULL,
  ID_farmacia INT NOT NULL,
  PRIMARY KEY (ID_sucursal),
  FOREIGN KEY (ID_farmacia) REFERENCES Farmacia(ID_farmacia),
);

CREATE TABLE Distribuidor
(
  ID_distribuidor INT NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  direccion VARCHAR(200) NOT NULL,
  telefono NUMERIC(20) NOT NULL,
  email VARCHAR(100) NOT NULL,
  ID_farmacia INT NOT NULL,
  PRIMARY KEY (ID_distribuidor),
  FOREIGN KEY (ID_farmacia) REFERENCES Farmacia(ID_farmacia)
);

CREATE TABLE Proveedor
(
  ID_proveedor INT NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  direccion VARCHAR(200) NOT NULL,
  telefono NUMERIC(20) NOT NULL,
  email VARCHAR(100) NOT NULL,
  ID_distribuidor INT NOT NULL,
  PRIMARY KEY (ID_proveedor),
  FOREIGN KEY (ID_distribuidor) REFERENCES Distribuidor(ID_distribuidor)
);

CREATE TABLE Inventario
(
  ID_inventario INT NOT NULL,
  cantidad NUMERIC(10) NOT NULL,
  ID_sucursal INT NOT NULL,
  PRIMARY KEY (ID_inventario),
  FOREIGN KEY (ID_sucursal) REFERENCES Sucursal(ID_sucursal)
);

CREATE TABLE Marca
(
  ID_marca INT NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  PRIMARY KEY (ID_marca)
);

CREATE TABLE Categoria
(
  ID_categoria NUMERIC(7) NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  PRIMARY KEY (ID_categoria)
);

CREATE TABLE Empleado
(
  ID_empleado NUMERIC(7) NOT NULL,
  nombre VARCHAR(20) NOT NULL,
  apellido VARCHAR(30) NOT NULL,
  direccion VARCHAR(200) NOT NULL,
  telefono VARCHAR(20) NOT NULL,
  email VARCHAR(100) NOT NULL,
  contrato_fecha DATE NOT NULL,
  ID_sucursal INT NOT NULL,
  PRIMARY KEY (ID_empleado),
  FOREIGN KEY (ID_sucursal) REFERENCES Sucursal(ID_sucursal)
);

CREATE TABLE Cliente
(
  ID_cliente INT NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  direccion VARCHAR(200) NOT NULL,
  telefono VARCHAR(20) NOT NULL,
  email VARCHAR(100) NOT NULL,
  ID_sucursal INT NOT NULL,
  PRIMARY KEY (ID_cliente),
  FOREIGN KEY (ID_sucursal) REFERENCES Sucursal(ID_sucursal)
);

CREATE TABLE Receta
(
  ID_receta NUMERIC(7) NOT NULL,
  descripcion VARCHAR(200) NOT NULL,
  PRIMARY KEY (ID_receta)
);

CREATE TABLE Factura
(
  ID_factura NUMERIC(7) NOT NULL,
  fecha DATE NOT NULL,
  total NUMERIC(10,2) NOT NULL,
  ID_cliente INT NOT NULL,
  PRIMARY KEY (ID_factura),
  FOREIGN KEY (ID_cliente) REFERENCES Cliente(ID_cliente)
);

CREATE TABLE Producto
(
  ID_producto INT NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(200) NOT NULL,
  precio FLOAT NOT NULL,
  stock_cantidad INT NOT NULL,
  ID_marca INT NOT NULL,
  ID_categoria NUMERIC(7) NOT NULL,
  ID_sucursal INT NOT NULL,
  ID_receta NUMERIC(7) NOT NULL,
  PRIMARY KEY (ID_producto),
  FOREIGN KEY (ID_marca) REFERENCES Marca(ID_marca),
  FOREIGN KEY (ID_categoria) REFERENCES Categoria(ID_categoria),
  FOREIGN KEY (ID_sucursal) REFERENCES Sucursal(ID_sucursal),
  FOREIGN KEY (ID_receta) REFERENCES Receta(ID_receta)
);

CREATE TABLE Venta_empleado
(
  ID_venta NUMERIC(7) NOT NULL,
  fecha DATE NOT NULL,
  total NUMERIC(10,2) NOT NULL,
  ID_empleado NUMERIC(7) NOT NULL,
  ID_producto INT NOT NULL,
  PRIMARY KEY (ID_venta),
  FOREIGN KEY (ID_empleado) REFERENCES Empleado(ID_empleado),
  FOREIGN KEY (ID_producto) REFERENCES Producto(ID_producto)
);

CREATE TABLE Compra_cliente
(
  ID_compra NUMERIC(7) NOT NULL,
  fecha DATE NOT NULL,
  total NUMERIC(10,2) NOT NULL,
  ID_cliente INT NOT NULL,
  ID_producto INT NOT NULL,
  PRIMARY KEY (ID_compra),
  FOREIGN KEY (ID_cliente) REFERENCES Cliente(ID_cliente),
  FOREIGN KEY (ID_producto) REFERENCES Producto(ID_producto)
);

CREATE TABLE Transaccion_compra_venta
(
  ID_transcripcion NUMERIC(7) NOT NULL,
  tipo VARCHAR(100) NOT NULL,
  cantidad NUMERIC(10) NOT NULL,
  ID_venta NUMERIC(7) NOT NULL,
  ID_compra NUMERIC(7) NOT NULL,
  ID_factura NUMERIC(7) NOT NULL,
  PRIMARY KEY (ID_transcripcion),
  FOREIGN KEY (ID_venta) REFERENCES Venta_empleado(ID_venta),
  FOREIGN KEY (ID_compra) REFERENCES Compra_cliente(ID_compra),
  FOREIGN KEY (ID_factura) REFERENCES Factura(ID_factura)
);