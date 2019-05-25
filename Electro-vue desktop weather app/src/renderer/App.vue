<template>
  <main id="app">
    <!-- 第一個部分的UI, ask question and you can type input -->
    <h2>輸入城市</h2>
    <section class="weather-input">
      <input type="text" v-model="query">
      <button :disabled="!query.length" @click="showWeather">Check</button>
    </section>
    
      <!-- 如果出現正確要顯示的部分 -->
    <!-- <section v-if="city.length" class="weather-result">
      <h1>{{city}}, {{country}}</h1>
    </section> -->

    <section v-if="city.length" class="weather-result">
      <h2> {{date_0}} </h2>

      <div class="weather-result__main">
        <img :src="icon_0" alt="Weather icon">
        <div class="weather-result__temp">
          {{temp_0}}&deg;C
          <p><em>{{weatherDescription_0}}</em></p>
        </div>
      </div>
    </section>

    <section v-if="city.length" class="weather-result">
      <h2> {{date_1}} </h2>

      <div class="weather-result__main">
        <img :src="icon_1" alt="Weather icon">
        <div class="weather-result__temp">
          {{temp_1}}&deg;C
          <p><em>{{weatherDescription_1}}</em></p>
        </div>
      </div>
    </section>

    <section v-if="city.length" class="weather-result">
      <h2> {{date_2}} </h2>
      
      <div class="weather-result__main">
        <img :src="icon_2" alt="Weather icon">
        <div class="weather-result__temp">
          {{temp_2}}&deg;C
          <p><em>{{weatherDescription_2}}</em></p>
        </div>
      </div>

      <!-- <div class="weather-result__details">
        <p>Min: {{tempMin}}&deg;C</p>
        <p>Max: {{tempMax}}&deg;C</p>
        <p>Humidity: {{humidity}}%</p>
      </div> -->
    </section>



<!-- 如果出現錯誤要輸出的部分 -->
    <section v-if="error" class="weather-error">
      找不到查詢的城市
    </section>

  </main>
</template>

<script>



async function quickstart(
  projectId = 'fast-ai-re4388-20190525' // Your GCP Project Id
) {
  // Imports the Google Cloud client library
  const {Translate} = require('@google-cloud/translate');

  // Instantiates a client
  const translate = new Translate({projectId});

  // The text to translate
  const text = 'Hello, world!';

  // The target language
  const target = 'ru';

  // Translates some text into Russian
  const [translation] = await translate.translate(text, target);
  console.log(`Text: ${text}`);
  console.log(`Translation: ${translation}`);
}


const Google_translate_API_KEY = 'AIzaSyBMuU1jbrO2NUEH0hFb5QYT2iBuCS319bg';
const API_KEY = 'cf13c71a52bad00d4b2c1f253e198b06';


export default {
  
  name: 'weather-app',

  // we will create a bunch of data properties to display different weather data
  // data resturn an object, whcih including all return query的情況
  data() {
    return {
      query: '',
      error: false,
      city: '',
      country: '',
      date:'',
      weatherDescription: '',
      temp: null,
      tempMin: null,
      tempMax: null,
      humidity: null,
      icon: '',
    };
  },

  methods: {

    // 這裡定義一個函數，主要用來處理 get request, 處理收到的respose 要定義什麼變數等
    // get, then and catch
    showWeather() {
      this.$http
        .get(`/forecast?q=${this.query}&lang=zh_tw&units=metric&&appid=${API_KEY}`)
        .then(response => {
          this.country = response.data.city.country;
          this.city = response.data.city.name;
          this.date_0 = response.data.list[0].dt_txt.substring(0, 10);
          this.weatherDescription_0 = response.data.list[0].weather[0].description;
          this.temp_0 = response.data.list[0].main.temp;
          this.icon_0 = `http://openweathermap.org/img/w/${
            response.data.list[0].weather[0].icon
          }.png`;
          this.date_1 = response.data.list[8].dt_txt.substring(0, 10);
          this.weatherDescription_1 = response.data.list[8].weather[0].description;
          this.temp_1 = response.data.list[8].main.temp;
          this.icon_1 = `http://openweathermap.org/img/w/${
            response.data.list[8].weather[0].icon
          }.png`;
          this.date_2 = response.data.list[16].dt_txt.substring(0, 10);
          this.weatherDescription_2 = response.data.list[16].weather[0].description;
          this.temp_2 = response.data.list[16].main.temp;
          this.icon_2 = `http://openweathermap.org/img/w/${
            response.data.list[16].weather[0].icon
          }.png`;



          this.error = false;

        })
        .catch(() => {
          this.error = true;
          this.city = '';
        });
    },



  },





};








</script>

<style lang="scss">
* {
  margin: 0;
  padding: 0;
}

html,

body,

#app {
  height: 100%;
}

#app {
  
  font-family: Arial, Helvetica, sans-serif;
  font-size: 16px;
  padding: 10px;
  background: rgb(212, 228, 239);
  background: -moz-radial-gradient(
    center,
    ellipse cover,
    rgba(212, 228, 239, 1) 0%,
    rgba(134, 174, 204, 1) 100%
  );
  background: -webkit-radial-gradient(
    center,
    ellipse cover,
    rgba(212, 228, 239, 1) 0%,
    rgba(134, 174, 204, 1) 100%
  );
  background: radial-gradient(
    ellipse at center,
    rgba(212, 228, 239, 1) 0%,
    rgba(134, 174, 204, 1) 100%
  );
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#d4e4ef', endColorstr='#86aecc',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */

}


.weather-input {
  display: flex;
  align-items: center;
  padding: 20px 0;
}


.weather-result {
  text-align: center;
  &__main {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 15px;
    font-size: 1.3rem;
    font-weight: bold;
  }
  &__details {
    display: flex;
    align-items: center;
    justify-content: space-around;
    color: dimgray;
  }
}


.weather-error {
  color: red;
  font-weight: bold;
}


input {
  width: 75%;
  outline: none;
  height: 20px;
  font-size: 0.8rem;
}


button {
  display: block;
  width: 25%;
  height: 25px;
  outline: none;
  border-radius: 5px;
  white-space: nowrap;
  margin: 0 10px;
  font-size: 0.8rem;
}


</style>
