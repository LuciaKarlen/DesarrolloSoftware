<template>
    <div>
        <h1 class = "titulo">Hola!</h1>
        <h4>Ingrese su nombre y apellido</h4>
        <input v-model="nombre"/>
        <p>Hola {{ nombre }}</p>
    </div>
</template>

<style>
.titulo{
    color: pink;
}
</style>

<script>
export default {
  name: 'Ejercicio1',
  data: function () {
    return {
      nombre: ''
    }
  }
}
</script>
