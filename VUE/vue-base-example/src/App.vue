<template>
  <div id="app">
    <Ejercicio1/>
  </div>
</template>

<script>
import ExampleComponent from './components/ExampleComponent'
import Ejercicio1 from './components/Ejercicio1'

export default {
  name: 'App',
  components: {
    Ejercicio1,
    ExampleComponent
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
