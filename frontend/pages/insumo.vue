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
                  v-model="addData.nome"
                  label="Nome do Insumo"
                  outlined
                  :rules="[v => !!v || 'Nome do insumo é obrigatório']"
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
                  label="ID do insumo"
                  prepend-icon="mdi-food-drumstick"
                  outlined
                  :rules="[v => !!v || 'ID do insumo é obrigatório']"
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
                  label="ID do insumo"
                  outlined
                  :rules="[v => !!v || 'ID do insumo é obrigatório']"
                />
                <v-text-field
                  v-model="updateData.nome"
                  label="Nome do Insumo"
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
      addData: {
        nome: ''
      },
      removeData: {
        _key: 'insumo_id',
        _value: ''
      },
      updateData: {
        _key: 'insumo_id',
        _value: '',
        nome: ''
      },
      data: [],
      header: [
        { text: 'Insumo ID', value: 'insumo_id' },
        { text: 'Nome', value: 'nome' }
      ]
    }
  },

  mounted () {
    this.get()
  },

  methods: {
    get () {
      this.$axios.get('/api/insumo')
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

        this.$axios.post('/api/insumo', data)
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
        this.$axios.delete('/api/insumo', {
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

        this.$axios.put('/api/insumo', data)
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
