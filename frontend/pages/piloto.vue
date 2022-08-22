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
                  v-model="addData.piloto_id"
                  label="RAB do piloto"
                  outlined
                  :rules="[v => !!v || 'RAB é obrigatório']"
                />
                <v-text-field
                  v-model="addData.companhia_id"
                  label="ID da Companhia Aérea"
                  outlined
                  :rules="[v => !!v || 'ID da companhia é obrigatório']"
                />
                <v-text-field
                  v-model="addData.nome"
                  label="Nome"
                  outlined
                  :rules="[v => !!v || 'Nome do piloto é obrigatório']"
                />
                <v-text-field
                  v-model="addData.sobrenome"
                  label="Sobrenome"
                  outlined
                  :rules="[v => !!v || 'Sobrenome do piloto é obrigatório']"
                />
                <v-text-field
                  v-model="addData.telefone"
                  label="Telefone"
                  outlined
                  :rules="[v => !!v || 'Telefone do piloto é obrigatório']"
                />
                <v-text-field
                  v-model="addData.email"
                  label="Email"
                  outlined
                  :rules="[v => !!v || 'Email do piloto é obrigatório']"
                />
                <v-checkbox
                  v-model="addData.comandante"
                  label="Comandante"
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
                  label="RAB do piloto"
                  prepend-icon="mdi-account-outline"
                  outlined
                  :rules="[v => !!v || 'RAB é obrigatório']"
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
                  label="RAB do piloto"
                  outlined
                  :rules="[v => !!v || 'RAB é obrigatório']"
                />
                <v-text-field
                  v-model="updateData.companhia_id"
                  label="ID da Companhia Aérea"
                  outlined
                />
                <v-text-field
                  v-model="updateData.nome"
                  label="Nome"
                  outlined
                />
                <v-text-field
                  v-model="updateData.sobrenome"
                  label="Sobrenome"
                  outlined
                />
                <v-text-field
                  v-model="updateData.telefone"
                  label="Telefone"
                  outlined
                />
                <v-text-field
                  v-model="updateData.email"
                  label="Email"
                  outlined
                />
                <v-checkbox
                  v-model="updateData.comandante"
                  label="Comandante"
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
        companhia_id: '',
        nome: '',
        sobrenome: '',
        telefone: '',
        email: '',
        comandante: false
      },
      removeData: {
        _key: 'piloto_id',
        _value: ''
      },
      updateData: {
        _key: 'piloto_id',
        _value: '',
        companhia_id: '',
        nome: '',
        sobrenome: '',
        telefone: '',
        email: '',
        comandante: false
      },
      data: [],
      header: [
        { text: 'Piloto ID', value: 'piloto_id' },
        { text: 'Companhia Aérea ID', value: 'companhia_id' },
        { text: 'Nome', value: 'nome' },
        { text: 'Sobrenome', value: 'sobrenome' },
        { text: 'Telefone', value: 'telefone' },
        { text: 'E-mail', value: 'email' },
        { text: 'Comandante', value: 'comandante' }
      ]
    }
  },

  mounted () {
    this.get()
  },

  methods: {
    get () {
      this.$axios.get('/api/piloto')
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

        this.$axios.post('/api/piloto', data)
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
        this.$axios.delete('/api/piloto', {
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

        this.$axios.put('/api/piloto', data)
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
