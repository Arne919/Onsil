import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
    },
    {
      name: '김두리',
      balance: 10000
    },
    {
      name: '김서이',
      balance: 100
    },
  ])

  const getDetailInfo = (name) => {
    console.log('method is called!!')
    return balances.value.filter((info) => info.name === name)[0]
  }
  
  const detailInfo = computed (() => {
    console.log('computed is called!!')
    return (name) => balances.value.filter((info) => info.name === name)[0]
  })

  const updateBalance = function (name) {
    balances.value = balances.value.map((info) => {
      if (info.name === name) {
        info.balance += 1000
      }
      return info
    })
  }
  return { balances, detailInfo, updateBalance, getDetailInfo }
})
