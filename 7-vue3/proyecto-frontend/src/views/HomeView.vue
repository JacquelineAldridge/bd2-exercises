<script setup>
import {ref} from "vue"
const nombre = "Estudiantes"
const asignatura = ref("base de datos II")
let num1= 3
const num2 = 5
const activo = true
const contador = ref(0)

function cambioDeAsignatura(){
  console.log(asignatura.value)
  asignatura.value = "Programación Web"
  console.log(asignatura.value)
}  

const sumar = () => contador.value++
const restar = () => contador.value--

</script>

<template>
  <h1> Mi primera aplicación con Vue3</h1>
  <p> Hola {{ nombre }}</p> 
  <p> {{ num1 + num2 }}</p>
  <div> Estado de actividad del usuario: {{ activo ? "Activo":"Inactivo" }}</div>
  {{ asignatura }}

  <!-- {{ cambioDeAsignatura() }}
   La asignatura es {{ asignatura.toLowerCase() }} -->

   <button @click="asignatura = 'hola'"> Cambiar asignatura</button>
   {{ asignatura }}
     <button @click="cambioDeAsignatura()"> Cambiar asignatura</button>
   {{ asignatura }}
    <v-btn variant="outlined" size="x-large" color="blue-darken-3" rounded append-icon="mdi-pencil"> Cambiar asignatura</v-btn>
    
    <!-- 
    Ejercicio: Añade a esta página un número en la pantalla que empiece en cero y con dos botones:
    uno que sume 1 y otro que reste 1. Crea las funciones para sumar y restar como arrow function.
    -->

  <div class="mx-15">
    <h2 class="mx-auto"> {{ contador }}</h2>
    <v-btn color="success" @click="sumar" variant="outlined" class="mr-5"> Sumar </v-btn>
    <v-btn color="error" @click="restar" variant="outlined"> Restar </v-btn>
  </div>
</template>


<style lang="css" scoped>
h2, div{
  width: fit-content
}
</style>