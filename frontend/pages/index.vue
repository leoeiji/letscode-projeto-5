<template>
  <v-row>
    <v-col cols="6">
      <v-card height="100%" class="elevation-0">
        <v-card-title class="secondary--text font-weight-bold">
          Pilotos
        </v-card-title>
        <v-data-table
          :headers="pilotosHeader"
          :items="pilotos"
          :items-per-page="5"
        />
      </v-card>
    </v-col>
    <v-col cols="6">
      <v-card height="100%" class="elevation-0">
        <v-card-title class="secondary--text font-weight-bold">
          Tripulantes
        </v-card-title>
        <v-data-table
          :headers="tripulantesHeader"
          :items="tripulantes"
          :items-per-page="5"
        />
      </v-card>
    </v-col>
    <v-col cols="6">
      <v-card height="100%" class="elevation-0">
        <v-card-title class="secondary--text font-weight-bold">
          Passageiros
        </v-card-title>
        <v-data-table
          :headers="passageirosHeader"
          :items="passageiros"
          :items-per-page="5"
        />
      </v-card>
    </v-col>
    <v-col cols="6">
      <v-card height="100%" class="elevation-0">
        <v-card-title class="secondary--text font-weight-bold">
          Voos
        </v-card-title>
        <v-data-table
          :headers="voosHeader"
          :items="voos"
          :items-per-page="5"
        />
      </v-card>
    </v-col>
    <v-col cols="6">
      <v-card height="100%" class="elevation-0">
        <v-card-title class="secondary--text font-weight-bold">
          Companhias Aéreas
        </v-card-title>
        <v-data-table
          :headers="companhiasHeader"
          :items="companhias"
          :items-per-page="5"
        />
      </v-card>
    </v-col>
    <v-col cols="6">
      <v-card height="100%" class="elevation-0">
        <v-card-title class="secondary--text font-weight-bold">
          Aeronaves
        </v-card-title>
        <v-data-table
          :headers="aeronavesHeader"
          :items="aeronaves"
          :items-per-page="5"
        />
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'IndexPage',

  data () {
    return {
      pilotos: [],
      pilotosHeader: [
        { text: 'RAB', value: 'piloto_id' },
        { text: 'Nome', value: 'nome' },
        { text: 'Sobrenome', value: 'sobrenome' },
        { text: 'E-mail', value: 'email' },
        { text: 'Telefone', value: 'telefone' }
      ],
      tripulantes: [],
      tripulantesHeader: [
        { text: 'ID', value: 'tripulante_id' },
        { text: 'Nome', value: 'nome' },
        { text: 'Sobrenome', value: 'sobrenome' },
        { text: 'E-mail', value: 'email' },
        { text: 'Telefone', value: 'telefone' },
        { text: 'Profissão', value: 'profissao' },
        { text: 'Companhia', value: 'companhia_id' }
      ],
      passageiros: [],
      passageirosHeader: [
        { text: 'Nome', value: 'nome' },
        { text: 'Sobrenome', value: 'sobrenome' },
        { text: 'E-mail', value: 'email' },
        { text: 'RG', value: 'rg' },
        { text: 'CPF', value: 'cpf' },
        { text: 'Endereço', value: 'endereco' },
        { text: 'Idade', value: 'idade' }
      ],
      voos: [],
      voosHeader: [
        { text: 'Aeronave ID', value: 'aeronave_id' },
        { text: 'Data', value: 'data' },
        { text: 'Origem', value: 'origem' },
        { text: 'Destino', value: 'destino' },
        { text: 'Tempo Estimado', value: 'tempo_estimado' },
        { text: 'Status', value: 'status' },
        { text: 'Tempo de Voo', value: 'tempo_voo' }
      ],
      companhias: [],
      companhiasHeader: [
        { text: 'Companhia ID', value: 'companhia_id' },
        { text: 'Nome', value: 'nome_cia' }
      ],

      aeronaves: [],
      aeronavesHeader: [
        { text: 'Aeronave ID', value: 'aeronave_id' },
        { text: 'Companhia ID', value: 'companhia_id' },
        { text: 'Modelo', value: 'modelo' },
        { text: 'Capacidade', value: 'capacidade' }
      ]
    }
  },

  mounted () {
    this.$axios.get('/api/piloto')
      .then((response) => {
        this.pilotos = response.data
      })
      .catch((error) => {
        alert(error)
      })

    this.$axios.get('/api/tripulante')
      .then((response) => {
        this.tripulantes = response.data
      })
      .catch((error) => {
        alert(error)
      })

    this.$axios.get('/api/passageiro')
      .then((response) => {
        this.passageiros = response.data
      })
      .catch((error) => {
        alert(error)
      })

    this.$axios.get('/api/voo')
      .then((response) => {
        this.voos = response.data
      })
      .catch((error) => {
        alert(error)
      })

    this.$axios.get('/api/companhia_aerea')
      .then((response) => {
        this.companhias = response.data
      })
      .catch((error) => {
        alert(error)
      })

    this.$axios.get('/api/aeronave')
      .then((response) => {
        this.aeronaves = response.data
      })
      .catch((error) => {
        alert(error)
      })
  }
}
</script>
