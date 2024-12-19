## why SFC?

1. vue로 만드는 페이지가 복잡해진다.
2. 하나의 프로젝트로 관리하기가 복잡해진다.
3. vite라는걸 사용해서 쉽게 관리하자.

-> SPA (즉, 단 한장의 index.html) 를 만든다.

```bash
$ npm create vue@latest
$ project name : 'django와 똑같다.'
# typescript -> JS (FE) 공부를 하면 필수적으로 따라오게 될건데
# 2학기가서 시간 남으면 그때 공부하면된다.
# vue router -> 라우터 (경로 설정 관리자) django에서 url
# route -> 루트 (경로)
# pinia -> data 관리자 
  # 컴포넌트들 간의 데이터를 어떻게 넘겨주지? 
  # setup 이라는 곳에 변수를 정의하고, data로 사용하고 있었는데
  # 각각의 컴포넌트는 서로 다른 .vue 파일에서 다룬다. -> 내일
    # 목요일 배우는 방법으로는 이 컴포넌트가 엄청 많아지면 복잡하다.
    # pinia를 써서 쉽게 관리할거다.
$ cd pjt-name
$ npm install
# package.json에 들어있는 내용을 기반으로
# 이 프로젝트를 구동하는데 필요한 라이브러리를 설치
# venv와 requirements.txt와 유사한 기능
$ npm run dev
# http://localhost:5173/ vue의 port
# http://127.0.0.1:8000/ django의 port
# 동일한 경로라도, port가 달라지면 서로 다른 요청을 받을 수 있다.
# 학기말에는 그래서 로컬 컴퓨터에 django랑 vue랑 같이 서버를 열어둘거다.
```

```html
<!-- index.html -->
<!--
  SPA의 핵심이 되는 메인 페이지 단 한장.
  id가 app인 요소 하나, 모든 컴포넌트는 이곳에서 다룬다.
-->
```

```js
import './assets/main.css'
// CDN 시절에는 const { createApp } 형식으로
// 변수에 할당 했는데...

// 이제는 import? 를 쓴다?
// 사실 python떄 이미 써봤음!! 
// from django.shortcuts import render
// import에도 객체구조분해할당을 쓸수있는 이유는?
// vue 모듈이 반환하는 값이 객체기 떄문에
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```

```json
// ctrl + shift + p
// vscode 설정 검색 창이 나온다.
// snippets 이라고 작성하면 나오는
// Configure User Snippets 을 선택한다.
// vue를 다시 검색한다.
// vue.json을 선택한다.
// 거기에 아래 코드를 붙여넣기한다.
{
	// Place your snippets for vue here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"vue for ssafy": {
		"prefix": "vue", // .vue 확장자 파일에서 vue라고 적으면 자동완성
		"body": [
"<template>",
"",
"</template>",
"",
"<script setup>",
"",
"</script>",
"",
"<style scoped>",
"",
"</style>",
		],
		"description": "vue for ssafy snippet"
	}
}
```