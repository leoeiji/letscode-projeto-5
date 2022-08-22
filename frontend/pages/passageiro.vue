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
                  label="Nome"
                  outlined
                  :rules="[v => !!v || 'Nome é obrigatório']"
                />
                <v-text-field
                  v-model="addData.sobrenome"
                  label="Sobrenome"
                  outlined
                  :rules="[v => !!v || 'Sobrenome é obrigatório']"
                />
                <v-text-field
                  v-model="addData.idade"
                  label="Idade"
                  outlined
                  :rules="[v => !!v || 'Idade é obrigatória']"
                />
                <v-text-field
                  v-model="addData.rg"
                  label="RG"
                  outlined
                />
                <v-text-field
                  v-model="addData.cpf"
                  label="CPF"
                  outlined
                />
                <v-text-field
                  v-model="addData.email"
                  label="E-mail"
                  outlined
                />
                <v-text-field
                  v-model="addData.endereco"
                  label="Endereço"
                  outlined
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
                  label="ID do passageiro"
                  prepend-icon="mdi-account-outline"
                  outlined
                  :rules="[v => !!v || 'ID do passageiro é obrigatório']"
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
                  label="ID do passageiro"
                  outlined
                  :rules="[v => !!v || 'ID do passageiro é obrigatório']"
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
                  v-model="updateData.idade"
                  label="Idade"
                  outlined
                />
                <v-text-field
                  v-model="updateData.rg"
                  label="RG"
                  outlined
                />
                <v-text-field
                  v-model="updateData.cpf"
                  label="CPF"
                  outlined
                />
                <v-text-field
                  v-model="updateData.email"
                  label="E-mail"
                  outlined
                />
                <v-text-field
                  v-model="updateData.endereco"
                  label="Endereço"
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
        idade: '',
        nome: '',
        sobrenome: '',
        rg: '',
        cpf: '',
        email: '',
        endereco: ''
      },
      removeData: {
        _key: 'passageiro_id',
        _value: ''
      },
      updateData: {
        _key: 'passageiro_id',
        _value: '',
        idade: '',
        nome: '',
        sobrenome: '',
        rg: '',
        cpf: '',
        email: '',
        endereco: ''
      },
      data: [],
      header: [
        { text: 'Passageiro ID', value: 'passageiro_id' },
        { text: 'Idade', value: 'idade' },
        { text: 'Nome', value: 'nome' },
        { text: 'Sobrenome', value: 'sobrenome' },
        { text: 'RG', value: 'rg' },
        { text: 'CPF', value: 'cpf' },
        { text: 'E-mail', value: 'email' },
        { text: 'Endereço', value: 'endereco' }
      ]
    }
  },

  mounted () {
    this.get()
  },

  methods: {
    get () {
      this.$axios.get('/api/passageiro')
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

        this.$axios.post('/api/passageiro', data)
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
        this.$axios.delete('/api/passageiro', {
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

        this.$axios.put('/api/passageiro', data)
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
