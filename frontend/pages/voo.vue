<template>
  <v-container
    class="d-flex flex-column"
    fluid
  >
    <v-card height="100%" flat>
      <v-card-title class="secondary--text font-weight-bold">
        Voos
      </v-card-title>
      <v-data-table
        :headers="header"
        :items="data"
        :items-per-page="20"
      />
    </v-card>

    <v-card flat>
      <v-card-title class="secondary--text font-weight-bold">
        CRUD
      </v-card-title>
      <v-tabs vertical>
        <v-tab>Adicionar</v-tab>
        <v-tab>Remover</v-tab>
        <v-tab>Modificar</v-tab>

        <v-tab-item>
          <v-card flat>
            <v-card-text>
              <v-form ref="formAdd">
                <v-text-field
                  v-model="addData.aeronave_id"
                  label="ID da aeronave"
                  prepend-icon="mdi-airplane"
                  outlined
                  :rules="[v => !!v || 'ID da aeronave é obrigatório']"
                />
                <v-text-field
                  v-model="addData.origem"
                  label="Origem"
                  prepend-icon="mdi-airplane-takeoff"
                  counter="10"
                  outlined
                  :rules="[v => !!v || 'Origem é obrigatória']"
                />
                <v-text-field
                  v-model="addData.destino"
                  label="Destino"
                  prepend-icon="mdi-airplane-landing"
                  counter="10"
                  outlined
                  :rules="[v => !!v || 'Destino é obrigatório']"
                />
                <v-menu
                  ref="menu1"
                  v-model="menu1"
                  :close-on-content-click="false"
                  transition="scale-transition"
                  offset-y
                  max-width="290px"
                  min-width="auto"
                >
                  <template #activator="{ on, attrs }">
                    <v-text-field
                      v-model="addData.data"
                      label="Data"
                      persistent-hint
                      prepend-icon="mdi-calendar"
                      outlined
                      v-bind="attrs"
                      :rules="[v => !!v || 'Data é obrigatória']"
                      v-on="on"
                    />
                  </template>
                  <v-date-picker
                    v-model="addData.data"
                    no-title
                    @input="menu1 = false"
                  />
                </v-menu>
                <v-menu
                  ref="menu2"
                  v-model="menu2"
                  :close-on-content-click="false"
                  transition="scale-transition"
                  offset-y
                  max-width="500px"
                >
                  <template #activator="{ on, attrs }">
                    <v-text-field
                      v-model="addData.hora"
                      label="Horário"
                      persistent-hint
                      prepend-icon="mdi-clock"
                      outlined
                      v-bind="attrs"
                      :rules="[v => !!v || 'Horário é obrigatório']"
                      v-on="on"
                    />
                  </template>
                  <v-time-picker
                    v-if="menu2"
                    v-model="addData.hora"
                    format="24hr"
                    full-width
                  />
                </v-menu>
                <v-select
                  v-model="addData.status"
                  :items="items"
                  label="Status"
                  prepend-icon="mdi-list-status"
                  outlined
                  :rules="[v => !!v || 'Status é obrigatório']"
                />
                <v-menu
                  ref="menu3"
                  v-model="menu3"
                  :close-on-content-click="false"
                  transition="scale-transition"
                  offset-y
                  max-width="500px"
                >
                  <template #activator="{ on, attrs }">
                    <v-text-field
                      v-model="addData.tempo_estimado"
                      label="Tempo Estimado de Vôo"
                      persistent-hint
                      prepend-icon="mdi-airplane-clock"
                      outlined
                      v-bind="attrs"
                      :rules="[v => !!v || 'Tempo Estimado de Vôo é obrigatório']"
                      v-on="on"
                    />
                  </template>
                  <v-time-picker
                    v-if="menu3"
                    v-model="addData.tempo_estimado"
                    format="24hr"
                    full-width
                  />
                </v-menu>
                <v-menu
                  ref="menu4"
                  v-model="menu4"
                  :close-on-content-click="false"
                  transition="scale-transition"
                  offset-y
                  max-width="500px"
                >
                  <template #activator="{ on, attrs }">
                    <v-text-field
                      v-model="addData.tempo_voo"
                      label="Tempo de Vôo"
                      persistent-hint
                      prepend-icon="mdi-airplane-clock"
                      outlined
                      v-bind="attrs"
                      v-on="on"
                    />
                  </template>
                  <v-time-picker
                    v-if="menu4"
                    v-model="addData.tempo_voo"
                    format="24hr"
                    full-width
                  />
                </v-menu>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn color="primary" @click="add">
                Adicionar
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <v-card-text>
              <v-form ref="formRemove">
                <v-text-field
                  v-model="removeData._value"
                  label="ID do voo"
                  prepend-icon="mdi-airplane"
                  outlined
                  :rules="[v => !!v || 'ID do voo é obrigatório']"
                />
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn color="error" @click="remove">
                Remover
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <v-card-text>
              <v-form ref="formUpdate">
                <v-text-field
                  v-model="updateData._value"
                  label="ID do voo"
                  prepend-icon="mdi-account-outline"
                  outlined
                  :rules="[v => !!v || 'ID do voo é obrigatório']"
                />
                <v-text-field
                  v-model="updateData.aeronave_id"
                  label="ID da aeronave"
                  prepend-icon="mdi-airplane"
                  outlined
                />
                <v-text-field
                  v-model="updateData.origem"
                  label="Origem"
                  prepend-icon="mdi-airplane-takeoff"
                  counter="10"
                  outlined
                />
                <v-text-field
                  v-model="updateData.destino"
                  label="Destino"
                  prepend-icon="mdi-airplane-landing"
                  counter="10"
                  outlined
                />
                <v-menu
                  ref="menu5"
                  v-model="menu5"
                  :close-on-content-click="false"
                  transition="scale-transition"
                  offset-y
                  max-width="290px"
                  min-width="auto"
                >
                  <template #activator="{ on, attrs }">
                    <v-text-field
                      v-model="updateData.data"
                      label="Data"
                      persistent-hint
                      prepend-icon="mdi-calendar"
                      outlined
                      v-bind="attrs"
                      v-on="on"
                    />
                  </template>
                  <v-date-picker
                    v-model="updateData.data"
                    no-title
                    @input="menu5 = false"
                  />
                </v-menu>
                <v-menu
                  ref="menu6"
                  v-model="menu6"
                  :close-on-content-click="false"
                  transition="scale-transition"
                  offset-y
                  max-width="500px"
                >
                  <template #activator="{ on, attrs }">
                    <v-text-field
                      v-model="updateData.hora"
                      label="Horário"
                      persistent-hint
                      prepend-icon="mdi-clock"
                      outlined
                      v-bind="attrs"
                      v-on="on"
                    />
                  </template>
                  <v-time-picker
                    v-if="menu6"
                    v-model="updateData.hora"
                    format="24hr"
                    full-width
                  />
                </v-menu>
                <v-select
                  v-model="updateData.status"
                  :items="items"
                  label="Status"
                  prepend-icon="mdi-list-status"
                  outlined
                />
                <v-menu
                  ref="menu7"
                  v-model="menu7"
                  :close-on-content-click="false"
                  transition="scale-transition"
                  offset-y
                  max-width="500px"
                >
                  <template #activator="{ on, attrs }">
                    <v-text-field
                      v-model="updateData.tempo_estimado"
                      label="Tempo Estimado de Vôo"
                      persistent-hint
                      prepend-icon="mdi-airplane-clock"
                      outlined
                      v-bind="attrs"
                      v-on="on"
                    />
                  </template>
                  <v-time-picker
                    v-if="menu7"
                    v-model="updateData.tempo_estimado"
                    format="24hr"
                    full-width
                  />
                </v-menu>
                <v-menu
                  ref="menu8"
                  v-model="menu8"
                  :close-on-content-click="false"
                  transition="scale-transition"
                  offset-y
                  max-width="500px"
                >
                  <template #activator="{ on, attrs }">
                    <v-text-field
                      v-model="updateData.tempo_voo"
                      label="Tempo de Vôo"
                      persistent-hint
                      prepend-icon="mdi-airplane-clock"
                      outlined
                      v-bind="attrs"
                      v-on="on"
                    />
                  </template>
                  <v-time-picker
                    v-if="menu8"
                    v-model="updateData.tempo_voo"
                    format="24hr"
                    full-width
                  />
                </v-menu>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn color="primary" @click="update">
                Modificar
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-tab-item>
      </v-tabs>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'IndexPage',

  data () {
    return {
      tab: null,
      menu1: false,
      menu2: false,
      menu3: false,
      menu4: false,
      menu5: false,
      menu6: false,
      menu7: false,
      menu8: false,
      items: ['Confirmado', 'Espera', 'Cancelado', 'Atrasado'],
      addData: {
        aeronave_id: '',
        origem: '',
        destino: '',
        data: '',
        hora: '',
        status: '',
        tempo_estimado: '',
        tempo_voo: ''
      },
      updateData: {
        _key: 'voo_id',
        _value: '',
        aeronave_id: '',
        origem: '',
        destino: '',
        data: '',
        hora: '',
        status: '',
        tempo_estimado: '',
        tempo_voo: ''
      },
      removeData: {
        _key: 'voo_id',
        _value: ''
      },
      data: [],
      header: [
        { text: 'Voo ID', value: 'voo_id' },
        { text: 'Aeronave ID', value: 'aeronave_id' },
        { text: 'Data', value: 'data' },
        { text: 'Origem', value: 'origem' },
        { text: 'Destino', value: 'destino' },
        { text: 'Tempo Estimado', value: 'tempo_estimado' },
        { text: 'Status', value: 'status' },
        { text: 'Tempo de Voo', value: 'tempo_voo' }
      ]
    }
  },

  mounted () {
    this.get()
  },

  methods: {
    get () {
      this.$axios.get('/api/voo')
        .then((response) => {
          this.data = response.data
        })
        .catch((error) => {
          alert(error)
        })
    },

    add () {
      this.$refs.formAdd.validate()
      if (this.$refs.formAdd.validate()) {
        const data = { ...this.addData }
        data.data = data.data + ' ' + data.hora
        delete data.hora

        this.$axios.post('/api/voo', data)
          .then((res) => {
            this.$refs.formAdd.reset()
            this.get()
            alert(res.data.message)
          })
          .catch((err) => {
            alert(err.response.data.message)
          })
      }
    },

    remove () {
      this.$refs.formRemove.validate()
      if (this.$refs.formRemove.validate()) {
        this.$axios.delete('/api/voo', {
          data: this.removeData
        })
          .then((res) => {
            this.$refs.formRemove.reset()
            this.get()
            alert(res.data.message)
          })
          .catch((err) => {
            alert(err)
          })
      }
    },

    update () {
      this.$refs.formUpdate.validate()
      if (this.$refs.formUpdate.validate()) {
        const data = { ...this.updateData }
        data.data = data.data + ' ' + data.hora
        delete data.hora

        // Removing all empty strings
        Object.keys(data).forEach((key) => {
          if (data[key] === '' || data[key] === ' ' || data[key] === null || data[key] === 'null null') {
            delete data[key]
          }
        })

        this.$axios.put('/api/voo', data)
          .then((res) => {
            this.$refs.formUpdate.reset()
            this.get()
            alert(res.data.message)
          })
          .catch((err) => {
            alert(err)
          })
      }
    }
  }
}
</script>
