<template>
  <v-container
    class="d-flex flex-column"
    fluid
  >
    <v-card height="100%" flat>
      <v-card-title class="secondary--text font-weight-bold">
        Companhias Aéreas
      </v-card-title>
      <v-data-table
        :headers="header"
        :items="data"
        :items-per-page="5"
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

        <!-- ADICIONAR -->
        <v-tab-item>
          <v-card flat>
            <v-card-text>
              <v-form ref="formAdd">
                <v-text-field
                  v-model="addData.voo_id"
                  label="ID do Voo"
                  prepend-icon="mdi-airplane"
                  outlined
                  :rules="[v => !!v || 'ID do Voo é obrigatório']"
                />
                <v-text-field
                  v-model="addData.passageiro_id"
                  label="ID do Passageiro"
                  prepend-icon="mdi-account-outline"
                  outlined
                  :rules="[v => !!v || 'ID do passageiro é obrigatório']"
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
                      v-model="addData.data_emissao"
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
                    v-model="addData.data_emissao"
                    no-title
                    @input="menu1 = false"
                  />
                </v-menu>
                <v-text-field
                  v-model="addData.assento"
                  label="Assento"
                  prepend-icon="mdi-seat"
                  outlined
                  :rules="[v => !!v || 'Assento é obrigatório']"
                />
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

        <!-- REMOVER -->
        <v-tab-item>
          <v-card flat>
            <v-card-text>
              <v-form ref="formRemove">
                <v-text-field
                  v-model="removeData._value"
                  label="ID do cartão de embarque"
                  prepend-icon="mdi-card-bulleted"
                  outlined
                  :rules="[v => !!v || 'ID do cartão é obrigatório']"
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

        <!-- MODIFICAR -->
        <v-tab-item>
          <v-card flat>
            <v-card-text>
              <v-form ref="formUpdate">
                <v-text-field
                  v-model="updateData._value"
                  label="ID do cartão de embarque"
                  outlined
                  :rules="[v => !!v || 'ID da aeronave é obrigatório']"
                />
                <v-text-field
                  v-model="updateData.voo_id"
                  label="ID do Voo"
                  prepend-icon="mdi-airplane"
                  outlined
                />
                <v-text-field
                  v-model="updateData.passageiro_id"
                  label="ID do Passageiro"
                  prepend-icon="mdi-account-outline"
                  outlined
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
                      v-model="updateData.data_emissao"
                      label="Data"
                      persistent-hint
                      prepend-icon="mdi-calendar"
                      outlined
                      v-bind="attrs"
                      v-on="on"
                    />
                  </template>
                  <v-date-picker
                    v-model="updateData.data_emissao"
                    no-title
                    @input="menu1 = false"
                  />
                </v-menu>
                <v-text-field
                  v-model="updateData.assento"
                  label="Assento"
                  prepend-icon="mdi-seat"
                  outlined
                />
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
      addData: {
        voo_id: '',
        data_emissao: '',
        assento: ''
      },
      removeData: {
        _key: 'cartao_id',
        _value: ''
      },
      updateData: {
        _key: 'cartao_id',
        _value: '',
        voo_id: '',
        data_emissao: '',
        assento: ''
      },
      data: [],
      header: [
        { text: 'ID do cartão', value: 'cartao_id' },
        { text: 'Voo ID', value: 'voo_id' },
        { text: 'Passageiro ID', value: 'passageiro_id' },
        { text: 'Data de Emissão', value: 'data_emissao' },
        { text: 'Assento', value: 'assento' }
      ]
    }
  },

  mounted () {
    this.get()
  },

  methods: {
    get () {
      this.$axios.get('/api/cartao_embarque')
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

        this.$axios.post('/api/cartao_embarque', data)
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
        this.$axios.delete('/api/cartao_embarque', {
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

        // Removing all empty strings
        Object.keys(data).forEach((key) => {
          if (data[key] === '' || data[key] === ' ' || data[key] === null || data[key] === 'null null') {
            delete data[key]
          }
        })

        this.$axios.put('/api/cartao_embarque', data)
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
