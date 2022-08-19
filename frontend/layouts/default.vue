<template>
  <v-app dark>
    <v-app-bar app flat color="primary">
      <v-toolbar-title>
        <span class="headline secondary--text font-weight-bold">Aeroporto Grifinória - Dashboard</span>
      </v-toolbar-title>
    </v-app-bar>
    <v-main>
      <v-container fluid>
        <Nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data () {
    return {
    }
  }
}
</script>
