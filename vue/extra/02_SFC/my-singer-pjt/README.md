# my-singer-pjt

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### 컴포넌트 다루기
- 각 영역마다 필요에 따라서 작업 도중에라도, 새로운 컴포넌트로 구분할 필요가 있다면, 새 `.vue` 파일을 만들어서 관리하면 된다.
- 그렇게 컴포넌트들을 늘려나가다보면, `components` 폴더가 지저분해진다.
- 그럴땐, 폴더를 기능별로 만들면되다.
- 예를들어, componets/articles/ArticleList.vue
          componets/accounts/UserList.vue
- 물론, 프로젝트 작업도중에, 이렇게 폴더 경로를 바꾸게 되면?
  - 우리가 import 하려고 적어둔 from의 폴더 경로가 바뀌게 된다.
  - 그럼 열심히 돌아다니면서 수정해야한다. (귀찮다)
  - 따라서, 프로젝트를 시작하기전, 컴포넌트는 어떻게 구성할지 미리 계획해두자.