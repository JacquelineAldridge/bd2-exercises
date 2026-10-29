<script setup>
import { ref } from 'vue'
const nombre = ref("")
const aceptaTerminos = ref(false)
const color = ref("primary")
const cambiarColor = () => {
    color.value = "warning"
}
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
</template>