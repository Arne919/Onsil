// 원래 assets 폴더에 있던 파일들 지웠다면? 
// 불러오는 코드도 당연히 지워야 동작한다!!
// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
