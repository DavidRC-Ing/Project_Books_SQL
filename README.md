# 📚 Project: Analysis for New Lines of Books
### *Análisis de comportamiento de usuarios, libros y editoriales para el diseño de un nuevo producto digital*

---

## 🧠 Contexto del Proyecto
El mercado de plataformas digitales de lectura ha crecido de forma acelerada en los últimos años, especialmente tras la pandemia, impulsando nuevos hábitos de consumo cultural.  
Este proyecto analiza una **base de datos real de una plataforma de libros**, con el objetivo de entender:

- el comportamiento de los usuarios,
- la popularidad y calidad de los libros,
- el desempeño de autores y editoriales.

Los resultados sirven como base para **definir una propuesta de valor de un nuevo producto digital** enfocado en mejorar la experiencia del usuario y potenciar la plataforma.

---

## 🎯 Finalidad del Proyecto
Extraer **insights accionables** a partir de datos históricos para apoyar decisiones estratégicas de producto.

### Objetivo General
Analizar la base de datos de la plataforma para identificar **tendencias y patrones relevantes** que contribuyan al desarrollo de un nuevo producto digital.

### Objetivos Específicos
- Comprender la estructura y relación de las tablas disponibles.
- Identificar libros publicados después del **1 de enero de 2000**.
- Calcular el número de reseñas y la **calificación promedio** por libro.
- Detectar la **editorial con mayor producción** de libros (>50 páginas).
- Identificar autores con **mejor calificación promedio**, considerando volumen suficiente de reseñas.
- Analizar el comportamiento de los **usuarios más activos**.

---

## 📊 Datos Utilizados
La base de datos incluye las siguientes tablas:

| Tabla | Descripción |
|------|-------------|
| `books` | Información de libros (título, páginas, fecha, editorial) |
| `authors` | Información de autores |
| `publishers` | Editoriales |
| `ratings` | Calificaciones numéricas de usuarios |
| `reviews` | Reseñas textuales de usuarios |

---

## 🔬 Metodología
- Conexión a base de datos **SQL**
- Consultas analíticas para responder preguntas de negocio
- Análisis exploratorio de datos (EDA)
- Identificación de patrones en:
  - publicaciones,
  - calificaciones,
  - reseñas,
  - participación de usuarios

---

## 💡 Conclusiones Clave

- 📈 **Crecimiento editorial:**  
  Se identificaron **819 libros publicados después del año 2000**, evidenciando un aumento significativo en la producción editorial.

- 📉 **Cambio en tendencias de publicación:**  
  Los lanzamientos crecieron de forma casi lineal hasta 2006 y luego cayeron más de un **70% a partir de 2007**, lo que sugiere cambios estructurales en la industria (digitalización, nuevos formatos, cambios de consumo).

- ⭐ **Popularidad y calidad:**  
  Los libros con más reseñas permiten evaluaciones más confiables. El libro líder supera las **1000 reseñas**, mientras que el resto del top muestra una participación notablemente menor.

- 👍 **Valoración positiva general:**  
  Los libros más populares mantienen calificaciones promedio entre **3.5 y 4.5**, indicando buena percepción por parte de los usuarios.

- 🏢 **Editoriales líderes:**  
  **Penguin Books** domina el ranking de publicaciones, seguida por **Vintage** y **Grand Central Publishing**. La diversidad editorial fortalece la oferta de la plataforma.

- ✍️ **Participación de usuarios:**  
  Solo un grupo reducido de usuarios ha calificado más de 50 libros y escrito reseñas, con un promedio de **24.3 reseñas** por usuario.  
  La mayoría de usuarios califica, pero **no deja comentarios escritos**.

- 🚀 **Oportunidad clara de mejora:**  
  La baja interacción crítica representa una oportunidad estratégica para fomentar la participación y enriquecer la experiencia lectora.

---

## 💎 Propuesta de Valor: Nuevo Producto Digital

### Descripción General
Se propone el desarrollo de **mejoras en la plataforma** orientadas a:
- incentivar la interacción del usuario,
- personalizar la experiencia lectora,
- mejorar la visibilidad de libros, autores y editoriales.

### Objetivos del Producto
1. **Fomentar participación activa**  
   Implementar gamificación, recompensas o reconocimientos para incentivar la creación de reseñas.

2. **Personalización inteligente**  
   Recomendaciones basadas en calificaciones, reseñas y hábitos de lectura.

3. **Visibilizar diversidad editorial y autoral**  
   Promover tanto grandes editoriales como autores y nichos menos explorados.

4. **Monitoreo de tendencias**  
   Integrar analítica continua para detectar cambios en preferencias y comportamiento del mercado.

---

## 🛠️ Herramientas
- **SQL** (consultas analíticas)
- **Python** (análisis exploratorio)
- Análisis de datos orientado a **producto digital**



---

📌 *Este proyecto demuestra cómo el análisis de datos puede guiar decisiones estratégicas de producto y mejorar la experiencia del usuario.*
