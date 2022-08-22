<template>
  <v-app dark>
    <v-app-bar
      app
      clipped-left
      color="primary"
    >
      <v-toolbar-title>
        <span class="headline secondary--text font-weight-bold">Aeroporto Grifinória - Dashboard</span>
      </v-toolbar-title>
    </v-app-bar>
    <v-navigation-drawer
      app
      permanent
      clipped
      color="primary darken-1"
    >
      <v-list dark>
        <v-subheader class="pl-2">
          TABELAS
        </v-subheader>
        <v-list-item
          v-for="path, index in paths"
          :key="index"
          :to="path"
        >
          {{ index }}
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
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
      paths: {
        companhia_aerea: '/companhia_aerea',
        piloto: '/piloto',
        tripulante: '/tripulante',
        voo: '/',
        aeronave: '/aeronave',
        insumo: '/insumo',
        cartao_embarque: '/cartao_embarque',
        passageiro: '/passageiro',
        bagagem: '/bagagem'
        // voo_piloto: '/voo_piloto',
        // voo_tripulante: '/voo_tripulante',
        // insumo_voo: '/insumo_voo'
      }
    }
  }
}
</script>
