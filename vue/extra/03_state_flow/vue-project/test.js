const A = {
  some() {
    return 'A'
  }
}

const B = {
  some(data) {
    return data
  }
}

console.log(A.some())
console.log(B.some('Alice'))