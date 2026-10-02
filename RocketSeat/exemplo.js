function a() {
if(n>0) {
console.log('positivo')
}else if(n<0) {
console.log('negativo')
}
else {
console.log('zero')}}
function b(arr) {let s=0; for(let i=0; i<arr.length; i++) {s+=arr[i]} 
return s}
let x=[1,2,3,4,5]
let y=b(x)
console.log('soma:'+y)
for(let i=0; i<x.length; i++){
if(x[i]%2==0) {console.log(x[i]+' é par')}
else {console.log(x[i]+' é ímpar')}}
a(10)
a(0)
a(-5)
