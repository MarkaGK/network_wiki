<template>
  <div>
    <p>{{ msg }}</p>
    <p>{{ secondMsg }}</p>
    <button @click="getSecondMessage">Получить второе сообщение</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TestPing',
  data() {
    return {
      msg: '',       // Сообщение от первого GET-запроса
      secondMsg: '', // Сообщение от второго GET-запроса
    };
  },
  methods: {
    // Первый GET-запрос (выполняется при загрузке компонента)
    getMessage() {
      axios.get('/')
          .then((res) => {
            this.msg = res.data;
          })
          .catch((error) => {
            console.error('Ошибка в первом GET-запросе:', error);
          });
    },

    // Второй GET-запрос (выполняется по нажатию кнопки)
    getSecondMessage() {
      axios.get('/another-endpoint') // Замените на ваш URL
          .then((res) => {
            this.secondMsg = res.data;
          })
          .catch((error) => {
            console.error('Ошибка во втором GET-запросе:', error);
            this.secondMsg = 'Ошибка при получении данных';
          });
    },
  },
  created() {
    this.getMessage(); // Выполняем первый GET-запрос при создании компонента
  },
};
</script>