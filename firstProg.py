    public function insert($categoriaId, $nomProducto, $Stock, $PrecioVenta, $imagen) {
        $sql = "INSERT INTO $this->table (Id_Categoria, Nombre_Producto, Stock, Precio_Venta, Imagen) VALUES (?, ?, ?, ?, ?)";
        $stmt = $this->conn->prepare($sql);
        $stmt->bind_param("isids", $categoriaId, $nomProducto, $Stock, $PrecioVenta, $imagen);
        return $stmt->execute();
    }
    
    public function obtenerProdut($product){
        $sql = "SELECT * FROM producto WHERE Nombre_Producto = ?";
        $stmt = $this->conn->prepare($sql);
        $stmt->bind_param("s", $product);
        $stmt->execute();
        
        $result = $stmt->get_result();
        if ($result->num_rows === 1) {
            $producto = $result->fetch_assoc();
            return $producto; // Devolver los datos del usuario
        } else {
            return null; // Usuario no encontrado
        }
        
        $stmt->close();
    }