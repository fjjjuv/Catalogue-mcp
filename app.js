(function(){
'use strict';
const bt=document.getElementById('backTop');
if(bt){window.addEventListener('scroll',()=>{bt.classList.toggle('visible',scrollY>400)});
bt.addEventListener('click',()=>scrollTo({top:0,behavior:'smooth'}));}
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target)}}),{threshold:.1});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
})();