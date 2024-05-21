

<title>Informe de Resultados del Análisis de Ruta para Robot en Rejilla</title>
<style>
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 20px;
    padding: 0;
}
h1, h2, h3 {
    margin-top: 0;
}
pre {
    background-color: #f4f4f4;
    padding: 10px;
    overflow-x: auto;
}
code {
    font-family: monospace;
}
</style>
</head>
<body>
<h1>Informe de Resultados del Análisis de Ruta para Robot en Rejilla</h1>

<h2>Descripción del Proceso:</h2>
<p>Se realizó un análisis para determinar la capacidad de un robot para encontrar una ruta desde la esquina superior izquierda hasta la esquina inferior derecha en una rejilla bidimensional. El robot puede moverse en dos direcciones: hacia abajo y hacia la derecha. Algunas celdas están bloqueadas y no se pueden atravesar.</p>

<h2>Resultados:</h2>

<h3>True (Positivo):</h3>
<p>Al llamar al método <code>find_path(0, 0)</code> con la rejilla proporcionada, el resultado fue True. Esto indica que se encontró una ruta válida desde la esquina superior izquierda hasta la esquina inferior derecha en la rejilla.</p>
<pre><code>grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

robot = Robot(grid)
print(robot.find_path(0, 0))
</code></pre>

<h3>False (Negativo):</h3>
<p>Al llamar al método <code>find_path(0, 0)</code> en una rejilla diferente donde no hay ruta posible, el resultado fue False. Esto indica que no se encontró ninguna ruta válida desde la esquina superior izquierda hasta la esquina inferior derecha en la rejilla.</p>
<pre><code>grid = [
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [0, 1, 1, 0]
]

robot = Robot(grid)
print(robot.find_path(0, 0))
</code></pre>

<h2>Conclusión:</h2>
<p>El algoritmo implementado en la clase Robot demostró ser efectivo para encontrar rutas válidas en la rejilla, proporcionando resultados precisos tanto en casos donde se encontró una ruta como en aquellos donde no se encontró ninguna ruta válida.</p>
</body>
</html>
