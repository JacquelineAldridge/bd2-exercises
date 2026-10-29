<script setup>
import { ref } from 'vue'
const nombre = ref("")
const aceptaTerminos = ref(false)
const color = ref("primary")
const cambiarColor = () => {
    color.value = "warning"
}
const estaActivo = ref(false)
const usuarios = [
    { id: 1, nombre: "Ana" },
    { id: 2, nombre: "Juan" },
    { id: 3, nombre: "Camila" }
]

const productos = [
    { id: 1, nombre: "Laptop", precio: 620000 },
    { id: 2, nombre: "Mouse", precio: 15000 },
    { id: 3, nombre: "Teclado", precio: 8000 }
]
</script>
<template>
    <v-container>
        <input v-model="nombre" />
        <p> Estas escribiendo {{ nombre }}</p>

        <input type="checkbox" v-model="aceptaTerminos"> Acepta los términos?
        <p> Aceptaste los términos? {{ aceptaTerminos ? 'Sí' : 'No' }}</p>
    </v-container>
    <v-btn :color="color" variant="tonal" @click="cambiarColor"> Click para cambiar el color </v-btn>

    <div class="mx-5">
        <v-text-field label="Ingrese un color" v-model="color"> </v-text-field>
        <v-btn :color="color"> Botón</v-btn>
    </div>

    <div v-if="estaActivo">
        El usuario esta activo
    </div>
    <div v-else>
        El usuario no esta activo
    </div>


    <div v-show="estaActivo">
        El usuario esta activo
    </div>
    <div v-show="!estaActivo">
        El usuario no esta activo
    </div>

    <ul>
        <li v-for="usuario in usuarios" :key="id"> {{ usuario.nombre }}</li>
    </ul>
    <v-container>
        <v-card class="mx-auto mb-3" v-for="producto in productos" rounded>
            <v-card-title class="bg-black"> {{ producto.nombre }} </v-card-title>
            <v-card-text class="py-4"> {{ producto.precio }}</v-card-text>
        </v-card>
    </v-container>

    <v-container>
        <v-row>
            <v-col v-for="producto in productos" cols="4" :key="producto.id"> {{ producto.nombre }} </v-col>
        </v-row>
    </v-container>

    Ejercicio 1: Lista de tareas simple
    <br>
    <div class="mb-10">
        Crea una aplicación que permita agregar tareas a una lista. <br>

        Requisitos:<br>
        1. Un campo de texto donde el usuario escriba el nombre de la tarea.<br>
        2. Un botón Agregar que añada la tarea a la lista y limpie el campo de texto.<br>
        3. Las tareas agregadas se muestran como una lista en pantalla.<br>
        4. Si todavía no hay tareas, se muestra el mensaje "No hay tareas aún." en lugar de la lista.<br>

        Utiliza el componente v-list
    </div>
</template>

<style lang="css" scoped>
.v-card {
    width: 30.4%;
    height: 100px;
}
</style>