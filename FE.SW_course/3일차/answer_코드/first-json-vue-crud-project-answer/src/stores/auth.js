import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const BASE_URL = "http://localhost:3000"; // API 서버 주소

export const useAuthStore = defineStore(
  "auth",
  () => {
    const user = ref(null);
    const token = ref(null); // ref(localStorage.getItem("token"));
    const error = ref(null);

    const isAuthenticated = computed(() => !!token.value);

    async function register(credentials) {
      try {
        const response = await axios.post(BASE_URL + "/register", credentials);
        token.value = response.data.accessToken;
        user.value = response.data.user;
        // localStorage.setItem("token", token.value);
        // axios.defaults.headers.common["Authorization"] = `Bearer ${token.value}`;
      } catch (err) {
        error.value = err.response?.data || "회원가입 중 오류가 발생했습니다.";
        throw err;
      }
    }

    async function login(credentials) {
      try {
        const response = await axios.post(BASE_URL + "/login", credentials);
        token.value = response.data.accessToken;
        user.value = response.data.user;
        // axios.defaults.headers.common["Authorization"] = `Bearer ${token.value}`;
      } catch (err) {
        error.value = err.response?.data || "로그인 중 오류가 발생했습니다.";
        throw err;
      }
    }

    function logout() {
      user.value = null;
      token.value = null;
      // localStorage.removeItem("token");
      // delete axios.defaults.headers.common["Authorization"];
    }

    return {
      user,
      token,
      error,
      isAuthenticated,
      register,
      login,
      logout,
    };
  },
  { persist: true }
);
